import os
import sys

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 998244353


def solve(n, k):
    if k == 1 or k == 2*n:
        return print(2)

    dp = [[0] * 2 for _ in range(k + 1)]  # 前i列，组成j个连通块，第i列情况是0、1的方法数
    # 0:白白和黑黑 1:白黑和黑白
    dp[1][0] = 2  # 第一列1色方案只有黑黑和白白，
    dp[2][1] = 2  # 第一列2色方案只有白黑和黑白
    t = [a[:] for a in dp]
    x = [dp, t]  # 滚动数组
    for i in range(2, n + 1):
        c, l = x[i & 1], x[(i + 1) & 1]
        for j in range(2, min(k + 1, 2 * i + 1)):
            c[j][0] = (l[j - 1][0] + l[j][0] + l[j][1] * 2) % MOD
            c[j][1] = (l[j - 2][1] + l[j][1] + l[j - 1][0] * 2) % MOD

    print(sum(x[n & 1][k]) % MOD)



# def solve2(n, k):
#     if k == 1:
#         return print(2)
#     if k == 2 * n:
#         return print(2)
#
#     dp = [[0] * 2 for _ in range(k + 1)]  # 前i列，组成j个连通块，第i列情况是0、1的方法数
#     # 0:白白和黑黑 1:白黑和黑白
#     dp[1][0] = 2
#     dp[2][1] = 2
#     for i in range(2, n + 1):
#         for j in range(min(k, 2 * i), 1, -1):
#             dp[j][0] = (dp[j - 1][0] + dp[j][0] + dp[j][1] * 2) % MOD
#             dp[j][1] = (dp[j - 2][1] + dp[j][1] + dp[j - 1][0] * 2) % MOD
#
#     print(sum(dp[k]) % MOD)


if __name__ == '__main__':
    n, k = map(int, input().split())
    solve(n, k)
