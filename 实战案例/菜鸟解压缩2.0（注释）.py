import os       # 导入 os 模块，用于文件和目录操作（如创建目录、检查路径）
import zipfile  # 导入 zipfile 模块，用于 ZIP 文件的创建、读取和解压
import shutil   # 导入 shutil 模块，用于高级文件操作（如移动、复制文件/目录）
import datetime # 导入 datetime 模块，用于处理日期和时间
import time     # 导入 time 模块，用于时间相关功能（如暂停执行）

# 路径配置 (请根据您的环境修改)
download_dir = r'D:\test_yk\Download_file'      # 定义下载文件存放的目录，r'...' 表示原始字符串，避免转义符问题
output_base_dir = r'D:\test_yk\Compressed_file' # 定义处理后压缩文件输出的基目录
internal_control_base = r'D:\test_yk\Internal_control_file' # 定义内部控制文件存放的基目录
poll_interval = 300  # 轮询间隔，单位：秒 (5分钟)

# ---- 不需要修改下面的内容 ----
log_path = os.path.join(output_base_dir, 'process_log.txt') # 构建日志文件的完整路径，存放在输出基目录下
processed_files = set() # 创建一个空集合，用于存储已经处理过的文件名，避免重复处理

def write_log(msg):
    """写入日志并打印到控制台""" # 定义一个函数，用于写入日志并打印
    log_msg = f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}" # 格式化日志消息，包含当前时间戳
    with open(log_path, 'a', encoding='utf-8') as f: # 以追加模式 ('a') 打开日志文件，使用 UTF-8 编码
        f.write(log_msg + "\n") # 将格式化后的日志消息写入文件，并换行
    print(log_msg) # 同时将日志消息打印到控制台

def check_subfolder_structure(car_path):
    """
    检查车号文件结构完整性 (已取消文件数量检查)
    """ # 定义一个函数，用于检查解压后的车号文件夹内部结构
    errors = [] # 初始化一个空列表，用于存放结构检查中发现的错误

    # 检查核心文件夹是否存在
    required_folders = ['camera_intrinsic_senyun', 'LIDAR-CAMERA', 'LIDAR-HLU', 'RADAR-CAMERA'] # 定义必须存在的子文件夹列表
    for folder in required_folders: # 遍历每个必需的文件夹
        if not os.path.exists(os.path.join(car_path, folder)): # 检查该文件夹在车号路径下是否存在
            errors.append(f"❌ 结构检查失败：缺少文件夹 {folder}") # 如果不存在，添加错误信息

    if not errors: # 如果 errors 列表为空，表示没有发现错误
        write_log(f"✅ {os.path.basename(car_path)} 核心文件夹结构存在。") # 写入日志表示结构检查通过

    return errors # 返回错误列表（如果为空则表示无错误）


def zip_directory(path, zip_handler, arc_prefix=''):
    """递归压缩目录，并可以指定在压缩包内的前缀""" # 定义一个函数，用于递归地将指定目录下的所有文件压缩到 ZIP 文件中
    for root, dirs, files in os.walk(path): # 遍历指定路径下的所有目录和文件（os.walk 会递归遍历）
        for file in files: # 遍历当前目录下的所有文件
            file_path = os.path.join(root, file) # 获取当前文件的完整路径
            # 创建在zip文件中的相对路径
            arcname = os.path.relpath(file_path, path) # 计算文件相对于指定路径的相对路径，作为在 ZIP 包中的名称
            if arc_prefix: # 如果指定了压缩包内的前缀
                arcname = os.path.join(arc_prefix, arcname) # 将前缀添加到相对路径前
            zip_handler.write(file_path, arcname) # 将文件写入 ZIP 包，并指定其在包内的路径名

def create_combined_intrin_zip(car_id, output_dir, intrin_senyun_path, date_str, hour_tag):
    """
    新功能：将 camera_intrinsic_senyun 和 Internal_control 文件合并压缩
    """ # 定义一个新函数，用于创建合并了特定文件和内部控制文件的 ZIP 包
    # 定义最终的压缩包名称和路径
    zip_name = f'{car_id}-CAMERA-INTRIN-{date_str}-{hour_tag}.zip' # 格式化合并压缩包的文件名
    zip_out_path = os.path.join(output_dir, zip_name) # 构建合并压缩包的完整输出路径

    try: # 尝试执行以下代码块，捕获可能发生的异常
        with zipfile.ZipFile(zip_out_path, 'w', zipfile.ZIP_DEFLATED) as zf: # 以写入模式 ('w') 创建 ZIP 文件，使用 DEFLATED 压缩算法
            # 1. 添加 camera_intrinsic_senyun
            if os.path.exists(intrin_senyun_path): # 检查 camera_intrinsic_senyun 目录是否存在
                write_log(f"    - 添加 'camera_intrinsic_senyun' 到压缩包...") # 记录日志
                # 将 'camera_intrinsic_senyun' 文件夹本身也作为一层目录放入zip
                zip_directory(intrin_senyun_path, zf, arc_prefix='camera_intrinsic_senyun') # 调用 zip_directory 压缩该目录，并指定在 ZIP 包内的前缀
            else:
                write_log(f"⚠️ 未找到 'camera_intrinsic_senyun' 目录: {intrin_senyun_path}") # 如果目录不存在，记录警告日志

            # 2. 添加内部控制文件
            internal_car_path = os.path.join(internal_control_base, car_id) # 构建车号对应的内部控制文件路径
            if os.path.exists(internal_car_path): # 检查内部控制目录是否存在
                write_log(f"    - 添加内部控制文件从: {internal_car_path}") # 记录日志
                # 遍历内部控制文件下的所有子文件夹
                for subfolder in os.listdir(internal_car_path): # 遍历内部控制目录下的所有文件和子目录
                    subfolder_path = os.path.join(internal_car_path, subfolder) # 获取子文件夹的完整路径
                    if os.path.isdir(subfolder_path): # 如果是子文件夹
                        # 将内部控制的子文件夹也作为一层目录放入zip
                        zip_directory(subfolder_path, zf, arc_prefix=subfolder) # 压缩该子文件夹，并以其自身名称作为 ZIP 包内前缀
            else:
                write_log(f"⚠️ 未找到内部控制目录: {internal_car_path}") # 如果目录不存在，记录警告日志

        write_log(f"📦 合并压缩完成: {zip_out_path}") # 记录合并压缩完成的日志
        return zip_out_path # 返回创建的 ZIP 文件的路径
    except Exception as e: # 捕获所有其他类型的异常
        write_log(f"❌ 合并压缩失败: {e}") # 记录合并压缩失败的错误信息
        return None # 返回 None 表示失败

def move_to_oss(output_dir, created_zips):
    """移动所有生成的压缩包到 oss_Upload 目录""" # 定义一个函数，用于将生成的 ZIP 包移动到指定上传目录
    upload_dir = os.path.join(output_dir, 'oss_Upload') # 构建 OSS 上传目录的完整路径
    os.makedirs(upload_dir, exist_ok=True) # 创建 OSS 上传目录，如果已存在则不报错

    moved_count = 0 # 初始化已移动文件计数器
    for zip_path in created_zips: # 遍历所有已创建的 ZIP 文件路径
        if os.path.exists(zip_path): # 检查 ZIP 文件是否存在
            try: # 尝试执行移动操作
                shutil.move(zip_path, os.path.join(upload_dir, os.path.basename(zip_path))) # 将 ZIP 文件移动到上传目录
                moved_count += 1 # 移动成功，计数器加1
            except Exception as e: # 捕获移动文件时可能发生的异常
                write_log(f"❌ 移动文件失败: {zip_path}, 错误: {e}") # 记录移动失败的错误信息

    if moved_count > 0: # 如果有文件被移动
        write_log(f"📁 {moved_count}个压缩包已移动到: {upload_dir}") # 记录移动成功的日志
    else:
        write_log("🤷‍♂️ 本次处理没有生成任何压缩包。") # 如果没有文件被移动，记录相应日志

def process_zip(zip_name):
    """处理单个ZIP文件""" # 定义一个函数，用于处理从下载目录发现的单个 ZIP 文件
    date_str = datetime.datetime.today().strftime('%Y-%m-%d') # 获取当前日期，格式为 YYYY-MM-DD
    hour_tag = datetime.datetime.now().strftime('%H') # 获取当前小时，格式为 HH
    zip_path = os.path.join(download_dir, zip_name) # 构建原始 ZIP 文件的完整路径
    car_id = os.path.splitext(zip_name)[0] # 从 ZIP 文件名中提取车号（去除 .zip 后缀）
    output_dir = os.path.join(output_base_dir, car_id) # 构建该车号对应的输出目录
    os.makedirs(output_dir, exist_ok=True) # 创建车号对应的输出目录，如果已存在则不报错

    all_created_zips = [] # 初始化一个列表，用于存储本次处理过程中创建的所有新 ZIP 包的路径

    # 1. 解压
    try: # 尝试解压 ZIP 文件
        with zipfile.ZipFile(zip_path, 'r') as zf: # 以读取模式 ('r') 打开 ZIP 文件
            zf.extractall(output_dir) # 将 ZIP 文件中的所有内容解压到输出目录
        write_log(f"✅ 解压完成: {zip_name}") # 记录解压完成日志
    except Exception as e: # 捕获解压过程中可能发生的异常
        write_log(f"❌ 解压失败: {zip_name}, 错误: {e}") # 记录解压失败错误信息
        return # 解压失败则直接返回，不继续后续处理

    # 2. 查找并验证顶层目录，如果不匹配则重命名
    try: # 尝试查找和处理解压后的顶层目录
        # 查找解压后唯一的顶层目录
        top_level_dirs = [d for d in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, d)) and d != 'oss_Upload'] # 列出输出目录下所有非 'oss_Upload' 的子目录
        if not top_level_dirs: # 如果没有找到任何子目录
            raise IndexError("解压后未找到任何有效目录") # 抛出 IndexError 异常

        extracted_folder_name = top_level_dirs[0] # 获取第一个（通常是唯一一个）解压出的顶层目录名
        root_path = os.path.join(output_dir, extracted_folder_name) # 构建解压出的顶层目录的完整路径

        # 【新功能】如果解压出的文件夹名与车号不符，则重命名
        if extracted_folder_name != car_id: # 如果解压出的文件夹名与预期的车号不一致
            write_log(f"⚠️ 文件夹名称不匹配: 期望 '{car_id}', 实际 '{extracted_folder_name}'。正在重命名...") # 记录警告日志
            new_root_path = os.path.join(output_dir, car_id) # 构建重命名后的新路径
            if os.path.exists(new_root_path): # 检查目标重命名路径是否已存在
                write_log(f"❌ 重命名失败，目标文件夹 '{new_root_path}' 已存在。") # 如果已存在，记录错误日志
                return # 重命名失败则返回
            os.rename(root_path, new_root_path) # 执行文件夹重命名操作
            root_path = new_root_path # 更新 root_path 为重命名后的路径
            write_log(f"✅ 文件夹已重命名为: {root_path}") # 记录重命名成功的日志

    except (IndexError, FileNotFoundError) as e: # 捕获索引错误（未找到目录）或文件未找到错误
        write_log(f"❌ 寻找解压目录失败: {zip_name}, 错误: {e}") # 记录错误日志
        return # 寻找解压目录失败则返回

    # 3. 结构校验 (只检查文件夹是否存在)
    errors = check_subfolder_structure(root_path) # 调用函数检查解压后目录的结构完整性
    if errors: # 如果存在结构错误
        for e in errors: # 遍历并记录所有错误信息
            write_log(e)
        # 即使结构不完整，仍然继续尝试压缩
        write_log("ℹ️ 尽管结构不完整，仍将继续尝试压缩。") # 提示即使有错误也继续处理

    # 4. 压缩三个子目录 (LIDAR-CAMERA, LIDAR-HLU, RADAR-CAMERA)
    folder_map = { # 定义需要独立压缩的子文件夹及其对应的输出文件名模板
        'LIDAR-CAMERA': f'{car_id}-CAMERA-LIDAR-{date_str}-{hour_tag}',
        'LIDAR-HLU': f'{car_id}-LIDAR-HLU-{date_str}-{hour_tag}',
        'RADAR-CAMERA': f'{car_id}-RADAR-CAMERA-{date_str}-{hour_tag}',
    }

    for folder, name in folder_map.items(): # 遍历每个需要压缩的子文件夹
        src_path = os.path.join(root_path, folder) # 构建源目录的完整路径
        if not os.path.exists(src_path): # 如果源目录不存在
            write_log(f"⚠️ 压缩跳过：未找到目录 {src_path}") # 记录警告并跳过该目录的压缩
            continue # 继续下一个循环

        zip_out = os.path.join(output_dir, name + '.zip') # 构建输出 ZIP 文件的完整路径
        try: # 尝试压缩子目录
            with zipfile.ZipFile(zip_out, 'w', zipfile.ZIP_DEFLATED) as zf: # 以写入模式创建 ZIP 文件
                zip_directory(src_path, zf) # 压缩源目录到 ZIP 文件
            write_log(f"📦 压缩完成: {zip_out}") # 记录压缩完成日志
            all_created_zips.append(zip_out) # 将新创建的 ZIP 文件路径添加到列表中
        except Exception as e: # 捕获压缩过程中可能发生的异常
            write_log(f"❌ 压缩失败: {folder}, 错误: {e}") # 记录压缩失败错误信息

    # 5. 【新功能】创建合并的 INTRIN 压缩包
    intrin_senyun_path = os.path.join(root_path, 'camera_intrinsic_senyun') # 构建 camera_intrinsic_senyun 目录的完整路径
    combined_zip_path = create_combined_intrin_zip(car_id, output_dir, intrin_senyun_path, date_str, hour_tag) # 调用函数创建合并的 ZIP 包
    if combined_zip_path: # 如果合并 ZIP 包成功创建
        all_created_zips.append(combined_zip_path) # 将其路径添加到列表中

    # 6. 移动所有生成的压缩包到 oss_Upload
    if all_created_zips: # 如果有任何 ZIP 包被创建
        move_to_oss(output_dir, all_created_zips) # 调用函数将所有创建的 ZIP 包移动到上传目录
    else:
        write_log("🤷‍♂️ 本次处理没有生成任何压缩包。") # 如果没有生成任何 ZIP 包，记录日志


# 🕒 主循环：轮询检测
write_log("📡 启动文件夹监控...") # 记录程序启动监控的日志

while True: # 进入无限循环，持续监控
    try: # 尝试执行监控逻辑
        # 查找所有未处理的zip文件
        all_zips = set(f for f in os.listdir(download_dir) if f.endswith('.zip')) # 获取下载目录下所有以 .zip 结尾的文件名，并转换为集合
        new_files = list(all_zips - processed_files) # 从所有 ZIP 文件中减去已处理的文件，得到新的未处理文件列表

        if new_files: # 如果有新文件被发现
            write_log(f"📬 发现 {len(new_files)} 个新文件: {', '.join(new_files)}") # 记录发现新文件的日志
            for zf in new_files: # 遍历每个新文件
                write_log(f"🚀 开始处理: {zf}") # 记录开始处理该文件的日志
                process_zip(zf) # 调用 process_zip 函数处理该文件
                processed_files.add(zf) # 将已处理的文件添加到 processed_files 集合中
                write_log(f"🏁 完成处理: {zf}") # 记录完成处理的日志
                write_log("-" * 40) # 打印分隔线，增强可读性
        else:
            # 使用 print 而非 write_log 来避免日志刷屏
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] ⏳ 无新文件，等待中...", end="\r") # 如果没有新文件，打印等待信息，并使用 \r 实现行内刷新

    except Exception as e: # 捕获主循环中可能发生的任何异常
        write_log(f"❌ 主循环发生严重异常: {e}") # 记录严重异常日志

    time.sleep(poll_interval) # 暂停执行，等待 poll_interval 秒后再次轮询