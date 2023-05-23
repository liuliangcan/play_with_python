# Problem: C. Edgy Trees
# Contest: Codeforces - Codeforces Round 548 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1139/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，实测这个快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1139/C

输入 n(2≤n≤1e5) k(2≤k≤100) 和一棵无向树的 n-1 条边（节点编号从 1 开始），每条边包含 3 个数 x y c，表示有一条颜色为 c 的边连接 x 和 y，其中 c 等于 0 或 1。

对于长为 k 节点序列 a，走最短路，按顺序经过节点 a1 -> a2 -> ... -> ak。
对于所有长为 k 的节点序列 a（这有 n^k 个），统计至少经过一条 c=1 的边的序列 a 的个数。
输入
4 4
1 2 1
2 3 1
3 4 1
输出 252

输入
4 6
1 2 0
1 3 0
1 4 0
输出 0

输入
3 5
1 2 1
2 3 0
输出 210
"""


class DSU:
    """基于数组的并查集"""
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.set_count = n  # 共几个家族

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
        self.set_count -= 1
        return True


#   187    ms
def solve():
    n, k = RI()
    dsu = DSU(n)
    for _ in range(n - 1):
        u, v, c = RI()
        if c == 0:
            dsu.union(u - 1, v - 1)
    ans = pow(n, k, MOD)
    for i in range(n):
        if dsu.find_fa(i) == i:
            ans = (ans - pow(dsu.size[i], k, MOD)) % MOD
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
