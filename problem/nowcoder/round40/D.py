# Problem: 小红升装备
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/80259/D
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

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
from math import sqrt, gcd, inf

# if not sys.version.startswith('3.5.3'):  # ACW没有comb
#     from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""


def iii():  # 牛客输入格式有bug
    num = 0
    neg = False
    while True:
        c = sys.stdin.read(1)
        if c == '-':
            neg = True
            continue
        elif c < '0' or c > '9':
            continue
        while True:
            num = 10 * num + ord(c) - ord('0')
            c = sys.stdin.read(1)
            if c < '0' or c > '9':
                break
        return -num if neg else num


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


class GroupedPackMaxMin:
    """分组背包求最大/最小值
    传入多组物品，每组中只能选一个，求极值。转化成01背包考虑，外层枚举体积j，内层尝试这个j选不同物品(注意和多重背包区分)。
    注意有时会和多重背包混淆：如题意描述成，第i种物品有c个，可以任选几个，但同种物品不区分。
    这种情况用多重背包计算就会出现重复方案，实际上考虑分组背包：这组中有c种物品，只能选0/1个。这c种物品分别是1个i，2个i。。c个i。
    """

    def __init__(self, vol, grouped_items=None, merge=max, sit='just', ini=None):
        """关于ini,可以不填，指定sit即可，其中sit用的最多的是at_most,这时一般可以直接返回p.f[-1]:
                   如果求体积'恰好'j时，ini应该是-inf/inf
                   如果求体积'至少/至多'时，ini应该是0
                   考虑只有一个物品v=4,但枚举j==5的场景，
                       若初始化f[1]=0,f[5]会计算成f[1]+w，是有结果的，实际上认为5可以容纳4，即体积不超过/至多5的数据全部容纳。
                       若初始化f[1]=-inf,则f[5]计算也会是-inf，认为非法。则任何位置只能从0先转移一个合法数据。
               """
        self.grouped_items = grouped_items  # 形如[[(1,2),(2,3)],[(1,2),(2,3)],]，注意是多组数组，每组中只能选一个
        self.merge = merge
        self.vol = vol
        if ini is None:
            if sit == 'just':
                ini = -inf if merge.__name__ == 'max' else inf
            elif sit in ['at_least',
                         'at_most']:  # 注意，至多的情况for循环需要修改为:for j in range(self.vol, -1, -1):f[j] = merge(f[j], f[max(j - v,0)] + w)
                ini = 0
        self.f = [0] + [ini] * vol  # f[j]代表体积j时的最优值，

    def grouped_pack(self, items):
        f, merge = self.f, self.merge
        for j in range(self.vol, 0, -1):
            for v, w in items:
                if j >= v:
                    f[j] = merge(f[j], f[j - v] + w)


#       ms
def solve():
    n, vol = RI()
    f = [0] + [-inf] * vol
    for _ in range(n):
        att, price, cost, upgrade, lvmx = RI()

        if price > vol: continue
        items = [(price, att)]
        for i in range(1, lvmx + 1):
            x, y = att + upgrade * i, price + cost * i
            if y > vol: break
            items.append((y, x))

        for j in range(vol, 0, -1):
            for v, w in items:
                if j < v: break
                f[j] = max(f[j], f[j - v] + w)

    print(max(f))


#       ms
def solve1():
    n, x = RI()
    f = [0] + [-inf] * x
    gp = GroupedPackMaxMin(x)
    for _ in range(n):
        att, price, cost, upgrade, lvmx = RI()

        if price > x: continue
        items = [(price, att)]
        for i in range(1, lvmx + 1):
            x, y = att + upgrade * i, price + cost * i
            if y > x: break
            items.append((y, x))
        gp.grouped_pack(items)

    print(max(gp.f))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
