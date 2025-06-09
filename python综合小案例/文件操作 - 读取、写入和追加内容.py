# 打开一个文件进行写入 (open: 打开)
with open("example.txt", "w") as file:  # "w" 表示写模式，文件不存在时会创建
    file.write("Hello, this is a test file.\n")  # write() 方法向文件写入内容

# 打开文件追加内容 (append: 追加)
with open("example.txt", "a") as file:  # "a" 表示追加模式
    file.write("Adding more lines to the file.\n")  # 追加一行内容

# 读取文件内容 (read: 读取)
with open("example.txt", "r") as file:  # "r" 表示只读模式
    content = file.read()  # read() 方法读取整个文件的内容
print(content)  # 输出文件内容
