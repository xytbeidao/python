class Student:
    # 定义一个学生类，名字叫 Student，用来表示一个学生对象

    def __init__(self, name, age, address):
        # 构造方法，当创建 Student 对象时会自动调用
        # 参数 name 表示学生姓名，age 表示年龄，address 表示地址
        self.name = name
        # 将传进来的 name 参数赋值给对象自己的 name 属性
        self.age = age
        # 将传进来的 age 参数赋值给对象自己的 age 属性
        self.address = address
        # 将传进来的 address 参数赋值给对象自己的 address 属性

    def show_info(self):
        # 定义一个方法，叫 show_info，用来打印当前学生的详细信息
        print(f"【学生姓名：{self.name}，年龄：{self.age}，地址：{self.address}】")
        # 使用格式化字符串 f"..." 打印学生信息，花括号内是变量
students = []
# 创建一个空列表，名字叫 students，用来存放多个学生对象
for i in range(3):
    # 循环3次（可以改成10次），每次代表录入一位学生

    print(f"\n当前录入第{i + 1}位学生信息，总共需要录入3位学生信息")
    # 打印提示信息，告诉用户正在录入第几位学生

    name = input("请输入学生姓名：")
    # 用 input() 获取用户输入的姓名，保存到变量 name 中

    age = input("请输入学生年龄：")
    # 获取输入的年龄（默认是字符串），保存到变量 age 中

    address = input("请输入学生地址：")
    # 获取输入的地址，保存到变量 address 中

    student = Student(name, age, address)
    # 使用刚才输入的3个信息创建一个 Student 对象

    students.append(student)
    # 把这个学生对象添加到 students 列表中保存起来

    print(f"学生{i + 1}信息录入完成，信息为：", end="")
    # 打印提示信息，end="" 表示后面不换行

    student.show_info()
    # 调用这个学生对象的 show_info() 方法，打印它的信息
    print("\n所有学生信息如下：")
    # 换行并打印标题，准备显示所有学生的信息

    for student in students:
        # 遍历 students 列表中的每一个学生对象

        student.show_info()
        # 调用每一个学生对象的 show_info() 方法，打印详细信息