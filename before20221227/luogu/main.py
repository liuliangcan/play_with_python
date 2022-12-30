import io
import os
import sys
from bisect import bisect_right
from collections import deque

from sortedcontainers import SortedSet

if os.getenv('LOCALTESTLUOGU'):
    sys.stdin = open('input.txt')
else:
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


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


def solve(L, N, M, D):
    D.append(L)
    n = len(D)

    # 使每块之间最小距离不小于s，要移走多少块石头，O(n)
    # s越大，移走的石头越多，单调递增
    def remove_how_many(s):
        ans = 0
        cur = 0
        for d in D:
            if d - cur < s:
                ans += 1
            else:
                cur = d
        return ans

    pos = my_bisect_right(range(L + 1), M, key=remove_how_many)-1
    print(pos)
    # ans = 0
    # l, r = 1, L
    # while l <= r:
    #     mid = (l + r) >> 1
    #     if remove_how_many(mid) <= M:
    #         ans = mid
    #         l = mid + 1
    #     else:
    #         r = mid - 1
    # print(ans)


if __name__ == '__main__':
    L, N, M = map(int, input().split())
    D = []
    for i in range(N):
        D.append(int(input()))
    solve(L, N, M, D)
    SortedSet()
