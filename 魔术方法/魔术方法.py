#-init- and -del-  对象的创建与销毁
class Person:                        # class 定义一个类，Person 是类名
    def __init__(self, name):        # def 定义方法，__init__ 是构造函数，在创建对象时自动调用；self 是实例对象；name 是参数
        self.name = name             # self.name 是实例变量，等于传入的参数 name，用于记录人的名字

    def __del__(self):               # __del__ 是析构函数，在对象被销毁时自动调用
        print(f"{self.name} 被销毁")  # 打印提示信息，f 是格式化字符串，{self.name} 会显示人的名字

#对象的字符串表示
class Book:                          # 定义 Book 类
    def __init__(self, title):       # 构造函数，接收书名 title
        self.title = title           # 把 title 存到对象的 title 属性中

    def __str__(self):               # __str__ 定义用户可读的字符串表现（用于 print）
        return f"《{self.title}》"     # 返回格式化字符串，显示为书名加书壳样式

    def __repr__(self):              # __repr__ 定义开发者可读的字符串表现（用于调试）
        return f"Book(title={self.title!r})"  # !r 表示用 repr 的格式打印 title

#运算符重载：让对象支持加法运算
class Vector:                        # 定义一个向量类 Vector
    def __init__(self, x, y):        # 构造函数，接收两个分量 x 和 y
        self.x = x                   # 保存 x 分量
        self.y = y                   # 保存 y 分量

    def __add__(self, other):        # 定义 + 运算符行为，other 是另一个 Vector 对象
        return Vector(self.x + other.x, self.y + other.y)  # 返回新 Vector，对应分量相加

    def __str__(self):               # 用于 print 显示向量
        return f"({self.x}, {self.y})"  # 返回格式化字符串表示坐标