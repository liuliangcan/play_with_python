# Problem: No Palindrome
# Contest: CodeChef - START97B
# URL: https://www.codechef.com/START97B/problems/NOPALINDROME
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
PROBLEM = """问题
给定正整数 
N 和 
K，令 
S 表示最小的具有 
N 位数（没有前导零）的数字，满足以下条件：

对于 
S 的任何长度严格大于 
K 的子串都不是回文串。
找到 
S 的各个数字的和。

注意：

一个数字的子串是通过从数字的开头删除一些（可能为零）数字和从数字的末尾删除一些（可能为零）数字得到的。例如，数字 
3010 的一些子串是 
3010，
301，
010，
01，
10 以及 
0。
子串中可以包含前导零。在上面的例子中， 
010 和 
01 是有效的子串。
输入格式
输入的第一行将包含一个整数 
T，表示测试用例的数量。
每个测试用例由两个以空格分隔的整数 
N 和 
K 组成，如问题描述中所述。
输出格式
对于每个测试用例，输出一个新行，表示满足给定条件的最小的 
N 位数的各个数字的和。
"""
"""手玩一下发现，结果一定是形如10000200 | 10000200的循环
循环节为1000020 ，其中两部分0段可以计算出来。
假设k=4，那么第一个0段长度就是k。
第二个0段要注意，不能和2以及前边的0组合起来超过k，那么长度就是(k-1)//2。
因此循环节总长度p=1+k+1+(k-1)//2。 每个循环节里求和是3.
divmod一下，再讨论最后一个循环节到哪即可。
"""

#       ms
def solve():
    n, k = RI()
    # 100020
    p = 1 + k + 1 + (k - 1) // 2
    x, y = divmod(n, p)
    ans = 3 * x
    if y:
        if y <= k + 1:
            ans += 1
        else:
            ans += 3
    print(ans)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
