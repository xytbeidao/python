class Vector:                              # class 定义一个类；Vector 是类的名称，代表向量
    def __init__(self, x, y):              # def 定义函数；__init__ 是构造方法，创建对象时自动调用
        self.x = x                         # self.x 是当前对象的 x 属性，= 表示赋值；把参数 x 存进去
        self.y = y                         # self.y 是当前对象的 y 属性，把参数 y 存进去

    def __add__(self, other):              # 定义 + 运算的行为；当你写 v1 + v2 时会自动调用这个方法
        return Vector(self.x + other.x,    # self.x + other.x 表示两个向量的 x 分量相加
                      self.y + other.y)    # self.y + other.y 表示两个向量的 y 分量相加

    def __str__(self):                     # 定义 print(v1) 的输出格式
        return f"({self.x}, {self.y})"     # f"..." 是格式化字符串，插入变量值，返回 (x, y) 形式

# 下面是使用这个类的实际例子：

v1 = Vector(3, 4)                          # 创建一个向量对象 v1，x=3, y=4
v2 = Vector(1, 2)                          # 创建另一个向量对象 v2，x=1, y=2

v3 = v1 + v2                               # 实际执行 v1.__add__(v2)，返回 Vector(4, 6)

print(v3)                                  # 实际调用 v3.__str__()，打印结果为：(4, 6)