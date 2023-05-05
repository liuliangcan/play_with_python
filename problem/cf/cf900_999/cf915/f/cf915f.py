# Problem: F. Imbalance Value of a Tree
# Contest: Codeforces - Educational Codeforces Round 36 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/915/F
# Memory Limit: 256 MB
# Time Limit: 4000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/915/F

输入 n (1≤n≤1e6) 和长为 n 的数组 a(1≤a[i]≤1e6)，下标从 1 开始。
然后输入一棵树的 n-1 条边，节点编号从 1 开始。

定义 Δ(x,y) 表示从 x 到 y 的简单路径上的 a[i] 的最大值与最小值的差。
输出所有 Δ(i,j) 的和，其中 1≤i≤j≤n。
输入
4
2 2 3 1
1 2
1 3
1 4
输出 6
"""

"""https://codeforces.com/problemset/submission/915/203430331

贡献法。

最大值和最小值分别计算贡献。

先算最大值的贡献。
随着 a[i] 不断变大，以 a[i] 为最大值的连通块的大小也在变大，这可以用并查集维护。
但是并查集一般是维护边的，怎么维护点呢？
把边 u-v 的边权当作 max(a[u],a[v]) 即可。
所以实际上是按照 max(a[u],a[v]) 对边排序，然后再并查集计算。
合并 u 和 v 的时候，计算 max(a[u],a[v]) 产生的贡献。根据乘法原理，这是 max(a[u],a[v]) * size[u] * size[v]，其中 size[i] 是合并前 i 所处连通块的大小。

最小值的贡献同理，按照 a[i] 从大到小计算。

代码实现时，可以让每条边的第二个端点的 a[i] 值更大，这样排序的时候就不需要求 max 了，效率更高。

相似题目
2421. 好路径的数目"""


class DSU:
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.setCount = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            self.edge_size[y] += 1
            return False
        # if self.size[x] > self.size[y]:  # 注意如果要定向合并x->y，需要干掉这个；实际上上边改成find_fa后，按轶合并没必要了，所以可以常关
        #     x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.setCount -= 1
        return True


#  TLE11    ms
def solve8():
    n, = RI()
    a = RILST()
    es1, es2 = [], []
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        if a[u] > a[v]:
            u, v = v, u
        es1.append((a[v], u, v))
        es2.append((-a[u], u, v))
    ans = 0
    # 每个点作为最大值的贡献
    es1.sort()
    dsu = DSU(n)
    for _, u, v in es1:
        x, y = dsu.find_fa(u), dsu.find_fa(v)
        ans += a[v] * dsu.size[x] * dsu.size[y]
        dsu.union(u, v)
    # 最小
    es2.sort()
    dsu = DSU(n)
    for _, u, v in es2:
        x, y = dsu.find_fa(u), dsu.find_fa(v)
        ans -= a[u] * dsu.size[x] * dsu.size[y]
        dsu.union(u, v)
    print(ans)


#    TLE37   ms
def solve1():
    n, = RI()
    a = RILST()
    es = []
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        if a[u] > a[v]:
            u, v = v, u
        es.append((u, v))
    ans = 0
    # 每个点作为最大值的贡献
    es.sort(key=lambda x: a[x[1]])
    dsu = DSU(n)
    for u, v in es:
        x, y = dsu.find_fa(u), dsu.find_fa(v)
        ans += a[v] * dsu.size[x] * dsu.size[y]
        dsu.union(u, v)
    # 最小
    es.sort(key=lambda x: a[x[0]], reverse=True)
    dsu = DSU(n)
    for u, v in es:
        x, y = dsu.find_fa(u), dsu.find_fa(v)
        ans -= a[u] * dsu.size[x] * dsu.size[y]
        dsu.union(u, v)
    print(ans)


#   TLE37  ms
def solve2():
    n, = RI()
    a = RILST()
    es = []
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        if a[u] > a[v]:
            u, v = v, u
        es.append((u, v))
    ans = 0

    def find_fa(x):
        t = x
        while dsu[x] != x:
            x = dsu[x]
        while t != x:
            dsu[t], t = x, dsu[t]
        return x

    # 每个点作为最大值的贡献
    es.sort(key=lambda x: a[x[1]])
    dsu = list(range(n))
    size = [1] * n
    for u, v in es:
        p = a[v]
        u, v = find_fa(u), find_fa(v)
        ans += p * size[u] * size[v]
        size[u] += size[v]
        dsu[v] = u
    # 最小
    es.sort(key=lambda x: a[x[0]], reverse=True)
    dsu = list(range(n))
    size = [1] * n
    for u, v in es:
        p = a[u]
        u, v = find_fa(u), find_fa(v)
        ans -= p * size[u] * size[v]
        size[u] += size[v]
        dsu[v] = u
    print(ans)


#  3400   ms
def solve():
    n, = RI()
    a = RILST()
    top = 10 ** 6
    mns = [[] for _ in range(top + 1)]  # mns[a[u]] 从大到小遍历，计算每个点作为最小值的贡献
    mxs = [[] for _ in range(top + 1)]  # mxs[a[v]]从小到大遍历，计算每个点作为最大值的贡献
    for _ in range(n - 1):
        u, v = RI()
        u -= 1
        v -= 1
        if a[u] > a[v]:
            u, v = v, u
        mns[a[u]].append((u, v))
        mxs[a[v]].append((u, v))
    ans = 0

    def find_fa(x):
        t = x
        while dsu[x] != x:
            x = dsu[x]
        while t != x:
            dsu[t], t = x, dsu[t]
        return x

    # 每个点作为最大值的贡献
    dsu = list(range(n))
    size = [1] * n
    for p, es in enumerate(mxs):
        for u, v in es:
            u, v = find_fa(u), find_fa(v)
            ans += p * size[u] * size[v]
            size[v] += size[u]
            dsu[u] = v
    # 最小
    dsu = list(range(n))
    size = [1] * n
    for p in range(top, -1, -1):
        for u, v in mns[p]:
            u, v = find_fa(u), find_fa(v)
            ans -= p * size[u] * size[v]
            size[v] += size[u]
            dsu[u] = v
    print(ans)


if __name__ == '__main__':
    solve()
