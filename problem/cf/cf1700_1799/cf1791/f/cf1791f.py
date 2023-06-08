# Problem: F. Range Update Point Query
# Contest: Codeforces - Codeforces Round 849 (Div. 4)
# URL: https://codeforces.com/contest/1791/problem/F
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(
    str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

PROBLEM = """给长为n的数组a，和q个操作
操作1 l r,把l到r区间的所有数字编程它的数位和
操作2 i,输出a[i]。
"""
"""由于数位和会迅速收敛(<10则不会继续动)，1e9内最多操作3次，因此可以暴力。
用RUPQ树状数组累计并计算每个位置的操作次数p。
查询时对这个位置进行p次计算，当发现<10则可以提前退出。
由于题目操作不会回退，因此可以把这个数直接更新到a[i]上，那么把cnt[i]置0即可。
    - 剪枝，由于<10的数不会变化，当发现这个位置<10后，不用进行后续的任何操作了，直接返回。
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


def f(x):
    return sum(map(int, str(x)))


#    389   ms
def solve():
    n, q = RI()
    a = [0] + RILST()
    cnt = BinIndexTreeRUPQ(n)
    for _ in range(q):
        t, *qq = RI()
        if t == 1:
            l, r = qq
            cnt.add_interval(l, r, 1)
        else:
            idx = qq[0]
            if a[idx] < 10:
                print(a[idx])
                continue
            p = cnt.query_point(idx)
            cnt.add_interval(idx, idx, -p)
            for _ in range(p):
                if a[idx] < 10: break
                a[idx] = f(a[idx])
            print(a[idx])


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
