class VendingMachine:                                 # 定义自动售货机类
    def __init__(self):                               # 构造函数
        self.__drinks = {                             # 私有属性：饮料名称 -> 价格
            "可乐": 3,
            "雪碧": 2,
            "果汁": 5
        }
        self.__stock = {                              # 私有属性：饮料名称 -> 库存数量
            "可乐": 5,
            "雪碧": 5,
            "果汁": 3
        }
        self.__balance = 0                            # 私有属性：用户余额，初始为 0 元

    def show_drinks(self):                            # 显示饮料列表及库存
        print("可选饮料（剩余）：")
        for name in self.__drinks:
            price = self.__drinks[name]               # 获取饮料价格
            stock = self.__stock.get(name, 0)         # 获取库存（默认 0）
            print(f"{name} - {price} 元（剩余 {stock} 瓶）")

    def recharge(self, amount):                       # 用户充值余额
        if amount > 0:                                # 金额必须大于 0
            self.__balance += amount                  # 增加余额
            print(f"充值成功，当前余额为 {self.__balance} 元")
        else:
            print("充值金额必须大于 0 元")

    def buy(self, name):                              # 买饮料，只需要指定名称，用余额购买
        if name not in self.__drinks:                 # 检查是否存在该饮料
            print("没有这种饮料")
        elif self.__stock.get(name, 0) <= 0:           # 检查库存是否为 0
            print("该饮料已售罄")
        elif self.__balance < self.__drinks[name]:     # 检查余额是否足够
            print(f"余额不足，当前余额：{self.__balance} 元")
        else:
            self.__balance -= self.__drinks[name]      # 扣除余额
            self.__stock[name] -= 1                    # 减少库存
            print(f"购买成功，剩余余额：{self.__balance} 元")

    def add_drink(self, name, price, quantity):        # 添加新饮料（老板使用）
        if name in self.__drinks:                      # 如果已经有这个饮料
            self.__stock[name] += quantity             # 增加库存
            print(f"已补货 {name}，库存增加 {quantity} 瓶")
        else:
            self.__drinks[name] = price                # 添加新饮料及价格
            self.__stock[name] = quantity              # 设置初始库存
            print(f"已添加新饮料：{name}，价格 {price} 元，库存 {quantity} 瓶")

    def show_balance(self):                            # 显示当前余额
        print(f"当前余额：{self.__balance} 元")


# 👇👇👇 以下是测试代码 👇👇👇

machine = VendingMachine()              # 创建售货机对象

machine.show_drinks()                   # 展示所有饮料和库存
machine.recharge(10)                    # 充值 10 元
machine.show_balance()                 # 显示当前余额

machine.buy("可乐")                     # 购买可乐，价格 3 元
machine.buy("雪碧")                     # 购买雪碧，价格 2 元
machine.buy("果汁")                     # 购买果汁，价格 5 元
machine.buy("果汁")                     # 余额不足时尝试再买果汁

machine.show_balance()                 # 显示剩余余额
machine.show_drinks()                  # 再次展示饮料，看看库存是否减少

machine.add_drink("奶茶", 6, 4)         # 老板添加新饮料“奶茶”
machine.show_drinks()                  # 展示新增饮料