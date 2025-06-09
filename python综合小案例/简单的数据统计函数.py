def average_speed(speeds):  # 定义一个函数，接收一个速度列表
    total = sum(speeds)  # 用 sum() 计算所有速度的总和
    count = len(speeds)  # 用 len() 计算一共有多少个数据
    avg = total / count  # 平均值 = 总和 / 个数
    return avg  # 返回平均值

speeds = [30, 32, 35, 33, 31]  # 模拟一段时间内的无人车速度数据

avg = average_speed(speeds)  # 调用我们定义的函数，得到平均速度

print(f"平均速度是：{avg:.2f} km/h")  # 打印保留两位小数的平均速度
