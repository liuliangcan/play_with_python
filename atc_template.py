import sys
import bisect
import random
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt, gcd, inf
from array import *
from functools import lru_cache
from types import GeneratorType
from heapq import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc178/tasks/abc178_f

输入 n(≤2e5) 和两个非降数组 a 和 b，元素范围在 [1,n]。
如果可以重排 b，使得 a[i] != b[i] 对每个 i 都成立，则输出 Yes 和重排后的 b，否则输出 No。
输入
6
1 1 1 2 2 3
1 1 1 2 2 3
输出
Yes
2 2 3 1 1 1

输入
3
1 1 2
1 1 3
输出
No

输入
4
1 1 2 3
1 2 3 3
输出
Yes
3 3 1 2

"""
"""
将b翻转，易得最多有一段和a重叠(相同),设这段上的数字是v.
对于段中每个v，在b里找到一个非v位置j和它交换，其中a[j]和b[j]都不等于v
j使用同向双指针维护，不必判<n,因为只有cnt[v]>n才会出现位置不够用的情况，提前特判，
忽略Counter,时间复杂度O(n+n),即i、j的移动距离
"""


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


#       ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    if max(Counter(a + b).values()) > n:
        return print('No')
    print('Yes')
    j = 0
    b = b[::-1]
    for i in range(n):
        if a[i] == b[i]:
            v = a[i]
            while a[j] == v or b[j] == v:
                j += 1
            b[i], b[j] = b[j], b[i]
    print(*b, sep=' ')


if __name__ == '__main__':
    solve()
