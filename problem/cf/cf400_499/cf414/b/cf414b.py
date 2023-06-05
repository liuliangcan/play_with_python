# Problem: B. Mashmokh and ACM
# Contest: Codeforces - Codeforces Round 240 (Div. 1)
# URL: https://codeforces.com/contest/414/problem/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/414/problem/B

输入 u n(1≤u,n≤2000)。
输出有多少个长为 n 的数组 a，满足：
1. 1≤a[1]≤a[2]≤...≤a[n]≤u。
2. a[i] 整除 a[i+1]（或者说 a[i] 是 a[i+1] 的因子）。
答案模 1e9+7。
输入 3 2
输出 5

输入 6 4
输出 39

输入 2 1
输出 2
"""
""" 线性dp+刷表法调和级数复杂度"""




# 186    ms
def solve():
    u, n = RI()
    f = [1] * (u + 1)
    for _ in range(1, n):
        for j in range(u, 0, -1):
            for k in range(j * 2, u + 1, j):
                f[k] = (f[k] + f[j]) % MOD

    print((sum(f) - 1) % MOD)


#   234  ms
def solve2():
    u, n = RI()
    f = [1] * u
    for _ in range(1, n):
        g = [0] * u
        for j, v in enumerate(f, start=1):
            for k in range(j, u + 1, j):
                g[k - 1] = (g[k - 1] + v) % MOD
        f = g
    print(sum(f) % MOD)


#   171  ms
def solve1():
    u, n = RI()
    f = [1] * u
    for _ in range(1, n):
        g = [0] * u
        for j, v in enumerate(f, start=1):
            p = j
            while p <= u:
                g[p - 1] = (g[p - 1] + v) % MOD
                p += j
        f = g
    print(sum(f) % MOD)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
