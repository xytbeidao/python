# 捕获除零错误 (try-except: 异常捕获)
try:
    result = 10 / 0  # 试图除以零，会引发 ZeroDivisionError
except ZeroDivisionError as e:  # 捕获异常
    print(f"发生了错误: {e}")  # 输出错误信息
finally:
    print("无论是否发生错误，这段代码都会执行。")
