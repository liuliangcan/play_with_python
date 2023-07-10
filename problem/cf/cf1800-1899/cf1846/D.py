# Problem: D. Rudolph and Christmas Tree
# Contest: Codeforces - Codeforces Round 883 (Div. 3)
# URL: https://codeforces.com/contest/1846/problem/D
# Memory Limit: 256 MB
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
RANDOM = random.randrange(2**62)
MOD = 10**9 + 7
# MOD = 998244353
PROBLEM = """鲁道夫画了一棵漂亮的圣诞树，并决定将这幅画打印出来。然而，墨盒中的墨水通常在最不方便的时候用完。因此，鲁道夫想要提前计算他将需要多少绿色墨水。

这棵树是一根垂直的主干，上面有不同高度的相同三角形枝条。主干的宽度可以忽略不计。

每个枝条是一个底边为 d
的等腰三角形，高度为 h
，底边与主干垂直。这些三角形呈上升角度排列，主干正好通过中间。第 i 个三角形的底边位于一个高度为 yi
。

下图展示了一棵树的例子，其中 d=4，h=2，有三个底边高度分别为 [1,4,5] 的枝条。

帮助鲁道夫计算树的枝条的总面积。

输入
第一行包含一个整数 t（1≤t≤104）- 测试用例的数量。

然后是测试用例的描述。

每个测试用例的第一行包含三个整数 n, d, h（1≤n,d,h≤2⋅105）- 枝条的数量，底边的长度和枝条的高度，依次。

每个测试用例的第二行包含 n 个整数 yi（1≤yi≤109，y1<y2<...<yn）- 枝条的底边高度。

所有测试用例中 n 的总和不超过 2⋅105。

输出
对于每个测试用例，输出一个实数，表示树的枝条的总面积。如果答案的绝对误差或相对误差不超过 10−6，则视为正确。
"""



#       ms
def solve():
    n,d,h = RI()
    a = RILST()
    s = d*h*n
    """
    h/d = (h-c)/x
    x = (h-c)*d/h
    """
    for i in range(1,n):
        c = a[i] - a[i-1]
        if c >= h:continue
        # s -= (h-c)*d/h*2*(h-c)
        s -= h*d * (h-c)/h* (h-c)/h
        # print(h-c,h*d * (h-c)/h* (h-c)/h)


    print(s/2)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
