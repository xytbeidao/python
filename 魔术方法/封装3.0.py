class VendingMachine:                           # 定义一个自动售货机的类
    def __init__(self):                         # 初始化售货机
        self.__drinks = {                       # 私有属性：饮料列表（不能直接访问）
            "可乐": 3,
            "雪碧": 2,
            "果汁": 5
        }

    def show_drinks(self):                      # 公有方法：展示有哪些饮料
        print("可选饮料：")
        for name, price in self.__drinks.items():
            print(f"{name} - {price} 元")

    def buy(self, name, money):                 # 公有方法：买饮料
        if name not in self.__drinks:
            print("没有这种饮料")
        elif money < self.__drinks[name]:
            print("钱不够")
        else:
            change = money - self.__drinks[name]
            print(f"购买成功，找零 {change} 元")

            machine = VendingMachine()  # 创建一个售货机

            machine.show_drinks()  # 展示饮料（用的是公有方法）

            machine.buy("可乐", 5)  # 买一瓶可乐，投5元 → 显示购买成功，找零2元

            # machine.__drinks["可乐"] = 0         # ❌ 这行访问私有属性会报错！因为封装了