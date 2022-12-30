import os
import sys

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 998244353

def solve(n,k):
    if k == 1:
        return print(2)


    dp = [[[0] * 4 for _ in range(k + 1)] for _ in range(n + 1)]  # 前i列，组成j个连通块，第i列情况是0123的方法数
    # 0:白白 1:白黑 2:黑白 3:黑黑
    dp[1][1][0] = 1
    dp[1][1][3] = 1
    dp[1][2][1] = 1
    dp[1][2][2] = 1
    for i in range(2, n + 1):
        for j in range(1, min(k+1, 2 * i + 1)):
            dp[i][j][0] = dp[i - 1][j - 1][3] + dp[i - 1][j][0] + dp[i - 1][j][1] + dp[i - 1][j][2]
            dp[i][j][3] = dp[i - 1][j - 1][0] + dp[i - 1][j][3] + dp[i - 1][j][1] + dp[i - 1][j][2]
            dp[i][j][1] = dp[i - 1][j - 1][2] + dp[i - 1][j][3] + dp[i - 1][j][1] + dp[i - 1][j][0]
            dp[i][j][2] = dp[i - 1][j - 1][1] + dp[i - 1][j][3] + dp[i - 1][j][2] + dp[i - 1][j][0]
            print(i,j,dp[i][j])

    print(sum(dp[n][k]) % MOD)
if __name__ == '__main__':
    n, k = map(int, input().split())
    solve(n,k)
