# Problem: A. Milking cows
# Contest: Codeforces - Codeforces Round 225 (Div. 1)
# URL: https://codeforces.com/problemset/problem/383/A
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
PROBLEM = """https://codeforces.com/problemset/problem/383/A

输入 n(1≤n≤2e5) 和长为 n 的数组 a，只包含 0 和 1。

你按照某种顺序，标记这 n 个数字。
当你标记一个数字 a[i] 时，统计 a[i] 左边所有没有被标记的 1 的个数，和右边所有没有被标记的 0 的个数，加入答案。

输出答案的最小值。
输入
4
0 0 1 0
输出 1
解释 按照下标 2,3,1,0 的顺序标记这 4 个数。

输入 
5
1 0 1 0 1
输出 3
"""
"""
把 0 视作左箭头 ←，把 1 视作右箭头 →。
考虑两个箭头标记的先后顺序：
1. 两个箭头背靠背：先标记谁都不影响答案。
2. 两个箭头面对面：先标记谁都会把答案加一。
3. 两个箭头都朝右：先标记左边的，这样不影响答案。
4. 两个箭头都朝左：先标记右边的，这样不影响答案。

对于朝右的箭头，我们从左往右标记。
对于朝左的箭头，我们从右往左标记。

在这种操作顺序下，只有面对面的箭头会对答案有贡献。
所以只需要统计有多少对箭头是面对面的。

代码
"""


#       ms
def solve():
    n, = RI()
    a = RILST()
    zero = a.count(0)
    p = 0
    for v in a:
        if v == 0:
            zero -= 1
        else:
            p += zero
    ans = p
    p = 0
    one = a.count(1)
    for v in a[::-1]:
        if v == 1:
            one -= 1
        else:
            p += one
    ans = min(ans, p)
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
