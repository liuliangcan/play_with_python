import sys
from collections import *
from itertools import *
from math import *
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')

# input = sys.stdin.readline
# input_int = sys.stdin.buffer.readline
# RI = lambda: map(int, input_int().split())
# RS = lambda: input().strip().split()
# RILST = lambda: list(RI())

# RI = lambda: map(int, sys.stdin.buffer.readline().split())
# RS = lambda: sys.stdin.readline().strip().split()
# RILST = lambda: list(RI())

# input = sys.stdin.buffer.readline
# RI = lambda: map(int, input().split())
# RS = lambda: map(bytes.decode, input().strip().split())
# RILST = lambda: list(RI())

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1178/E

输入一个长度不超过 1e6 的字符串 s，仅包含 a b c，且相邻字符不同。
你需要找到一个 s 的回文子序列 t，且 t 的长度至少是 s 长度的一半（下取整）。
输出任意一个符合要求的 t。
注意子序列不要求连续。
输入 cacbac
输出 aba

输入 abc
输出 a

输入 cbacacacbcbababacbcb
输出 cbaaacbcaaabc

https://codeforces.com/contest/1178/submission/173928518
位运算做法 https://codeforces.com/contest/1178/submission/173928055
Python https://codeforces.com/contest/1178/submission/173920506

提示 1：根据鸽巢原理，s 的前两个字符和后两个字符中，必然有两个相同的字符，且由于 s 的相邻字符不同，这两个相同字符必然一个在前两个字符中，另一个在后两个字符中。

提示 2：去掉首尾各两个字符，按同样的方法处理剩余字符。

提示 3：如果剩余字符不足 4 个，可以任取一个字符，作为 t 的回文中心。
"""


#  171	 ms
def solve(s):
    ans = []
    l, r = 0, len(s) - 1

    while l + 2 < r:
        ans.append(s[l] if s[l] in s[r - 1:r + 1] else s[l + 1])
        r -= 2
        l += 2
    m = '' if l > r else s[l]
    print(''.join(ans + [m] + ans[::-1]))


#  201	 ms
def solve2(s):
    n = len(s)
    if n <= 3:
        return print(s[0])

    ans = []
    l, r = 0, n - 1

    while l + 2 < r:
        ans.append(({s[r], s[r - 1]} & {s[l], s[l + 1]}).pop())
        r -= 2
        l += 2
    m = '' if l > r else s[l]
    print(''.join(ans + [m] + ans[::-1]))


def solve3(s):
    n = len(s)
    if n <= 3:
        return print(s[0])

    ans = []
    l, r = 0, n - 1

    while l + 2 < r:
        if s[l] == s[r]:
            ans.append(s[l])
        elif s[l + 1] == s[r]:
            ans.append(s[r])
            l += 1
        elif s[l] == s[r - 1]:
            ans.append(s[l])
            r -= 1
        else:
            ans.append(s[l + 1])
            l += 1
            r -= 1
        l += 1
        r -= 1

    m = '' if l > r else s[l]
    print(''.join(ans + [m] + ans[::-1]))


if __name__ == '__main__':
    s, = RS()

    solve(s)
    'babababcbcbacacac'
    'aaabcbaaa'
