# Problem: C1. Increasing Subsequence (easy version)
# Contest: Codeforces - Codeforces Round 555 (Div. 3)
# URL: https://codeforces.com/contest/1157/problem/C1
# Memory Limit: 256 MB
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
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/1157/C1

输入 n(1≤n≤2e5) 和长为 n 的双端队列 a(1≤a[i]≤2e5)。
每次操作，弹出 a 的队首或队尾。
从第二次操作开始，弹出的数字必须严格大于上一次弹出的数字。
输出最多可以弹出多少个数字，以及操作序列（队首为 L，队尾为 R）。
输入中的数据各不相同
"""




#    124   ms
def solve():
    n, = RI()
    a = RILST()
    l, r = 0, n - 1
    ans = []
    cur = 0  # 1<=a[i]
    while l <= r and (a[l] > cur or a[r] > cur):
        if cur < a[l] < a[r] or a[r] <= cur < a[l]:  # 用l优或者只能用l
            cur = a[l]
            ans.append('L')
            l += 1
        else:
            cur = a[r]
            ans.append('R')
            r -= 1

    print(len(ans))
    print(''.join(ans))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
