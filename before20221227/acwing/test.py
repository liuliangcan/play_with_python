import collections
from collections import Counter

from sortedcontainers import SortedList

#
# MOD = 10 ** 9 + 7
# MAX_N = 10 ** 5 + 5
# inv = [0] * MAX_N
# inv[1] = 1
# p = MOD
# for i in range(2, MAX_N):
#     inv[i] = (p - p // i) * inv[p % i] % p
#
# a = 2675
# b = inv[a]
# print(a * b % MOD)

# SortedList()
# c = Counter()
# c.most_common(2)



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


a = [0, 1, 2, 3, 3, 3, 6, 7, 8, 9, 10]
# print(my_bisect_left(a,12))
# def calc(x):
#     return 10-x
# for i in range(14):
#     print(i, my_bisect_left(a, -i, key=lambda x: - calc(x)))

df = collections.defaultdict()
df.default_factory = lambda :k
df.setdefault()
print(df[1])