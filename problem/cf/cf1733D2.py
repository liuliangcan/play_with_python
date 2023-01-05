# Problem: D2. Zero-One (Hard Version)
# Contest: Codeforces - Codeforces Round #821 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1733/D2
# Memory Limit: 512 MB
# Time Limit: 3000 ms
# 
# Powered by CP Editor (https://cpeditor.org)

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
PROBLEM = """https://codeforces.com/problemset/problem/1733/D2

输入 t(≤1000) 表示 t 组数据，每组数据输入 n(5≤n≤5000) x y(1~1e9) 和两个长为 n 的二进制数 s 和 t。
所有数据的 n 之和不超过 5000。
每次操作你可以把 s 的两个比特位翻转（0 变 1，1 变 0），如果两个比特位相邻，则代价为 x，否则为 y。
输出把 s 变成 t 的最小代价，如果无法做到，输出 -1。

进阶：你能做到 O(n) 时间复杂度吗？
输入 
6
5 8 9
01001
00101
6 2 11
000001
100000
5 7 2
01000
11011
7 8 3
0111001
0100001
6 3 4
010001
101000
5 10 1
01100
01100
输出
8
10
-1
6
7
0
"""
"""
O(n)：
https://codeforces.com/problemset/submission/1733/187727396

空间优化：
https://codeforces.com/problemset/submission/1733/187727663

我的题解，欢迎点赞：
https://www.luogu.com.cn/blog/endlesscheng/solution-cf1733d2
提示 1
首先统计 a[i] \ne b[i]a[i] 

​
 =b[i] 的 ii，记到数组 pp 中，由于每次操作只能改变 22 个这样的 ii，那么如果 pp 的长度是奇数，则输出 -1−1。

提示 2
分类讨论：y \le xy≤x 和 y > xy>x。

提示 3
设 mm 为 pp 的长度。对于 y \le xy≤x：

如果 m=2m=2 且 p[0]+1=p[1]p[0]+1=p[1]，则答案为 \min(2y, x)min(2y,x)，因为可以找个不相邻的位置充当「中转站」（注意 n\ge 5n≥5）；
否则答案为 m/2 \cdot ym/2⋅y，方案是把 p[i]p[i] 和 p[i+m/2]p[i+m/2] 一组。
提示 4
对于 y > xy>x，可以用动态规划求解。

提示 5
设 f[i]f[i] 表示修改 pp 的前 ii 个位置的最小花费，那么对于 p[i]p[i]，有两种方案：

找个不相邻的位置操作，花费 yy，那么对于 p[i]p[i] 相当于花费 y/2y/2，因此
f[i] = f[i-1] + y/2
f[i]=f[i−1]+y/2
不断找相邻的位置操作，把 p[i]p[i] 和 p[i-1]p[i−1] 一组，那么需要操作 p[i]-p[i-1]p[i]−p[i−1] 次，因此
f[i] = f[i-2] + (p[i]-p[i-1])\cdot x
f[i]=f[i−2]+(p[i]−p[i−1])⋅x
两者取最小值，即
f[i] = \min(f[i-1] + y/2, f[i-2] + (p[i]-p[i-1])\cdot x)
f[i]=min(f[i−1]+y/2,f[i−2]+(p[i]−p[i−1])⋅x)
初始值 f[0]=0f[0]=0，f[1]=yf[1]=y，答案为 f[m]f[m]。

代码实现时，为了方便处理 y/2，可以把所有数都乘 2，最后再除以 2。

此外，计算 f 的过程可以用两个变量滚动计算。

答疑
问：为什么花费 y 的时候，不用考虑相邻的情况？

答：因为 y>x，如果相邻，从 f[i-2]f[i−2] 转移过来是更优的。

问：转移方程没有对选了多少个 y 加以限制，如果选了奇数个 y 怎么办？

答：注意 m 是偶数，那么一定会选偶数个 y，你可以从记忆化搜索的角度来思考这一点。
"""


#       ms
def solve():
    t, = RI()
    for _ in range(t):
        n, x, y = RI()
        s, = RS()
        t, = RS()

        def calc():  # 用return跳出比较舒服因此写成方法
            a = []
            for i, (b, c) in enumerate(zip(s, t)):
                if b != c:
                    a.append(i)
            m = len(a)
            if m & 1:
                return print(-1)
            if y <= x:
                if m == 2 and a[0] + 1 == a[1]:
                    return print(min(x, 2 * y))
                return print(m // 2 * y)
            f = [0] * (m + 1)
            for i, v in enumerate(a):
                if i == 0:
                    f[1] = y  # 把数据都乘2
                else:
                    f[i + 1] = min(f[i] + y, f[i - 1] + (v - a[i - 1]) * 2 * x)  # 把数据都乘2
            print(f[-1] // 2)  # 记得除2

        calc()


if __name__ == '__main__':
    solve()
