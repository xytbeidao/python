from collections import Counter

# 输入文本
text = """
人工智能是计算机科学的一个分支，目的是让机器模拟人类的学习、推理、解决问题的能力。
如今，人工智能已广泛应用于各个领域，如医疗、教育、金融、自动驾驶等。
"""

# 1. 文本预处理（去掉标点符号，按空格分词）
words = text.replace("，", " ").replace("。", " ").replace("、", " ").split()

# 2. 统计词频
word_counts = Counter(words)

# 3. 找出频率最高的 5 个词
top_5_words = word_counts.most_common(5)

# 输出结果
print("出现频率最高的词：")
for word, count in top_5_words:
    print(f"{word}：{count} 次")
