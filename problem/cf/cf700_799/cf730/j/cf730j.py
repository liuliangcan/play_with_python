# Problem: J. Bottles
# Contest: Codeforces - 2016-2017 ACM-ICPC, NEERC, Southern Subregional Contest (Online Mirror, ACM-ICPC Rules, Teams Preferred)
# URL: https://codeforces.com/problemset/problem/730/J
# Memory Limit: 512 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/730/J

输入 n(1≤n≤100) 和两个长为 n 的数组 a b (1≤a[i]≤b[i]≤100)。

有 n 个水桶，第 i 个水桶装了 a[i] 单位的水，水桶容量为 b[i]。
花费 1 秒，可以从某个水桶中，转移 1 个单位的水，到另一个水桶。

输出两个数：
把水汇集起来，最少需要多少个桶（换句话说需要倒空尽量多的桶），该情况下至少要多少秒完成？
输入
4
3 3 4 3
4 7 6 5
输出 2 6

输入
2
1 1
100 100
输出 1 1

输入
5
10 30 5 6 24
10 41 7 8 24
输出 3 11
"""
"""二维背包
显然最少桶可以先贪心算出来，设为m；设总水量为sa
那么问题变成选恰好m个桶，总容量超过sa时，能装的最多的水是多少。那么答案就是sa-v
设f[i][j][k]为从前i个桶里选j个桶，且容量恰好为k时的最多水。
那么f[i][j][k] = max(f[i-1][j][k],f[i-1][j-1][k-b[i]+a[i])
复杂度n^4
"""
"""存在3次方做法：
设dp[i][j]=(x,y)为从前i个桶里选，且容量为j时，能取到的最少桶数和最多水量
那么对于第i个桶：
    若不选它，dp[i][j]=dp[i-1][j]
    若选它: 先找到dp[i-1][j-b[i]] 这代表上一层里，对应体积的 最少桶数q和最多水量t
        dp[i][j] = q+1,t+a[i]
# https://codeforces.com/contest/730/submission/148088697
n=int(input())
dp=[[(-10**9,-10**9) for i in range(10001)]for j in range(101)]
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=(10**9,10**9)
dp[0][0]=(0,0)
tot=sum(a)
full=sum(b)
for i in range(1,n+1):
    for j in range(full+1):
        dp[i][j]=dp[i-1][j]
        if j>=b[i-1]:
            q,t=dp[i-1][j-b[i-1]]
            dp[i][j]=max(dp[i][j],(q-1,t+a[i-1]))
        if j>=tot and dp[i][j][0]>-10**9:
            q,t=dp[i][j]
            ans=min(ans,(-q,tot-t))
print(*ans)
"""


# 124 ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    sa = sum(a)

    sb = m = 0
    for i, v in enumerate(sorted(b, reverse=True), start=1):
        sb += v
        if sb >= sa:
            m = i
            break
    if m == n:
        return print(f'{m} 0')
    sb = sum(b)
    # dp[i][j]=(x,y)为从前i个桶里选，且容量为j时，能取到的最少桶数和最多水量。
    # 实现时把x取反，便于直接max
    inf = 10 ** 9
    f = [(-inf, -inf) for _ in range(sb + 1)]
    f[0] = (0, 0)
    ans = (inf, inf)
    for x, y in zip(a, b):
        for j in range(sb, y - 1, -1):  # 容量y
            q, t = f[j - y]
            f[j] = max(f[j], (q - 1, t + x))
            if j >= sa:
                q, t = f[j]
                ans = min(ans, (-q, sa - t))
    print(f'{ans[0]} {ans[1]}')


#  体积至少 刷表n^4 966    ms
def solve4():
    n, = RI()
    a = RILST()
    b = RILST()
    sa = sum(a)

    sb = m = 0
    for i, v in enumerate(sorted(b, reverse=True), start=1):
        sb += v
        if sb >= sa:
            m = i
            break
    if m == n:
        return print(m, 0)
    # sb = sum(b)
    f = [[-inf] * (sa + 1) for _ in range(m + 1)]  # f[i][j][k] 为用前i个桶，恰好选j个桶不动，桶的总体积为k时，这些桶最多的水
    f[0][0] = 0
    for x, y in zip(a, b):
        for k in range(sa, -1, -1):  # 容量y
            z = k + y if k + y < sa else sa
            for j in range(m):  # 1个桶
                if f[j][k] + x > f[j + 1][z]:
                    f[j + 1][z] = f[j][k] + x
    print(m, sa - f[-1][-1])


#  体积至少 刷表n^4 777    ms
def solve3():
    n, = RI()
    a = RILST()
    b = RILST()
    sa = sum(a)

    sb = m = 0
    for i, v in enumerate(sorted(b, reverse=True), start=1):
        sb += v
        if sb >= sa:
            m = i
            break
    if m == n:
        return print(m, 0)
    # sb = sum(b)
    f = [[-inf] * (sa + 1) for _ in range(m + 1)]  # f[i][j][k] 为用前i个桶，恰好选j个桶不动，桶的总体积为k时，这些桶最多的水
    f[0][0] = 0
    for x, y in zip(a, b):
        for j in range(m - 1, -1, -1):  # 1个桶
            for k in range(sa, -1, -1):  # 容量y
                z = k + y if k + y < sa else sa
                if f[j][k] + x > f[j + 1][z]:
                    f[j + 1][z] = f[j][k] + x
                # f[j + 1][z] = max(f[j + 1][z], f[j][k] + x)  # 水多x
    print(m, sa - f[-1][-1])


#  刷表n^4 919    ms
def solve2():
    n, = RI()
    a = RILST()
    b = RILST()
    sa = sum(a)

    p = m = 0
    for i, v in enumerate(sorted(b, reverse=True), start=1):
        p += v
        if p >= sa:
            m = i
            break
    if m == n:
        return print(m, 0)
    sb = sum(b)
    f = [[-inf] * (sb + 1) for _ in range(m + 1)]  # f[i][j][k] 为用前i个桶，恰好选j个桶不动，桶的总体积为k时，这些桶最多的水
    f[0][0] = 0
    for x, y in zip(a, b):
        for j in range(m - 1, -1, -1):  # 1个桶
            for k in range(sb - y, -1, -1):  # 容量y
                f[j + 1][k + y] = max(f[j + 1][k + y], f[j][k] + x)  # 水多x
    print(m, sa - max(f[-1][sa:]))


#  填表n^4  967   ms
def solve1():
    n, = RI()
    a = RILST()
    b = RILST()
    sa = sum(a)

    p = m = 0
    for i, v in enumerate(sorted(b, reverse=True), start=1):
        p += v
        if p >= sa:
            m = i
            break
    if m == n:
        return print(m, 0)
    sb = sum(b)
    f = [[-inf] * (sb + 1) for _ in range(m + 1)]  # f[i][j][k] 为用前i个桶，恰好选j个桶不动，桶的总体积为k时，这些桶最多的水
    f[0][0] = 0
    for x, y in zip(a, b):
        for j in range(m, 0, -1):  # 1个桶
            for k in range(sb, y - 1, -1):  # 容量y
                f[j][k] = max(f[j][k], f[j - 1][k - y] + x)  # 水多x
    print(m, sa - max(f[-1][sa:]))


if __name__ == '__main__':
    n, = RI()
    a = RILST()
    b = RILST()
    sa = sum(a)

    # sb = m = 0
    # for i, v in enumerate(sorted(b, reverse=True), start=1):
    #     sb += v
    #     if sb >= sa:
    #         m = i
    #         break
    # if m == n:
    #     print(m, 0)
    #     exit()
    # sb = sum(b)
    # dp[i][j]=(x,y)为从前i个桶里选，且容量为j时，能取到的最少桶数和最多水量。
    # 实现时把x取反，便于直接max
    inf = 10 ** 9
    f = [(-inf, -inf) for _ in range(sa + 1)]
    f[0] = (0, 0)
    ans = (inf, inf)
    for x, y in zip(a, b):
        for j in range(sa, -1, -1):  # 容量y
            q, t = f[j]
            z = sa if sa < j + y else j + y
            if (q - 1, t + x) > f[z]:
                f[z] = (q - 1, t + x)
    print(-f[-1][0], sa - f[-1][1])  # 93
