# 定义一个字符串
text = "Python is awesome and Python is easy to learn."

# 查找子字符串出现的次数 (count: 计数)
count_python = text.count("Python")  # count() 统计 "Python" 在字符串中出现的次数
print(f"'Python' 出现了 {count_python} 次。")

# 替换子字符串 (replace: 替换)
replaced_text = text.replace("Python", "Programming")  # 把 "Python" 替换成 "Programming"
print(replaced_text)

# 分割字符串 (split: 分割)
words = text.split(" ")  # 按空格分割字符串为一个列表
print(words)

# 检查字符串是否以特定子字符串开头 (startswith: 开头)
is_start_with_python = text.startswith("Python")  # 判断是否以 "Python" 开头
print(f"字符串是否以 'Python' 开头: {is_start_with_python}")
