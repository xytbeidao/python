from datetime import datetime, timedelta  # 导入日期时间模块

# 获取当前时间 (now: 现在)
now = datetime.now()  # 获取当前时间
print(f"当前时间是: {now}")

# 格式化时间 (strftime: 格式化)
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")  # 格式化为 "年-月-日 时:分:秒"
print(f"格式化时间: {formatted_time}")

# 计算时间差 (timedelta: 时间差)
future_time = now + timedelta(days=7)  # 当前时间加 7 天
print(f"未来的时间是: {future_time}")
