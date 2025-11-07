

import sys
input = sys.stdin.readline

MOD = 1000

def mat_mul(A, B):
    return [
        [(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD],
        [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD]
    ]

def mat_pow(M, e):
    res = [[1, 0], [0, 1]]
    base = M
    while e > 0:
        if e & 1:
            res = mat_mul(res, base)
        base = mat_mul(base, base)
        e >>= 1
    return res

def first3(n):
    if n == 0:
        return "001"

    M = [[6 % MOD, (-4) % MOD], [1, 0]]
    P = mat_pow(M, n-1)
    # S1 = 6, S0 = 2
    Sn_mod = (P[0][0] * 6 + P[0][1] * 2) % MOD
    x = (Sn_mod - 1) % MOD
    return f"{x:03d}"

def main():
    t = int(input().strip())
    for i in range(1, t+1):
        n = int(input().strip())
        ans = first3(n)
        print(f"Case #{i}: {ans}")

if __name__ == "__main__":
    main()
