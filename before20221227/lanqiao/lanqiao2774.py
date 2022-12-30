import io
import os
import sys
from collections import deque
from functools import reduce, lru_cache
from math import gcd, inf
from operator import or_

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
else:
    input = sys.stdin.buffer.readline
MOD = 10 ** 9 + 7


class IntervalTree:
    def __init__(self, size, nums=None):
        self.size = size
        self.nums = nums
        self.interval_tree = [0] * (size * 4)
        if nums:
            self.build_tree(1, 1, size)

    def build_tree(self, p, l, r):
        interval_tree = self.interval_tree
        nums = self.nums
        if l == r:
            interval_tree[p] = nums[l - 1]
            return
        mid = (l + r) // 2
        self.build_tree(p * 2, l, mid)
        self.build_tree(p * 2 + 1, mid + 1, r)
        interval_tree[p] = gcd(interval_tree[p * 2], interval_tree[p * 2 + 1])

    @lru_cache()
    def gcd_interval(self, p, l, r, x, y):
        if y < l or r < x:
            return 1
        interval_tree = self.interval_tree
        if x <= l and r <= y:
            return interval_tree[p]
        mid = (l + r) // 2
        a = b = None
        if x <= mid:
            a = self.gcd_interval(p * 2, l, mid, x, y)
        if mid < y:
            b = self.gcd_interval(p * 2 + 1, mid + 1, r, x, y)
        if not a:
            return b
        if not b:
            return a
        return gcd(a, b)


class SparseTable:
    def __init__(self, data: list, func=or_):
        # 稀疏表，O(nlgn)预处理，O(1)查询区间最值/或和/gcd
        # 下标从0开始
        self.func = func
        self.st = st = [list(data)]
        i, N = 1, len(st[0])
        while 2 * i <= N+1:
            pre = st[-1]
            st.append([func(pre[j], pre[j + i]) for j in range(N - 2 * i + 1)])
            i <<= 1

    def query(self, begin: int, end: int):  # 查询闭区间[begin, end]的最大值
        lg = (end - begin+1).bit_length() - 1
        # print(lg)
        return self.func(self.st[lg][begin], self.st[lg][end - (1 << lg) + 1])




def my_bisect_left(a, x, lo=None, hi=None, key=None):
    """
    由于3.10才能用key参数，因此自己实现一个。
    :param a: 需要二分的数据
    :param x: 查找的值
    :param lo: 左边界
    :param hi: 右边界(闭区间)
    :param key: 数组a中的值会依次执行key方法，
    :return: 第一个大于等于x的下标位置
    """
    if not lo:
        lo = 0
    if not hi:
        hi = len(a) - 1
    else:
        hi = min(hi, len(a) - 1)
    size = hi - lo + 1

    if not key:
        key = lambda _x: _x
    while size:
        half = size >> 1
        mid = lo + half
        if key(a[mid]) < x:
            lo = mid + 1
            size = size - half - 1
        else:
            size = half
    return lo

def my_bisect_right(a, x, lo=None, hi=None, key=None):
    if not lo:
        lo = 0
    if not hi:
        hi = len(a) - 1
    else:
        hi = min(hi, len(a) - 1)
    size = hi - lo + 1

    if not key:
        key = lambda _x: _x
    while size:
        half = size >> 1
        mid = lo + half
        if key(a[mid]) > x:
            size = half
        else:
            lo = mid + 1
            size = size - half - 1
    return lo
def solve(n, a):
    if reduce(gcd, a) != 1:
        return print(-1)
    c = a.count(1)
    if c:
        return print(n - c)
    # tree = IntervalTree(n, a)
    st = SparseTable(a, gcd)
    ans = inf

    # 每个点找右边相邻区间
    # for i in range(n):
        # def query(k):
        #     return -st.query(i, k)
        #
        # pos = my_bisect_left(range(n), -1, lo=i + 1, hi=n-1, key=query)
        # # print(pos,i)
        # if pos < n and query(pos) == -1:
        #     ans = min(ans, pos - i)

    # 每个点找左边相邻区间
    for i in range(n):
        def query(k):
            return st.query(k, i)

        pos = my_bisect_right(range(i), 1, lo=0, key=query)
        # print(pos,i)
        if pos and query(pos-1) == 1:
            ans = min(ans, i-pos+1)

    print(ans + n - 1)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    solve(n, a)
