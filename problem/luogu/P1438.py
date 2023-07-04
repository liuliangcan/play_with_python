# Problem: P1438 无聊的数列
# Contest: Luogu
# URL: https://www.luogu.com.cn/problem/P1438
# Memory Limit: 128 MB
# Time Limit: 1000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """第一种操作是给定一段数列的范围[l, r]，以及等差数列的首项K和公差D，将这个等差数列对应加到范围内的每一个数上。具体地，对于范围内的每一个数a[i]，都将其加上K加上(i - l)乘以D。这样就完成了一次更新操作。

第二种操作是查询数列的第p个数的值，即返回a[p]。

输入格式为：

第一行包含三个整数n、m和opt，分别表示数列的长度、操作的个数和操作类型。
第二行包含n个整数，表示数列a的初始值。
接下来的m行，每行包含一个整数opt和其对应的参数。若opt为1，则再输入四个整数l、r、K和D；若opt为2，则再输入一个整数p。
"""
"""
我们用线段树维护一个差分数组tree，那么询问a[p]实际是询问sum(tree[1~p]) logN搞定
对于区间a[l,r]加上等差数列(k,d),对于差分数组d是:
1. d[l]+=k 
2. d[l+1~r] += d 
3. d[r+1]-=k+d*(r-l)  即等差数列末项
耗时的在操作2，可以用lazy线段树
"""


class IntervalTree:
    """区间加，区间求和"""
    def __init__(self, size):
        self.size = size
        self.interval_tree = [0 for _ in range(size * 4)]
        self.lazys = [0 for _ in range(size * 4)]

    def give_lay_to_son(self, p, l, r):
        interval_tree = self.interval_tree
        lazys = self.lazys
        if lazys[p] == 0:
            return
        mid = (l + r) // 2
        interval_tree[p * 2] += lazys[p] * (mid - l + 1)
        interval_tree[p * 2 + 1] += lazys[p] * (r - mid)
        lazys[p * 2] += lazys[p]
        lazys[p * 2 + 1] += lazys[p]
        lazys[p] = 0

    def add_interval(self, p, l, r, x, y, val):
        """
        把[x,y]区域全+=val
        """
        if y < l or r < x:
            return
        interval_tree = self.interval_tree
        lazys = self.lazys
        if x <= l and r <= y:
            interval_tree[p] += val * (r - l + 1)
            lazys[p] += val
            return
        self.give_lay_to_son(p, l, r)
        mid = (l + r) // 2

        if x <= mid:
            self.add_interval(p * 2, l, mid, x, y, val)
        if mid < y:
            self.add_interval(p * 2 + 1, mid + 1, r, x, y, val)
        interval_tree[p] = interval_tree[p * 2] + interval_tree[p * 2 + 1]

    def sum_interval(self, p, l, r, x, y):
        """
        查找x,y区间的最大值        """

        if y < l or r < x:
            return 0
        if x <= l and r <= y:
            return self.interval_tree[p]
        self.give_lay_to_son(p, l, r)
        mid = (l + r) // 2
        s = 0
        if x <= mid:
            s += self.sum_interval(p * 2, l, mid, x, y)
        if mid < y:
            s += self.sum_interval(p * 2 + 1, mid + 1, r, x, y)
        return s


class BinIndexTreeRURQ:
    """树状数组的RURQ模型"""

    def __init__(self, size_or_nums):  # 树状数组,区间加区间求和，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
            self.c2 = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.c = [0 for _ in range(self.size + 5)]
            self.c2 = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_interval(i + 1, i + 1, v)

    def add_point(self, c, i, v):  # 单点增加,下标从1开始;不支持直接调用，这里增加的是差分数组的单点,同步修改c2
        while i <= self.size:
            c[i] += v
            i += -i & i

    def sum_prefix(self, c, i):  # 前缀求和，下标从1开始；不支持直接调用，这里求和的是差分数组的前缀和;传入c决定怎么计算，但是不要直接调用 无视吧
        s = 0
        while i >= 1:
            s += c[i]
            i -= -i & i
        return s

    def add_interval(self, l, r, v):  # 区间加，下标从1开始，把[l,r]闭区间都加v
        self.add_point(self.c, l, v)
        self.add_point(self.c, r + 1, -v)
        self.add_point(self.c2, l, (l - 1) * v)
        self.add_point(self.c2, r + 1, -v * r)

    def sum_interval(self, l, r):  # 区间求和，下标从1开始，返回闭区间[l,r]上的求和
        return self.sum_prefix(self.c, r) * r - self.sum_prefix(self.c2, r) - self.sum_prefix(self.c, l - 1) * (
                l - 1) + self.sum_prefix(self.c2, l - 1)

    def query_point(self, i):  # 单点询问值，下标从1开始，返回i位置的值
        return self.sum_prefix(self.c, i)

    def lowbit(self, x):
        return x & -x


#    838    ms
def solve():
    n, m = RI()
    a = RILST()
    size = n
    tree = IntervalTree(size)
    # tree.add_interval(1, 1, size, 1, 1, a[0])
    # for i in range(1, n):
    #     tree.add_interval(1, 1, size, i + 1, i + 1, a[i] - a[i - 1])
    for _ in range(m):
        t, *q = RI()
        if t == 1:
            l, r, k, d = q
            tree.add_interval(1, 1, size, l, l, k)
            tree.add_interval(1, 1, size, l + 1, r, d)
            if r + 1 <= n:
                tree.add_interval(1, 1, size, r + 1, r + 1, -k - d * (r - l))
        else:
            print(tree.sum_interval(1, 1, size, 1, q[0]) + a[q[0] - 1])


#    417ms
def solve1():
    n, m = RI()
    a = RILST()
    tree = BinIndexTreeRURQ(n + 1)
    tree.add_interval(1, 1, a[0])
    for i in range(1, n):
        tree.add_interval(i + 1, i + 1, a[i] - a[i - 1])
    for _ in range(m):
        t, *q = RI()
        if t == 1:
            l, r, k, d = q
            tree.add_interval(l, l, k)
            tree.add_interval(l + 1, r, d)
            tree.add_interval(r + 1, r + 1, -k - d * (r - l))
        else:
            print(tree.sum_interval(1, q[0]))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
