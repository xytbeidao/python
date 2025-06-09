#1. 初始化文件
#2. 提供功能选项（添加学生、查看成绩、计算平均分、搜索学生）
#3. 用户选择功能后，调用对应模块
#4. 记录日志
#5. 循环，直到用户退出

import os  # 操作系统模块，用于文件路径操作
from datetime import datetime  # 日期时间模块

# 定义一个文件路径 (file path: 文件路径)
file_path = "students_scores.txt"  # 用于存储学生成绩的文件

# 函数：初始化文件 (initialize: 初始化)
def initialize_file():
    if not os.path.exists(file_path):  # 检查文件是否存在
        with open(file_path, "w") as file:  # 如果文件不存在，创建文件
            file.write("姓名,数学,英语,科学\n")  # 写入表头
        print("文件已初始化！")

# 函数：添加学生成绩 (add: 添加)
def add_student_score(name, math, english, science):
    with open(file_path, "a") as file:  # 以追加模式打开文件
        file.write(f"{name},{math},{english},{science}\n")  # 写入学生成绩
    print(f"成功添加学生 {name} 的成绩！")

# 函数：读取所有学生成绩 (read: 读取)
def read_all_scores():
    with open(file_path, "r") as file:  # 以只读模式打开文件
        lines = file.readlines()  # 读取所有行
    print("学生成绩列表：")
    for line in lines:  # 遍历每一行
        print(line.strip())  # 去掉行尾的换行符并打印

# 函数：计算每个学生的平均成绩 (average: 平均值)
def calculate_averages():
    averages = []  # 用于存储每个学生的平均成绩
    with open(file_path, "r") as file:
        lines = file.readlines()[1:]  # 跳过表头
        for line in lines:
            parts = line.strip().split(",")  # 按逗号分割字符串
            name = parts[0]  # 获取学生姓名
            scores = list(map(int, parts[1:]))  # 转换成绩为整数列表
            avg = sum(scores) / len(scores)  # 计算平均分
            averages.append((name, avg))  # 保存姓名和平均分
    print("学生平均成绩：")
    for name, avg in averages:
        print(f"{name}: {avg:.2f}")  # 输出格式化的平均分
    return averages

# 函数：查找学生成绩 (search: 搜索)
def search_student(name):
    with open(file_path, "r") as file:
        lines = file.readlines()[1:]  # 跳过表头
        for line in lines:
            if line.startswith(name):  # 如果行以学生姓名开头
                print(f"找到学生：{line.strip()}")  # 输出学生信息
                return line.strip()
    print(f"未找到学生 {name} 的记录！")
    return None

# 函数：获取当前时间并记录日志 (log: 日志)
def log_operation(operation):
    now = datetime.now()  # 获取当前时间
    with open("log.txt", "a") as log_file:  # 打开日志文件
        log_file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {operation}\n")  # 写入操作日志

# 主程序入口 (main: 主函数)
if __name__ == "__main__":
    initialize_file()  # 初始化文件
    log_operation("初始化文件")

    # 添加一些学生成绩
    add_student_score("Alice", 90, 85, 88)
    log_operation("添加学生成绩: Alice")
    add_student_score("Bob", 78, 82, 80)
    log_operation("添加学生成绩: Bob")
    add_student_score("Charlie", 95, 90, 93)
    log_operation("添加学生成绩: Charlie")

    # 读取并显示所有学生成绩
    read_all_scores()
    log_operation("读取所有学生成绩")

    # 计算并显示学生平均成绩
    calculate_averages()
    log_operation("计算学生平均成绩")

    # 查找特定学生的成绩
    search_student("Alice")
    log_operation("搜索学生成绩: Alice")
