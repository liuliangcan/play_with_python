import io
import os
import sys
from collections import *
from functools import reduce, lru_cache
from itertools import *
from math import gcd, inf

if sys.hexversion == 50923504:
    sys.stdin = open('input.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = sys.stdin.buffer.readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())
MOD = 10 ** 9 + 7


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


def solve(n, x, a):
    pre = [0] + list(accumulate(a))

    def calc(i, j):
        return pre[j + 1] - pre[i]

    def check(x):  # 跳跃能力是x时，最多能过几次河
        ans = inf
        for i in range(x - 1, n - 1):
            ans = min(ans, calc(i - x + 1, i))
        return ans

    print(my_bisect_left(range(n + 1), 2 * x, lo=1, key=check))


if __name__ == '__main__':
    n, x = RI()
    a = RILST()
    solve(n, x, a)
