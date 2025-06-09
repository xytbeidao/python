with open("log1.txt", "r", encoding="utf-8") as file:  # 读取日志文件
    lines = file.readlines()  # 把每一行都读成一个列表元素

for line in lines:  # 遍历每一行
    if "障碍" in line:  # 如果这一行包含“障碍”这个词
        print("匹配到：", line.strip())  # 打印这行，strip() 去除首尾空格和换行符
