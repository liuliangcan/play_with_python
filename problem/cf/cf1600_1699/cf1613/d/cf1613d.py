# Problem: D. MEX Sequences
# Contest: Codeforces - Educational Codeforces Round 118 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1613/D
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

# MOD = 10**9 + 7
MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1613/D

输入 T(≤1e5) 表示 T 组数据。所有数据的 n 之和 ≤5e5。
每组数据输入 n(1≤n≤5e5) 和长为 n 的数组 a(0≤a[i]≤n)。

称序列 b 为 MEX 序列，如果对所有 i 都有 abs(b[i] - mex(b[0],...,b[i])) ≤ 1 成立，其中 mex(S) 表示不在 S 中的最小非负整数。
输出 a 的非空 MEX 子序列的个数，模 998244353。
两个子序列只要有元素下标不同，就算不同的子序列。例如 a=[0,0,0] 有 7 个不同的非空子序列。
注：子序列不要求连续。
输入
4
3
0 2 1
2
1 0
5
0 0 0 0 0
4
0 1 2 3
输出
4
2
31
7
"""

"""
定义:f[i][0/1][j] 表示 用前i个数，mex为j时，且数列里[不含/含有] 超过mex的数字的情况数. (实际上[含有]时，这个数只能是mex+1，即0123^5)
初始:f[i][0][0]=1
转移:转移到a[i]时，设  v=a[i]
    那么v只能转移到mex为v-1,v(不可能),v+1的地方，它们的转移来源是：
    f[i-1][0/1][v-1]-> f[i][1][v-1]  # 即原来是012/0124 添加一个4，mex不变，依然是v-1=3
    f[i-1][0][v]    -> f[i][0][v+1]  # 即原来是0123 添加一个4, mex=v+1
    f[i-1][0/1][v+1]-> f[i][0/1][v+1]  # 即原来是01234/012346 添加一个4, mex不变，依然是v+1=5
答案:sum(f[-1])-1  ,注意删除空集
实现时第一层省去，由于j只会从更小的转移，因此优先处理v+1，用一个数组搞定
"""

"""灵神的题解
提示 1：MEX 序列的第一个数可以是哪些？第二个数呢？第三个数呢？

提示 2：把状态机画出来，照着写一个状态机 DP。

提示 3：
定义 f[i] 表示形如 00...011...122...2 ... ii...i 的非空子序列个数。
例如 f[3] 包含 0111233。
那么有 f[0] = f[0] * 2 + 1，表示要么不选这个 0，要么和前面的 0 拼起来，要么单独成一个 0。
同理有 f[i] = f[i] * 2 + f[i-1]。

定义 g2[i]，表示形如 00...011...122...2 ... (i-2)... i... (i-2)... i... (i-2)... i... 的非空子序列个数。
例如 g2[3] 包含 000113313113。
定义 l2[i]，表示形如 00...011...122...2 ... (i+2)... i... (i+2)... i... (i+2)... i... 的非空子序列个数。
例如 l2[1] 包含 000113313331。

那么有 
g2[i] = g2[i] * 2 + l2[i-2] + f[i-2]，
l2[i] = l2[i] * 2 + g2[i+2]。

最后还有一种情况，就是 11..1 这样的也算 MEX 序列。
定义 f1 表示它的个数，那么有
f1 = f1 * 2 + 1。

最后答案为 f1 + sum(f) + sum(g2) + sum(l2)。

https://codeforces.com/problemset/submission/1613/214488015"""


#  280   ms
def solve1():
    n, = RI()
    a = RILST()
    f = [[0] * (n + 2) for _ in range(2)]
    f[0][0] = 1
    for v in a:
        f[0][v + 1] = f[0][v + 1] * 2 % MOD
        f[1][v + 1] = f[1][v + 1] * 2 % MOD
        f[0][v + 1] = (f[0][v + 1] + f[0][v]) % MOD
        if v:
            f[1][v - 1] = (f[1][v - 1] + f[0][v - 1] + f[1][v - 1]) % MOD
    print((sum(f[0]) + sum(f[1]) - 1) % MOD)


#  187   ms
def solve():
    n, = RI()
    a = RILST()
    f0 = [0] * (n + 2)
    f1 = [0] * (n + 2)
    f0[0] = 1
    for v in a:
        f0[v + 1] = (f0[v + 1] * 2 + f0[v]) % MOD
        f1[v + 1] = f1[v + 1] * 2 % MOD
        if v:
            f1[v - 1] = (f1[v - 1] + f0[v - 1] + f1[v - 1]) % MOD
    print((sum(f0) + sum(f1) - 1) % MOD)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
