with open("log.txt", "r", encoding="utf-8") as file:  # 打开文件，使用 with 是为了读完自动关闭文件
    content = file.read()  # 读取整个文件内容到一个字符串中

word = "无人车"  # 要统计的目标词

count = content.count(word)  # 统计这个词在整个文本中出现了多少次

print(f"‘{word}’ 出现了 {count} 次")  # 使用格式化字符串打印结果
