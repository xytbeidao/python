numbers = [8, 3, 15, 6, 12]  # 一个数字列表
max_num = numbers[0]         # 假设第一个是最大

for num in numbers:          # 遍历每个数字
    if num > max_num:        # 如果当前数字比之前的最大还大
        max_num = num        # 更新最大值

print("最大值是：", max_num)  # 输出最大值
