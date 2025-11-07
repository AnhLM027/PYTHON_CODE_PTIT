
t = int(input())
for _ in range(t):
    n = int(input())
    X, Y, Z = map(int, input().split())

    dp = [0] * (n + 2)
    dp[0] = 0
    dp[1] = X

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + X
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + Z)
        else:
            dp[i] = min(dp[i], dp[(i + 1) // 2] + Z + Y)

    print(dp[n])
