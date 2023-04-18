# Problem: A. Division
# Contest: Codeforces - Codeforces Round 680 (Div. 1, based on Moscow Team Olympiad)
# URL: https://codeforces.com/problemset/problem/1444/A
# Memory Limit: 512 MB
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
from functools import lru_cache
from types import GeneratorType
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")
MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1444/A

输入 T(≤50) 表示 T 组数据。
每组数据输入 p(1≤p≤1e18) 和 q(2≤q≤1e9)。

输出最大的 x，满足 p 是 x 的倍数，且 x 不是 q 的倍数。
输入
3
10 4
12 6
179 822
输出
10
4
179
"""
"""https://codeforces.com/problemset/submission/1444/202556296

如果 p 不是 q 的倍数，那么答案就是 p。
如果 p 是 q 的倍数，那么答案必须比 q 小，又能整除 p。
考虑质因子分解：
例如 p = 2^5 * 3^4，q = 2^3 * 3^4，通过把 p 中 2 的幂次减小到 2，得到 2^2 * 3^4，就可以满足题目要求了（不是 q 的倍数）
也可以把 p 中 3 的幂次减小到 3，得到 2^5 * 3^3，同样不是 q 的倍数。
遍历 q 的每个质因子（必然都是 p 的质因子），幂次减小后的数的最大值即为答案。

怎么实现呢？模拟的做法是质因子分解（之前周赛讲过），计算质因子的幂次。也可以从 p 开始不断除质因子，直到无法被 q 整除时为止。"""
"""注意到p是1e8无法分解质因数。但是可以对q分解。
分类讨论:
1. 若p不能被q整除，显然最大的p就是答案。
2. 否则，p中一定包含了q中所有质因数，且每个质因数数量>=q中的数量。
    - 不在q中的质因数，一定可以贡献在答案x中。
    - 那么只需要枚举所有q中的质因子k，数量v，让p中的k数量减小到恰好<v,即v-1,其它质因子不变，则这个x一定不能被q整除，且最大。
    - 计算p中有多少个k可以连除，最多lg(1e18)次。
    - 总复杂度logq*logp
"""


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


#   93    ms
def solve1():
    p, q = RI()
    if p < q or p % q:
        return print(p)
    ans = 1
    for k, v in get_prime_reasons(q).items():
        cnt = v
        x = p // (k ** v)
        while x % k == 0:
            cnt += 1
            x //= k
        # ans = max(ans, p // (k ** (cnt - v + 1)))
        ans = max(ans, x*k**(v-1))  # 避免除法
    print(ans)

#   93    ms
def solve():
    p, q = RI()
    if p < q or p % q:
        return print(p)
    ans = 1
    for k, v in get_prime_reasons(q).items():
        x = p // (k ** v)
        while x % k == 0:
            x //= k
        # ans = max(ans, p // (k ** (cnt - v + 1)))
        ans = max(ans, x*k**(v-1))  # 避免除法
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
