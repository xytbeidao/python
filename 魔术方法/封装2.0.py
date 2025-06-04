class Student:
    def __init__(self,name,score):
        self.name = name
        self.__score =score #封装
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0<= score<=100:
            self.__score =score
        else:
            raise ValueError("成绩报错")

    def display(self):
        print(f"student:{self.name},成绩{self.__score}")

stu = Student("小明", 85)                      # 创建 Student 的实例，传入姓名 "小明" 和成绩 85

print(stu.name)                                # 访问公有属性 name，打印 "小明"
# print(stu.__score)                           # 这行如果取消注释会报错：AttributeError，外部无法直接访问 __score

print(stu.get_score())                         # 通过 get_score() 方法获取私有属性 __score，打印 85

stu.set_score(95)                               # 通过 set_score() 方法修改私有属性 __score 为 95
print(stu.get_score())                         # 再次获取，确认成绩变成 95

# stu.set_score(150)                           # 如果取消注释，这里会因为 150 超出 0-100 范围而抛出 ValueError

stu.display()                                   # 调用 display() 方法，打印 “学生：小明，成绩：95”