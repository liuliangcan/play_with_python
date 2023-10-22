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
PROBLEM = """https://www.lanqiao.cn/problems/5131/learning/?contest_id=144
离线查询做两次，
先处理a<b的数据：把r<b的区间全加进BIT，那么a位置就是有几个区间包含a。
再处理a>b的数据：把l>b的区间全加进去
注意两次排序是不同的：
    向右处理lr要按r排序
    向左处理lr要按l排序
"""


class BinIndexTreeRUPQ:
    """树状数组的RUPQ模型，结合差分理解"""

    def __init__(self, size_or_nums):  # 树状数组，下标需要从1开始
        # 如果size 是数字，那就设置size和空数据；如果size是数组，那就是a
        if isinstance(size_or_nums, int):
            self.size = size_or_nums
            self.c = [0 for _ in range(self.size + 5)]
        else:
            self.size = len(size_or_nums)
            self.c = [0 for _ in range(self.size + 5)]
            for i, v in enumerate(size_or_nums):
                self.add_interval(i + 1, i + 1, v)

    def add_point(self, i, v):  # 单点增加,下标从1开始;不支持直接调用，这里增加的是差分数组的单点
        while i <= self.size:
            self.c[i] += v
            i += i & -i

    def sum_prefix(self, i):  # 前缀求和，下标从1开始；不支持直接调用，这里求和的是差分数组的前缀和
        s = 0
        while i >= 1:
            s += self.c[i]
            i &= i - 1
        return s

    def add_interval(self, l, r, v):  # 区间加，下标从1开始，把[l,r]闭区间都加v
        self.add_point(l, v)
        self.add_point(r + 1, -v)

    def query_point(self, i):  # 单点询问值，下标从1开始，返回i位置的值
        return self.sum_prefix(i)

    def lowbit(self, x):
        return x & -x


def read_int():
    num = 0
    neg = 1
    while True:
        c = sys.stdin.buffer.read(1)
        if c == '-':
            neg = -1
            continue
        elif not b'0' <= c <= b'9':
            continue
        while True:
            num = num * 10 + int(c.decode())
            c = sys.stdin.buffer.read(1)
            if not b'0' <= c <= b'9':
                break
        return num * neg


#    2554 ms
def solve():
    n = read_int()
    q = read_int()
    lr = []
    for _ in range(n):
        l, r = read_int(), read_int()
        lr.append((l, r))
    qs = []
    ans = [0] * q
    for i in range(q):
        a, b = read_int(), read_int()
        qs.append((a, b, i))

    qs.sort(key=lambda x: x[1])
    lr.sort(key=lambda x: x[1])
    tree = BinIndexTreeRUPQ(2 * 10 ** 5 + 5)
    j = 0
    for a, b, i in qs:
        if a >= b:
            continue
        while j < n and lr[j][1] < b:
            tree.add_interval(lr[j][0], lr[j][1], 1)
            j += 1
        ans[i] = tree.query_point(a)

    qs.sort(key=lambda x: x[1], reverse=True)
    lr.sort(reverse=True)
    tree = BinIndexTreeRUPQ(2 * 10 ** 5 + 5)
    j = 0
    for a, b, i in qs:
        if a <= b:
            continue
        while j < n and lr[j][0] > b:
            tree.add_interval(lr[j][0], lr[j][1], 1)
            j += 1
        ans[i] = tree.query_point(a)
    print(*ans, sep='\n')


# 2552
def solve2():
    n, q = RI()
    lr = []
    for _ in range(n):
        l, r = RI()
        lr.append((l, r))
    qs = []
    ans = [0] * q
    for i in range(q):
        a, b = RI()
        qs.append((a, b, i))
    qs.sort(key=lambda x: x[1])
    lr.sort(key=lambda x: x[1])
    tree = BinIndexTreeRUPQ(2 * 10 ** 5 + 5)
    j = 0
    for a, b, i in qs:
        if a >= b:
            continue
        while j < n and lr[j][1] < b:
            tree.add_interval(lr[j][0], lr[j][1], 1)
            j += 1
        ans[i] = tree.query_point(a)

    qs.sort(key=lambda x: x[1], reverse=True)
    lr.sort(reverse=True)
    tree = BinIndexTreeRUPQ(2 * 10 ** 5 + 5)
    j = 0
    for a, b, i in qs:
        if a <= b:
            continue
        while j < n and lr[j][0] > b:
            tree.add_interval(lr[j][0], lr[j][1], 1)
            j += 1
        ans[i] = tree.query_point(a)
    print(*ans, sep='\n')


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
