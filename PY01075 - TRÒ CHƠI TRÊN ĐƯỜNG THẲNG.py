import sys
from math import gcd

input_data = sys.stdin.read().strip().split()
it = iter(input_data)

for _ in range(int(next(it))):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    c = [int(next(it)) for _ in range(n)]
    
    dp = {0: 0}
    for ai, ci in zip(a, c):
        for g, cost in list(dp.items()):
            g2 = gcd(g, ai)
            newcost = cost + ci
            if g2 not in dp or dp[g2] > newcost:
                dp[g2] = newcost
                
    ans = dp.get(1, -1)
    print(ans)