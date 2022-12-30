import os
import sys


if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 10 ** 9 + 7


def solve(n, h):
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = min(dp[i - 1] + 1, h[i])
    dp[-1] = 1
    for i in range(n - 2, -1, -1):
        dp[i] = min(dp[i + 1] + 1, dp[i])
    print(max(dp))


if __name__ == '__main__':
    n =int(input())
    h = list(map(int, input().split()))
    # print(n,d,h)
    solve(n, h)
