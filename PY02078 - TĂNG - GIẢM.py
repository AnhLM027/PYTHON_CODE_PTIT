
t = int(input())
for _ in range(t):
    n = int(input())
    A, B = [], []
    for _ in range(n):
        x, y = map(float, input().split())
        A.append(x)
        B.append(y)

    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i] and B[j] > B[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
