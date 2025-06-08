import zipfile
import os
import datetime
import time

# 配置路径
download_dir = r'D:\test_yk\Download_file'
output_base_dir = r'D:\test_yk\Compressed_file'
log_path = os.path.join(output_base_dir, 'process_log.txt')

# 当前日期与时间
date_str = datetime.datetime.today().strftime('%Y-%m-%d')
hour_tag = '12'

# 创建日志文件
os.makedirs(output_base_dir, exist_ok=True)
log_file = open(log_path, 'a', encoding='utf-8')
log_file.write(f"\n\n=== 处理时间：{datetime.datetime.now()} ===\n")

start_time = time.time()

# 遍历所有 zip 文件
zip_files = [f for f in os.listdir(download_dir) if f.lower().endswith('.zip')]
if not zip_files:
    log_file.write("⚠️ 未找到任何 ZIP 文件。\n")
    print("⚠️ 未找到任何 ZIP 文件。")
else:
    for filename in zip_files:
        t0 = time.time()
        zip_path = os.path.join(download_dir, filename)
        zip_name = os.path.splitext(filename)[0]
        print(f"\n📦 正在处理：{zip_name}")
        log_file.write(f"\n📦 正在处理：{zip_name}\n")

        # 创建解压目录
        output_dir = os.path.join(output_base_dir, zip_name)
        os.makedirs(output_dir, exist_ok=True)

        # 解压 zip
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(output_dir)
        except Exception as e:
            log_file.write(f"❌ 解压失败：{e}\n")
            continue

        # 找顶层解压目录
        top_dirs = [d for d in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, d))]
        if not top_dirs:
            log_file.write("❌ 未找到顶层目录，跳过此文件。\n")
            continue
        data_root = os.path.join(output_dir, top_dirs[0])

        # 定义目标子目录与命名规则
        folder_map = {
            'LIDAR-CAMERA': f'{zip_name}-CAMERA-LIDAR-{date_str}-{hour_tag}',
            'LIDAR-HLU': f'{zip_name}-LIDAR-HLU-{date_str}-{hour_tag}',
            'RADAR-CAMERA': f'{zip_name}-RADAR-CAMERA-{date_str}-{hour_tag}',
        }

        # 压缩每个子目录
        for subfolder, output_name in folder_map.items():
            subfolder_path = os.path.join(data_root, subfolder)
            if not os.path.isdir(subfolder_path):
                log_file.write(f"⚠️ 跳过：未找到 {subfolder}\n")
                print(f"⚠️ 跳过：未找到 {subfolder}")
                continue

            output_zip = os.path.join(output_dir, f"{output_name}.zip")
            with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(subfolder_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, subfolder_path)
                        zipf.write(file_path, arcname)

            log_file.write(f"✅ 压缩完成：{output_zip}\n")
            print(f"✅ 压缩完成：{output_zip}")

        # 删除原始 ZIP 文件
        try:
            os.remove(zip_path)
            log_file.write(f"🗑️ 已删除原始 ZIP 文件：{zip_path}\n")
        except Exception as e:
            log_file.write(f"⚠️ 删除 ZIP 文件失败：{e}\n")

        t1 = time.time()
        log_file.write(f"⏱️ 耗时：{t1 - t0:.2f} 秒\n")

# 总耗时
end_time = time.time()
total_seconds = end_time - start_time
log_file.write(f"\n✅ 所有压缩包处理完成，总耗时：{total_seconds:.2f} 秒\n")
print(f"\n✅ 所有压缩包处理完成，总耗时：{total_seconds:.2f} 秒")
log_file.close()
