# Problem: 排列
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/5055/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf, factorial

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """类似康托展开
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


def overk(n, k):
    s = 1
    while n:
        s *= n
        if s >= k:
            return True
        n -= 1
    return False


def check(x):
    pp = set(str(x))
    pp.discard('4')
    pp.discard('7')
    if pp:
        return False
    return True


#       ms
def solve():
    n, k = RI()
    if not overk(n, k):
        return print(-1)
    if n == 1:
        return print(0)
    p = 1
    s = 1
    while s < k:
        p += 1
        s *= p
    a = list(range(n - p + 1, n + 1))
    s = set(a)
    size = len(a)
    k -= 1
    for i, v in enumerate(a):
        ss = sorted(s)
        if factorial(size) == k:
            a[i:] = ss[::-1]
            break
        size -= 1
        f = factorial(size)
        x, k = divmod(k, f)
        a[i] = ss[x]
        s.remove(a[i])
    # print(a)
    # 第k个排列一定是：前边数字就是1~x，后边是剩下数字的排列，且这个数列很短
    # 暴力验证后边部分，然后前边数位dp
    i = n
    ans = 0
    while a:
        # a.pop()
        if check(a.pop()) and check(i):
            ans += 1
        i -= 1
    # 接下来计算1~i 里有几个只含47的数
    s = str(i)
    # print(s)
    @lru_cache(None)
    def f(i, is_limit, is_num):
        if i == len(s):
            return int(is_num)
        ans = 0
        if not is_num:
            ans += f(i + 1, False, False)
        up = int(s[i]) if is_limit else 9
        for j in [4, 7]:
            if j <= up:
                ans += f(i + 1, is_limit and j == up, True)
        return ans

    ans += f(0, True, False)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
