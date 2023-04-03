import os
import sys

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('../../../../../before20221227/cf/cfinput.txt')
MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/166/E

输入正整数 n(n<=1e7)。
一只蚂蚁站在一个四面体的某个顶点 D 上，沿着四面体的棱行走。
输出它走了恰好 n 条棱后，又重新回到顶点 D 的路径数，模 1e9+7 的结果。
路径中间可以经过 D。"""

if __name__ == '__main__':
    n = int(input())
    dp = [0, 0, 0, 1]

    for i in range(1, n + 1):
        s = sum(dp) % MOD
        dp[0] = s - dp[0]
        dp[1] = s - dp[1]
        dp[2] = s - dp[2]
        dp[3] = s - dp[3]
    print(dp[3] % MOD)
