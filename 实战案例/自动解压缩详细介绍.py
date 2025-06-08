# 模块导入
import zipfile  # 用于处理 ZIP 文件（解压和压缩）
import os  # 提供操作系统相关的功能，如路径操作和文件管理
import datetime  # 用于处理日期和时间
import time  # 提供时间相关的功能，如测量程序运行时间

# 配置路径
download_dir = r'D:\test_yk\Download_file'  # ZIP 文件存储的目录
output_base_dir = r'D:\test_yk\Compressed_file'  # 解压后的文件及压缩后的新文件存储的目录
log_path = os.path.join(output_base_dir, 'process_log.txt')
# 日志文件路径 os.path: 这是 os 模块下的一个子模块，专门用于处理路径名的常见操作 os内置模块 output_base_dir: 这是一个变量 'process_log.txt': 这是你想要在该目录下创建的文件名

# 当前日期与时间
date_str = datetime.datetime.today().strftime('%Y-%m-%d')
# 获取今天的日期，格式为 YYYY-MM-DD 第二个 datetime，指的是 datetime 模块中的一个类
#.today(): 这是一个方法，它属于 datetime.datetime 这个类。当你调用它时（后面跟着括号 ()），它会返回一个 datetime 对象，这个对象代表了当前本地的日期和时间（也就是今天的日期和当前的时间）。
"""strf "string format"（字符串格式化）。
time 指的是时间。
strftime ：“将一个时间对象格式化成字符串”。
'%Y-%m-%d'：这是一个格式字符串。它告诉 strftime() 你希望日期被格式化成什么样子：
%Y: 表示完整的年份（例如：2025）。
%m: 表示月份，会用零来填充，始终是两位数字（例如：6 月是 06）。
%d: 表示日期（一个月中的哪一天），同样会用零填充，始终是两位数字（例如：7 号是 07）。
整行代码的含义：这行代码会先获取当前的日期和时间，然后将这个日期格式化成 "YYYY-MM-DD"（例如 "2025-06-07"）这样的字符串形式，最后把这个格式化好的日期字符串存储到名为 date_str 的变量中"""
hour_tag = '12'  # 将字符串值 '12' 直接赋值给名为 hour_tag 的变量

# 创建日志文件
os.makedirs(output_base_dir, exist_ok=True)  # 如果目标目录不存在，则创建该目录
"""os: 这是 Python 的内置模块，提供了与操作系统交互的功能
.: 在这里是点运算符，用于访问模块（或对象）内的函数或属性。
makedirs: 这是 os 模块下的一个函数。它的作用是“make directories”，即创建多级目录。
( ): 这是函数调用符，表示你在执行 makedirs 这个函数，括号里是传递给函数的参数。
output_base_dir: 这是一个变量，它存储着你想要创建的目录的路径
exist_ok=True: 这是 makedirs 函数的一个关键字参数。
exist_ok: 这是一个参数名，它的字面意思是“如果存在就确定”。
True: 这是一个布尔值（真/是）。
当 exist_ok 设置为 True 时，如果 output_base_dir 指定的目录已经存在，os.makedirs() 不会抛出错误。如果设置为 False（默认值），并且目录已存在，则会抛出 FileExistsError 错误。
在实际应用中，设置为 True 通常是为了确保目录存在，而不管它是否是新创建的，这让代码更健壮。
"""
log_file = open(log_path, 'a', encoding='utf-8')  # 打开日志文件，以追加模式写入 log_path: 这是一个变量，它存储着你要打开的日志文件的完整路径
log_file.write(f"\n\n=== 处理时间：{datetime.datetime.now()} ===\n")
# 在日志中 log_file:#{datetime.datetime.now()}: 这是 f-string 中嵌入的表达式。
# datetime.datetime: 再次引用 datetime 模块中的 datetime 类。
# .now(): 这是 datetime 类的一个方法，它返回一个 datetime 对象，代表当前精确的日期和时间。
# 当这个对象在 f-string 的花括号 {} 中时，Python 会自动把它转换成一个可读的字符串形式（例如：2025-06-07 21:13:06.123456）。
# 这是上一行代码中我们获取到的文件对象录当前处理时间 .: 点运算符，用于访问对象的方法或属性。

# 遍历 ZIP 文件
start_time = time.time()  # 记录脚本运行的开始时间 内置模块time，time（）第一个time下面的函数，调用后返回时间
#记录当前脚本开始运行时的精确时间。它通过 time.time() 函数获取一个表示当前时间的浮点数（时间戳），并把这个时间戳存储在名为 start_time 的变量中。这个时间戳通常会在脚本结束时用来计算脚本总共运行了多长时间。
zip_files = [f for f in os.listdir(download_dir) if f.lower().endswith('.zip')]  # 获取 download_dir 中所有 .zip 文件
#zip_files: 这是一个变量名。它将存储一个列表，这个列表里会包含 download_dir 目录下所有以 .zip 结尾的文件名
"""f: 这是一个临时变量，代表 os.listdir(download_dir) 遍历到的每一个文件或目录的名称。
for f in os.listdir(download_dir): 这是列表推导式的循环部分。
os.listdir(download_dir):
os: Python 的 os 模块。
.listdir(): os 模块下的一个函数，它接收一个目录路径作为参数（这里是 download_dir 变量的值），并返回该目录中所有文件和子目录的名称列表（字符串形式），这些名称不包含完整的路径。
所以，for f in os.listdir(download_dir) 的意思是，遍历 download_dir 目录下所有文件和目录的名称，并把每个名称暂时赋值给 f。"""
if not zip_files:  # 如果没有找到 ZIP 文件
    log_file.write("⚠️ 未找到任何 ZIP 文件。\n")  # 写入日志文件 log_file: 这是前面通过 open() 函数获取到的文件对象（代表你打开的日志文件）。
    print("⚠️ 未找到任何 ZIP 文件。")  # 输出到控制台

# 处理每个 ZIP 文件
for filename in zip_files:#这行代码启动一个循环，它会依次遍历 zip_files 列表中存储的每一个 ZIP 文件名。在每一次循环中，当前的 ZIP 文件名都会被赋值给 filename 变量，然后执行循环体内（即下面缩进的代码）的操作。
#filename: 这是一个临时变量。在每次循环中，zip_files 列表中的一个元素（也就是一个 ZIP 文件的名称，例如 'my_archive.zip'）会被依次赋值给这个 filename 变量。
#in: 这是一个成员运算符，用于检查一个值是否在序列中，
# 在这里它用于指定循环的范围zip_files: 这是之前我们通过列表推导式获取到的列表变量，里面包含了 download_dir 目录下所有 .zip 文件的文件名。
# :: 这是 for 循环的冒号，表示循环头部结束，后面缩进的代码块是循环体，会针对 zip_files 中的每个 filename 执行。
    t0 = time.time()  # 记录每个 ZIP 文件处理的开始时间 在每次循环开始处理一个新的 ZIP 文件时，记录下当前的精确时间。这个时间戳 t0 将用于后续计算处理该单个 ZIP 文件所花费的时间。
    zip_path = os.path.join(download_dir, filename)  # 这行代码的作用是构造出当前正在处理的 ZIP 文件的完整路径。它将存储目录路径的 download_dir 和当前文件名 filename 安全地组合起来，形成一个可以直接用来访问该文件的完整路径
# 获取 ZIP 文件的完整路径 download_dir: 这是一个变量，存储着 ZIP 文件所在的目录路径。 filename: 这是当前循环中正在处理的 ZIP 文件名
    zip_name = os.path.splitext(filename)[0]  # 获取文件名（不包含扩展名）
# os.path 模块下的一个函数，用于将文件名分割成两部分：主文件名和扩展名。它返回一个元组 (tuple)，元组的第一个元素是文件名（不包含扩展名），第二个元素是扩展名（包含开头的点 .）。
#filename: 当前循环中正在处理的 ZIP 文件名。
#[0]: 这是索引操作符。因为 os.path.splitext() 返回的是一个元组（例如 ('my_archive', '.zip')），[0] 表示我们只取出这个元组中的第一个元素，也就是不包含扩展名的文件名部分。
    print(f"\n📦 正在处理：{zip_name}")  # 打印当前正在处理的文件名
    log_file.write(f"\n📦 正在处理：{zip_name}\n")  # 写入日志文件


    # 创建解压目录
    output_dir = os.path.join(output_base_dir, zip_name)  # 定义解压后的文件存储路径
    os.makedirs(output_dir, exist_ok=True)  # 如果路径不存在则创建

    # 解压 ZIP 文件 这个代码块的主要目的是尝试解压一个 ZIP 文件，并在解压过程中出现任何问题时捕获并报告错误
    try: #try: 这是 Python 中异常处理的关键字之一。它标志着一个代码块的开始，在这个代码块中，你预期可能会发生错误（即“异常”）。如果 try 块中的代码运行没有问题，那么 except 块就会被跳过。
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:  # 打开 ZIP 文件
            #with: 这是 Python 的上下文管理器 (Context Manager) 关键字。它用于确保资源（比如文件）在使用后被正确地关闭和清理，即使在处理过程中发生错误。使用 with 语句可以省去手动调用 close() 方法的麻烦，是处理文件 I/O 的推荐方式。
            #zipfile: 这是 Python 的一个内置模块，专门用于创建、读取、写入和解压 ZIP 压缩文件。
            #zip_path: 这是一个变量，存储着当前要解压的 ZIP 文件的完整路径
            #'r': 这是打开 ZIP 文件的模式。
            #as: 这是 with 语句的一部分，用于给通过上下文管理器创建的对象指定一个别名。
            # #zip_ref: 这是一个变量名，它存储着 zipfile.ZipFile 类返回的ZIP 文件对象。通过这个 zip_ref，你可以调用解压、读取等相关方法。
            #整行代码的含义：这行代码使用 with 语句安全地打开由 zip_path 指定的 ZIP 文件，并以只读模式 ('r') 进行操作。一旦文件成功打开，一个表示该 ZIP 文件的对象就会被创建并赋值给 zip_ref。with 语句确保无论解压成功与否，这个 ZIP 文件都会在 with 块结束后被自动关闭，防止资源泄露。
            zip_ref.extractall(output_dir)  # 解压所有内容到指定目录
            #zip_ref: 这是前面通过 zipfile.ZipFile() 打开的ZIP 文件对象。
            # extractall(): 这是 zip_ref 对象的一个方法，用于解压 ZIP 文件中的所有内容
            # output_dir: 这是一个变量，它存储着解压后的文件将要存放的目标目录路径
            # 整行代码的含义：这行代码会将当前 ZIP 文件 (zip_ref 所指向的) 中包含的所有文件和目录都解压到由 output_dir 变量指定的目录中。
    except Exception as e:  # 如果解压过程中出现异常
        """except: 这是 Python 中异常处理的另一个关键字。它紧跟在 try 块之后，用于捕获并处理 try 块中可能发生的特定类型或所有类型的错误。
Exception: 这是一个 Python 内置的基类，代表了所有非系统退出的异常。使用 Exception 可以捕获大多数常见的错误（例如文件不存在、权限问题、ZIP 文件损坏等）。
as: 这是 except 语句的一部分，用于给捕获到的异常指定一个别名。
e: 这是一个变量名，用来存储捕获到的异常对象。通过这个 e，你可以获取到关于错误的详细信息（例如错误消息）。
:: except 语句的冒号，表示异常处理块的开始。
整行代码的含义：这行代码表示“如果在前面的 try 块中发生了任何类型的异常（除了那些表示程序即将退出的系统异常），那么就捕获这个异常，并把它赋值给变量 e，然后执行这个 except 块中的代码”。"""
        log_file.write(f"❌ 解压失败：{e}\n")  # 写入日志文件 og_file.write(...): 这会将一条错误信息写入之前打开的日志文件。
        print(f"❌ 解压失败：{e}")  # 打印异常信息到控制台
        continue  # 跳过当前文件，处理下一个

    # 找顶层解压目录
    top_dirs = [d for d in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, d))]  # 获取解压目录下的所有子目录
    """d: 这是一个临时变量，代表 os.listdir(output_dir) 遍历到的每一个文件或目录的名称。
for d in os.listdir(output_dir): 这是列表推导式的循环部分。
os.listdir(output_dir):
os: Python 的 os 模块。
.listdir(): os 模块下的一个函数，它接收一个目录路径（这里是 output_dir 变量的值），并返回该目录中所有文件和子目录的名称列表（字符串形式）。这些名称不包含完整的路径，只是文件名或目录名。
所以，for d in os.listdir(output_dir) 的意思是遍历 output_dir 目录下所有文件和目录的名称，并将每个名称暂时赋值给 d。
if os.path.isdir(os.path.join(output_dir, d)): 这是列表推导式的条件过滤部分。只有满足这个条件的元素才会被包含在最终的 top_dirs 列表中。
os.path.join(output_dir, d): 在这里，os.path.join() 函数再次被使用。它将基础解压目录 output_dir 和当前遍历到的文件/目录名 d 拼接起来，形成一个完整的路径。这是必要的，因为 os.listdir() 只返回名称，而 os.path.isdir() 需要一个完整的路径来判断。
os.path.isdir(...): 这是 os.path 模块下的一个函数。它接收一个完整的路径作为参数，然后判断这个路径是否指向一个实际存在的目录。如果是目录，则返回 True；否则返回 False（如果是文件或者不存在的路径）。
所以，if os.path.isdir(os.path.join(output_dir, d)) 的意思是只选择那些在 output_dir 目录下实际是子目录的条目。
整行代码的含义：这行代码的作用是检查 output_dir（即 ZIP 文件的解压目标目录）下的所有内容，并从中筛选出所有直接的子目录。它会将这些子目录的名称收集到一个名为 top_dirs 的列表中。"""
    if not top_dirs:  # 如果没有找到任何子目录
        log_file.write("❌ 未找到顶层目录，跳过此文件。\n")  # 写入日志文件
        continue  # 跳过当前文件

    data_root = os.path.join(output_dir, top_dirs[0])  # 假设第一个子目录为数据根目录

    # 定义目标子目录与命名规则
    folder_map = { #folder_map: 这是我们创建的这个字典的变量名
        'LIDAR-CAMERA': f'{zip_name}-CAMERA-LIDAR-{date_str}-{hour_tag}',
        'LIDAR-HLU': f'{zip_name}-LIDAR-HLU-{date_str}-{hour_tag}',
        'RADAR-CAMERA': f'{zip_name}-RADAR-CAMERA-{date_str}-{hour_tag}',
        #'LIDAR-CAMERA': 这是这个键值对中的键（key）。
        # 它是一个字符串字面量 通过这些变量值和固定文本的组合，这个 f-string 会动态地生成一个独特的文件夹名称字符串。
        # 例如，如果 zip_name 是 "ProjectA"，date_str 是 "2025-06-07"，hour_tag 是 "12"，那么这个值就会变成："ProjectA-CAMERA-LIDAR-2025-06-07-12"。
    }

    # 压缩每个子目录
    for subfolder, output_name in folder_map.items():
        """for: 这是 Python 的循环关键字，用于遍历序列（如列表、元组、字符串）或字典中的元素。
subfolder, output_name: 这是两个临时变量。在每次循环中，folder_map 字典的一个键值对会被解包（unpacked）并分别赋值给这两个变量。
subfolder 将得到字典中当前的键（key），例如 'LIDAR-CAMERA'。
output_name 将得到字典中当前键对应的值（value），例如 'ProjectA-CAMERA-LIDAR-2025-06-07-12'。
in: 这是一个成员运算符，表示循环的范围。
folder_map.items(): 这是字典的一个方法。当你调用它时，它会返回一个由字典中所有键值对组成的视图对象。每个键值对都是一个元组（例如 ('LIDAR-CAMERA', 'ProjectA-CAMERA-LIDAR-2025-06-07-12')）。这个方法使得你可以同时获取到字典的键和值进行遍历。
:: 这是 for 循环的冒号，表示循环头部结束，其后缩进的代码块是循环体，会针对 folder_map 中的每一个键值对执行。
整行代码的含义：这行代码启动一个循环，它会逐个遍历 folder_map 字典中的每一个键值对。在每次循环中，
当前键值对的键（代表预期的子目录名称）会被赋值给 subfolder 变量，而对应的值（代表新文件夹的最终名称）会被赋值给 output_name 变量。然后，程序会执行循环体内（即下面缩进的代码）的操作。"""
        subfolder_path = os.path.join(data_root, subfolder)  # 定义子目录路径
        #这行代码的作用是构造出当前正在检查的子目录的完整路径。它将 data_root 路径与 subfolder 名称拼接起来，形成一个可以直接用来检查该子目录是否存在或访问其内容的完整路径。
        # 例如，如果 data_root 是 '/home/user/data/ProjectA' 且 subfolder 是 'LIDAR-CAMERA'，那么 subfolder_path 就会是 '/home/user/data/ProjectA/LIDAR-CAMERA'
        if not os.path.isdir(subfolder_path):  # 如果子目录不存在
            """os.path.isdir(): 这是 os.path 模块下的一个函数。它接收一个完整路径作为参数，并判断这个路径是否指向一个实际存在的目录。如果路径是目录，返回 True；否则返回 False。
( ): 函数调用符，括号里是传递给函数的参数。
subfolder_path: 这是上一步构造出的子目录的完整路径。
所以，os.path.isdir(subfolder_path) 会判断 subfolder_path 是否是一个存在的目录。
然后，not os.path.isdir(subfolder_path) 的意思是：“如果 subfolder_path 不是一个存在的目录（即 os.path.isdir() 返回 False，not 把它变成 True）”。
:: 这是 if 语句的冒号，表示条件判断部分的结束，后面是满足条件时要执行的代码块。
整行代码的含义：这行代码会检查由 subfolder_path 指定的子目录是否存在。如果这个子目录不存在，那么 if 语句的条件就会成立，程序将执行其后的缩进代码块。"""
            log_file.write(f"⚠️ 跳过：未找到 {subfolder}\n")  # 写入日志文件
            print(f"⚠️ 跳过：未找到 {subfolder}")  # 输出到控制台
            continue  # 跳过该子目录
#如果当前正在检查的子目录 (subfolder) 在 data_root 中不存在，这条 continue 语句会确保程序立即结束对这个不存在的子目录的当前处理。
        # 它会跳过 for 循环中所有针对该子目录的后续代码，直接开始处理 folder_map 字典中的下一个键值对（即下一个预期的子目录）。这使得脚本能够灵活地处理解压内容不完全符合所有预期的情况，避免因缺失某些子目录而导致程序崩溃。
        output_zip = os.path.join(output_dir, f"{output_name}.zip")  # 定义压缩后的 ZIP 文件路径
        #f"{output_name}.zip": 这是一个 f-string，用来动态生成新 ZIP 文件的文件名。
#output_name: 这是一个变量（来自 folder_map 的值），它存储着为当前传感器组合生成的新文件夹名称（例如 ProjectA-CAMERA-LIDAR-2025-06-07-12）。
        with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:  # 创建新的 ZIP 文件
            #with: 这是 Python 的上下文管理器关键字
            #zipfile.ZipFile(): 这是 zipfile 模块中的一个类
            #zipfile.ZIP_DEFLATED: 这是 zipfile 模块中的一个常量，指定了压缩方法
            #as zipf: 这是 with 语句的一部分，将创建的 ZIP 文件对象赋值给变量 zipf。在这个 with 块中，你可以通过 zipf 来操作这个 ZIP 文件
            for root, dirs, files in os.walk(subfolder_path):  # 遍历子目录及其所有文件
                #root, dirs, files: 这是三个临时变量。os.walk() 函数在每次迭代时会返回一个三元组，这个元组会被解包并分别赋值给这三个变量：
                #os.walk(): 这是 os 模块下的一个函数，用于生成目录树中的文件名
                for file in files:
                    #这是内层循环，遍历 os.walk() 在当前 root 目录下找到的文件列表。file: 这是一个临时变量，在每次循环中，files 列表中的一个文件名（例如 'sensor_data.csv'）会被赋值给 file。
                    file_path = os.path.join(root, file)  # 获取文件完整路径
                    arcname = os.path.relpath(file_path, subfolder_path)  # 计算相对路径 file_path: 待计算相对路径的完整文件路径。
                    zipf.write(file_path, arcname)  # 添加文件到 ZIP 包中

        log_file.write(f"✅ 压缩完成：{output_zip}\n")  # 写入日志文件
        print(f"✅ 压缩完成：{output_zip}")  # 打印成功信息

    # 删除原始 ZIP 文件
    try:
        os.remove(zip_path)  # 删除 ZIP 文件
        log_file.write(f"🗑️ 已删除原始 ZIP 文件：{zip_path}\n")  # 写入日志文件
    except Exception as e:  # 如果删除过程中出现异常
        log_file.write(f"⚠️ 删除 ZIP 文件失败：{e}\n")  # 写入日志文件

    t1 = time.time()  # 记录文件处理结束时间
    log_file.write(f"⏱️ 耗时：{t1 - t0:.2f} 秒\n")  # 写入处理时间到日志

# 总耗时
end_time = time.time()  # 记录脚本运行的结束时间
total_seconds = end_time - start_time  # 计算总耗时
log_file.write(f"\n✅ 所有压缩包处理完成，总耗时：{total_seconds:.2f} 秒\n")  # 写入总耗时到日志
print(f"\n✅ 所有压缩包处理完成，总耗时：{total_seconds:.2f} 秒")  # 输出总耗时到控制台
log_file.close()  # 关闭日志文件
