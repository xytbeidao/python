# 1. 提示用户输入一组数字 (input: 输入)
user_input = input("请输入一组数字，用空格分隔：")  # input() 函数让用户输入数据，返回字符串
# user_input 变量存储用户输入的字符串，例如 "10 20 30 40 50"

# 2. 把输入的字符串转换成数字列表 (split: 分割, map: 映射)
numbers = list(map(int, user_input.split()))
# split() 方法把字符串按空格分割成一个列表，例如 "10 20" -> ["10", "20"]
# map(int, ...) 把每个字符串转换为整数
# list(...) 把 map 的结果变成列表，例如 ["10", "20"] -> [10, 20]

# 3. 计算总和和平均值
total_sum = sum(numbers)  # 计算总和，sum() 函数把列表中的数字相加
count = len(numbers)      # 计算数字个数，len() 函数返回列表中元素数量
average = total_sum / count  # 计算平均值，总和除以数字个数

# 4. 打印结果
print(f"数字总和是：{total_sum}")  # 输出总和，{total_sum} 插入变量值
print(f"数字平均值是：{average}")  # 输出平均值，{average} 插入变量值
