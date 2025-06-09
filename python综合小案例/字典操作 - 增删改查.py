# 创建一个字典 (dictionary: 字典)
student = {"name": "Alice", "age": 25, "grade": "A"}  # 键值对的集合，键用来标识，值存储数据

# 访问字典的值 (get: 获取)
name = student.get("name")  # get() 方法获取键对应的值
print(f"学生的名字是: {name}")

# 更新字典 (update: 更新)
student.update({"age": 26, "major": "Computer Science"})  # update() 更新字典中的键值对
print(student)

# 添加新的键值对
student["school"] = "XYZ University"  # 直接赋值添加新键
print(student)

# 删除键值对 (pop: 删除)
student.pop("grade")  # 删除键为 "grade" 的项
print(student)
