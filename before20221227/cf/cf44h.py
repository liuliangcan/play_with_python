import os
import sys
from math import floor, ceil

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 998244353


# def solve(s):
#     s = list(map(int, s))
#     n = len(s)
#     dp = [[0] * 10 for _ in range(n)]
#     dp[0] = [1] * 10
#     flag = True
#     for i in range(n - 1):
#         t = (s[i] + s[i + 1]) / 2
#         if s[i + 1] != ceil(t) and s[i + 1] != floor(t):
#             flag = False
#         for j in range(10):
#             a, b = divmod(j + s[i + 1], 2)
#             dp[i + 1][a] += dp[i][j]
#             if b == 1:
#                 dp[i + 1][a + 1] += dp[i][j]
#
#     print(sum(dp[-1]) - flag)
def solve(s):
    s = list(map(int, s))
    n = len(s)
    dp = [1] * 10
    for i in range(n - 1):
        g = [0] * 10
        for j in range(10):
            a, b = divmod(j + s[i + 1], 2)
            g[a] += dp[j]
            if b == 1:
                g[a + 1] += dp[j]
        dp = g
    print(sum(dp) - all(abs(s[i + 1] - s[i]) <= 1 for i in range(n - 1)))


if __name__ == '__main__':
    s = input()
    solve(s)
