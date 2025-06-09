def climb_stairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    # 使用动态规划求解
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # 每一步可以从 i-1 或 i-2 来
    return dp[n]

# 测试
stairs = 10
print(f"爬到 {stairs} 级楼梯一共有 {climb_stairs(stairs)} 种方法")
