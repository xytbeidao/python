# 创建一个列表 (list: 列表)
numbers = [10, 5, 8, 12, 3]

# 排序 (sort: 排序)
numbers.sort()  # sort() 方法对列表进行原地排序（从小到大）
print(f"排序后的列表: {numbers}")

# 反转排序 (reverse: 反转)
numbers.reverse()  # reverse() 方法将列表顺序反转
print(f"反转排序后的列表: {numbers}")

# 使用列表推导式 (list comprehension: 列表推导式)
squared = [x**2 for x in numbers]  # 对每个元素求平方
print(f"平方列表: {squared}")

# 使用 filter() 函数过滤 (filter: 过滤)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # 过滤偶数
print(f"偶数列表: {even_numbers}")
