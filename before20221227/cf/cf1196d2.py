import io
import os
import sys
from itertools import product
from math import inf

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
else:
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    input = sys.stdin.readline
MOD = 10 ** 9 + 7


# def solve(n, k, s):
#     if k == 1:
#         return 0
#     trans = {'R': 0, 'G': 1, 'B': 2}
#     s = list(map(trans.get, s))
#     # print(s)
#     dp = [[0] * 3 for _ in range(n - k + 1)]  # 把s[i:i+k]修改为以R、G、B开头的的合法子串的最小修改次数
#     # 0 1 2:R G B
#     for i in range(k):
#         if s[i] != i % 3:
#             dp[0][0] += 1
#         if s[i] != (i + 1) % 3:
#             dp[0][1] += 1
#         if s[i] != (i + 2) % 3:
#             dp[0][2] += 1
#     # print(dp)
#     for i in range(k, n):
#         dp[i - k + 1][0] = dp[i - k][2]
#         dp[i - k + 1][1] = dp[i - k][0]
#         dp[i - k + 1][2] = dp[i - k][1]
#         l = s[i - k]
#         # print(i,l)
#         # print(dp[i - k + 1])
#         dp[i - k + 1][0] -= l != 2
#         dp[i - k + 1][1] -= l != 0
#         dp[i - k + 1][2] -= l != 1
#         # print(dp[i - k + 1],l )
#         # 如果头i-k+1 是0，那么需求s[i]应该是k%3;即s[i]=(s[i-k+1]+k-1)%3
#
#         dp[i - k + 1][0] += (s[i] != (0 + k-1) % 3)
#         dp[i - k + 1][1] += (s[i] != (1 + k-1) % 3)
#         dp[i - k + 1][2] += (s[i] != (2 + k-1) % 3)
#     print(dp)
#     ans = inf
#     for i, j in product(range(n - k + 1), range(3)):
#         ans = min(ans, dp[i][j])
#     return ans
#     """
#     0120
#     """

def solve(n, k, s):
    if k == 1:
        return 0
    trans = {'R': 0, 'G': 1, 'B': 2}
    s = list(map(trans.get, s))
    # print(s)
    dp = [0] * 3  # 把s[i:i+k]修改为以R、G、B开头的的合法子串的最小修改次数
    # 0 1 2:R G B
    for i in range(k):
        if s[i] != i % 3:
            dp[0] += 1
        if s[i] != (i + 1) % 3:
            dp[1] += 1
        if s[i] != (i + 2) % 3:
            dp[2] += 1
    # print(dp)
    ans = min(dp)
    for i in range(k, n):
        a, b, c = dp[2], dp[0], dp[1]
        dp[0], dp[1], dp[2] = a, b, c
        l = s[i - k]
        dp[0] -= l != 2
        dp[1] -= l != 0
        dp[2] -= l != 1
        # print(dp[i - k + 1],l )
        # 如果头i-k+1 是0，那么需求s[i]应该是k%3;即s[i]=(s[i-k+1]+k-1)%3
        dp[0] += (s[i] != (0 + k - 1) % 3)
        dp[1] += (s[i] != (1 + k - 1) % 3)
        dp[2] += (s[i] != (2 + k - 1) % 3)
        ans = min(ans, min(dp))

    return ans


if __name__ == '__main__':
    t = int(input())
    # print(t)
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        # print(n, k, s)
        print(solve(n, k, s))
