# Problem: 顶级厨师
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/56825/E
# Memory Limit: 524288 MB
# Time Limit: 6000 ms

import sys
from bisect import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n"
                                   )  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """有点像99乘法表。
二份答案。
令ok(x)表示严格小于x的数目有多少个，显然x越大，这个数目越大；对于<x的数，ok(x)<qi;
实现ok时也要二分。
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


#   3143    ms
def solve1():
    n, m, k, q = RI()
    a = RILST()
    b = RILST()
    ban = [[] for _ in range(n)]
    for _ in range(k):
        u, v = RI()
        ban[u - 1].append(b[v - 1])
    for v in ban:
        v.sort()
    b.sort()
    UP = 10 ** 12
    for _ in range(q):
        qq, = RI()

        def ok(x):
            s = 0
            for i, v in enumerate(a):
                p = x // v
                s += bisect_right(b, p) - bisect_right(ban[i], p)
                if s >= qq:
                    return True
            return False

        print(lower_bound(1, UP, ok))


#   1661ms
def solve2():
    n, m, k, q = RI()
    a = RILST()
    b = RILST()
    ban = []
    for _ in range(k):
        u, v = RI()
        ban.append(a[u - 1] * b[v - 1])
    ban.sort()
    b.sort()
    a.sort()
    UP = a[-1] * b[-1]
    for _ in range(q):
        qq, = RI()

        def ok(x):
            s = -bisect_right(ban, x)
            for v in a:
                s += bisect_right(b, x // v)
                if s >= qq:
                    return True
            return False

        print(lower_bound(1, UP, ok))


#   1661ms
def solve():
    n, m, k, q = RI()
    a = RILST()
    b = RILST()
    ban = []
    for _ in range(k):
        u, v = RI()
        ban.append(a[u - 1] * b[v - 1])
    ban.sort()
    b.sort()
    a.sort()
    UP = a[-1] * b[-1] + 1
    for _ in range(q):
        qq, = RI()

        l, r = 0, UP
        while l + 1 < r:
            mid = (l + r) >> 1
            s = -bisect_right(ban, mid)
            for v in a:
                s += bisect_right(b, mid // v)
                if s >= qq:
                    break
            if s >= qq:
                r = mid
            else:
                l = mid
        print(r)


if __name__ == '__main__':
    solve()
