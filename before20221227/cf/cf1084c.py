import os
import sys

if os.getenv('LOCALCFTEST'):
    sys.stdin = open('cfinput.txt')
MOD = 10 ** 9 + 7

if __name__ == '__main__':
    s = input()
    # 令dp[i]为以s[i]为结尾的合法子序列数量
    # 显然，第一个a处,dp[i] = 1
    # 在i后，下一个a处，设为k，如果k和i中间无b，那么，只能用k来替换i，来组合出合法序列，dp[k]=dp[i];否则，可以和前边所有case组合，再加上自己单独，dp[k]=sum(pre)+1。
    dp = 0
    ans = 0
    b = False
    start = True
    for c in s:
        if c == 'b':
            if not b:
                b = True
            continue
        if c == 'a':
            if start:
                start = False
                dp = 1
                b = False
            else :
                if b:
                    dp = (ans+1) % MOD
                    b = False

            ans = (ans + dp) % MOD

    print(ans)
