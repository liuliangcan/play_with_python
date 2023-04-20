# Problem: B. Tree Tag
# Contest: Codeforces - Codeforces Round 668 (Div. 1)
# URL: https://codeforces.com/problemset/problem/1404/B
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1404/B

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤1e5。
每组数据输入 n(2≤n≤2e5) 表示一棵 n 个节点的树（节点编号从 1 开始）。
然后输入树上两个不同的点 a 和点 b，表示 Alice 和 Bob 的位置。
然后输入 da db，范围在 [1,n-1]。表示 Alice 和 Bob 每次传送的最大距离。例如从 x 传送到 y，那么 x 到 y 的简单路径的边数不能超过最大距离。
然后输入这棵树的 n-1 条边。

Alice 和 Bob 轮流在树上传送（可以原地不动），Alice 先手。
Bob 逃，Alice 追。
如果在有限步内 Alice 和 Bob 能在同一个点，输出 Alice，否则输出 Bob。
注意从 x 传送到 y，并不会经过从 x 到 y 的简单路径的中间节点。
"""
"""
输入
4
4 3 2 1 2
1 2
1 3
1 4
6 6 1 2 5
1 2
6 5
2 3
3 4
4 5
9 3 9 2 5
1 2
1 6
1 9
1 3
9 5
7 9
4 8
4 3
11 8 11 3 3
1 2
11 9
4 9
6 5
2 10
3 2
5 9
8 3
7 4
7 10
输出
Alice
Bob
Alice
Alice"""

"""https://codeforces.com/contest/1404/submission/202566203

分类讨论：

如果 2*da >= db，那么 Alice 每次向 Bob 移动一步，必然可以在某个时刻让 Bob 无路可走。

如果 Alice 到 Bob 的距离 <= da，那么 Alice 第一步就可以和 Bob 相遇。

如果 2*da >= 树的直径，那么 Alice 只要走到树的直径的中点，就可以传送到树的任意位置，也就可以和 Bob 相遇了。

其余情况，Bob 总是可以「跨过」Alice。

注：树的直径可以用 DP，也可以用两次 DFS。

---

@Aging：这题告诉我们既要有生存能力也要有生存空间。"""


#   233    ms
def solve():
    n, a, b, da, db = RI()
    a -= 1
    b -= 1
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    if da * 2 >= db:  # b被逼到边缘无法跨过
        return print('Alice')

    def get_d():  # ab距离
        d = 0
        q = [(a, -1)]
        while q:
            d += 1
            nq = []
            for u, fa in q:
                for v in g[u]:
                    if v == b:
                        return d
                    if v == fa:
                        continue
                    nq.append((v, u))
            q = nq

    d = get_d()
    if d <= da:
        return print('Alice')

    start = 0
    dim = 0  # 直径
    for _ in range(2):
        dim = -1
        q = [(start, -1)]
        while q:
            dim += 1
            nq = []
            for u, fa in q:
                for v in g[u]:
                    if v == fa:
                        continue
                    nq.append((v, u))
                    start = v
            q = nq
    if dim <= 2 * da:  # a走到直径中心，下一步可以到达任意位置
        return print('Alice')
    print('Bob')


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
