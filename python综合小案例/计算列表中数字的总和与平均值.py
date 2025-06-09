# 定义一个包含数字的列表 (list: 列表)
numbers = [10, 20, 30, 40, 50]  # numbers 表示数字们，列表里的数字可以随意更改

# 计算数字的总和 (sum: 总和)
total_sum = sum(numbers)  # sum 是 Python 内置函数，用来计算所有数字的总和
# total_sum 变量表示列表中数字的总和

# 计算数字的个数 (len: 长度、数量)
count = len(numbers)  # len 是 Python 内置函数，用来计算列表中元素的个数
# count 变量表示列表中的数字有多少个

# 计算平均值 (average: 平均值)
average = total_sum / count  # 使用总和除以数字个数，得到平均值
# average 变量表示列表中数字的平均值

# 打印结果 (print: 打印)
print(f"数字总和是：{total_sum}")  # f-string 格式化字符串，{total_sum} 是变量插值
# 输出数字总和
print(f"数字平均值是：{average}")  # 输出数字平均值
