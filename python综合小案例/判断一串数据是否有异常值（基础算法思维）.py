speeds = [30, 32, 35, 33, 31, 45, 30, 29, 50, 32]  # 模拟的10秒速度记录

for i in range(1, len(speeds)):  # 从第二个数据开始遍历（因为要和前一个对比）
    diff = abs(speeds[i] - speeds[i - 1])  # 计算当前值与前一个值的差值
    if diff > 10:  # 如果差值超过10
        print(f"第{i+1}秒出现异常！速度跳变为 {speeds[i]} km/h（与上一秒差 {diff}）")
