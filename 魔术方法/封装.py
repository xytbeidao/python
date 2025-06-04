class Student:
    def __init__(self, name, score):         # 构造函数，传入姓名和成绩
        self.name = name                     # 公有属性 name
        self.__score = score                 # 私有属性 __score（使用双下划线封装）

    def get_score(self):                     # 公有方法，用于获取私有属性
        return self.__score

    def set_score(self, score):              # 公有方法，用于设置私有属性
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("成绩必须在 0 到 100 之间")

    def display(self):                       # 显示信息的方法
        print(f"学生：{self.name}，成绩：{self.__score}")


# ----------------- 测试部分 -----------------

stu = Student("小明", 85)                      # 创建 Student 的实例，传入姓名 "小明" 和成绩 85

print(stu.name)                                # 访问公有属性 name，打印 "小明"
# print(stu.__score)                           # 这行如果取消注释会报错：AttributeError，外部无法直接访问 __score

print(stu.get_score())                         # 通过 get_score() 方法获取私有属性 __score，打印 85

stu.set_score(95)                               # 通过 set_score() 方法修改私有属性 __score 为 95
print(stu.get_score())                         # 再次获取，确认成绩变成 95

# stu.set_score(150)                           # 如果取消注释，这里会因为 150 超出 0-100 范围而抛出 ValueError

stu.display()                                   # 调用 display() 方法，打印 “学生：小明，成绩：95”