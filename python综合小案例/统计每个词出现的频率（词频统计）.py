text = "无人车 遇到 障碍物 避障 成功 无人车 避障 无人车 成功"  # 一段简单文本

words = text.split()  # 用空格分割字符串，得到词的列表：['无人车', '遇到', '障碍物', ...]

word_freq = {}  # 创建一个空字典，用来存储词频

for word in words:  # 遍历每一个词
    if word in word_freq:  # 如果这个词已经在字典里
        word_freq[word] += 1  # 对应的计数加1
    else:
        word_freq[word] = 1  # 如果第一次出现，就赋值为1

print("词频统计结果：")
for w, c in word_freq.items():  # 遍历字典，w是词，c是次数
    print(f"{w}：{c}次")
