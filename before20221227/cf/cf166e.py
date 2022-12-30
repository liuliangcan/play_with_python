import os
import sys

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 10 ** 9 + 7


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
