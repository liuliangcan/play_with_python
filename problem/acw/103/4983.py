# Problem: 猜数字
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4983/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """分解质因数
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


def get_prime_reasons(x):
    # 获取x的所有质因数，虽然是两层循环且没有判断合数，但复杂度依然是O(sqrt(x))
    # 由于i是从2开始增加，每次都除完，因此所有合数的因数会提前除完，合数不会被x整除的
    if x == 1:
        return Counter()
    ans = Counter()
    i = 2
    while i * i <= x:
        while x % i == 0:
            ans[i] += 1
            x //= i
        i += 1
    if x > 1: ans[x] += 1
    return ans


#       ms
def solve():
    n, = RI()
    if n == 1:
        print(0)
        return print()
    if n == 2:
        print(1)
        return print(2)
    cnt = Counter()
    for i in range(2, n + 1):
        for k, v in get_prime_reasons(i).items():
            cnt[k] = max(cnt[k], v)
    ans = []
    # print(cnt)
    for k, v in cnt.items():
        for i in range(1, v + 1):
            ans.append(k ** i)
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
