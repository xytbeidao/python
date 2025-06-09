text = "这是一辆无人车，无人车正在进行测试，无人车通过了障碍物"  # 定义一个字符串，内容就是你要分析的文本

word_to_count = "无人车"  # 我们要统计这个词出现了几次

count = text.count(word_to_count)  # 使用字符串的内置函数 count() 统计该词在字符串中出现的次数

print("‘" + word_to_count + "’ 出现了", count, "次")  # 打印结果，告诉我们出现了多少次
