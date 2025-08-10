# Problem: F. Skibidus and Slay
# Contest: Codeforces - Codeforces Round 1003 (Div. 4)
# URL: https://codeforces.com/problemset/problem/2065/F
# Memory Limit: 512 MB
# Time Limit: 4000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RILST = lambda: list(RI())
# DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')  # cf突然编不过这行了
print = lambda d: sys.stdout.write(
    d + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

PROBLEM = """https://codeforces.com/problemset/problem/2065/F

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤5e5。
每组数据输入 n(2≤n≤5e5) 和长为 n 的数组 a(1≤a[i]≤n)。
然后输入一棵 n 个节点的无向树的 n-1 条边。节点编号从 1 开始。节点 i 的点权为 a[i]。

对于 1 到 n 的每个整数 x，判断：
树中是否存在一条至少有两个点的简单路径，路径点权的严格众数存在且等于 x？输出 0 或者 1。
注：序列 S 的严格众数为出现次数严格大于 |S|/2 的数。

你需要输出一个长为 n 的 0-1 字符串。
输入
4
3
1 2 3
1 3
2 3
4
3 1 1 3
1 2
2 3
4 2
4
2 4 4 2
1 2
2 3
3 4
13
1 4 4 7 4 7 1 1 7 11 11 11 11
1 2
2 3
3 4
4 5
4 6
2 7
7 8
2 9
6 10
5 11
11 12
10 13
输出
000
1010
0001
1001001000100
"""


#       ms
def solve():
    n, = RI()
    a = [0] + RILST()
    vis = set()
    ans = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = RI()
        x, y = a[u], a[v]
        if x == y:
            ans[x] = 1
            continue
        # if not ans[y]:
        if u << 20 | y in vis:
            ans[y] = 1
        else:
            vis.add(u << 20 | y)
        # if not ans[x]:
        if v << 20 | x in vis:
            ans[x] = 1
        else:
            vis.add(v << 20 | x)
    print(''.join(map(str, ans[1:])))
    # print(*ans[1:], sep='')


#   TLE21    ms
def solve1():
    n, = RI()
    a = [0] + RILST()
    vis = [set() for _ in range(n + 1)]
    ans = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = RI()
        if a[u] == a[v]:
            ans[a[u]] = 1
            continue
        if a[v] in vis[u]:
            ans[a[v]] = 1
        else:
            vis[u].add(a[v])
        if a[u] in vis[v]:
            ans[a[u]] = 1
        else:
            vis[v].add(a[u])
    # print(''.join(map(str, ans[1:])))
    print(*ans[1:], sep='')


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
