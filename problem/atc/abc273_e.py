# Problem: E - Notebook
# Contest: AtCoder - Panasonic Programming Contest 2022(AtCoder Beginner Contest 273)
# URL: https://atcoder.jp/contests/abc273/tasks/abc273_e
# Memory Limit: 1024 MB
# Time Limit: 3000 ms
#
# Powered by CP Editor (https://cpeditor.org)

import sys
import heapq
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

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://atcoder.jp/contests/abc273/tasks/abc273_e

一开始你有一个空数组 a 和一个 1e9 页的笔记本，每页上都记录着一个空数组。
有四种类型的操作：
ADD x：在 a 的末尾添加元素 x (1≤x≤1e9)。
DELETE：如果 a 不为空，删除 a 的最后一个元素。
SAVE y：把 a 记在第 y 页上（覆盖原来的数组）。
LOAD z：把 a 替换为第 z 页上的数组。

输入 q(≤5e5) 和 q 个操作。
在每个操作结束后，你需要输出 a 的最后一个元素（数组为空时输出 -1）。
输入
11
ADD 3
SAVE 1
ADD 4
SAVE 2
LOAD 1
DELETE
DELETE
LOAD 2
SAVE 1
LOAD 3
LOAD 1
输出
3 3 4 4 3 -1 -1 4 4 -1 4
"""
"""用一个类似Trie的结构来模拟，但是节点储存父节点，以便pop
cur指针永远指向当前最后一个节点，
add时，增加一个节点[cur,y]
delete时，cur指向父节点cur=cur[0]
save时，把当前节点cur储存到第y页。
load时，替换cur为第y页上的数据。
"""
# if __name__ == '__main__':
#     q, = RI()
#     cur = []
#     p = {}
#     ans = []
#     for _ in range(q):
#         ops = list(RS())
#         if len(ops) == 2:
#             y = int(ops[1])
#         if ops[0][0] == 'D':
#             if cur:
#                 cur = cur[0]
#         elif ops[0][0] == 'A':
#             cur = [cur, y]
#         elif ops[0][0] == 'S':
#             p[y] = cur
#         else:
#             cur = p.get(y, [])
#         ans.append(cur[1] if cur else -1)
#     print(' '.join(map(str, ans)))

if __name__ == '__main__':
    q, = RI()
    cur = root = [0, -1]
    cur[0] = root  # 小技巧，避免删除时的判断；且ans可以直接取
    p = {}
    ans = []
    for _ in range(q):
        ops = list(RS())
        if len(ops) == 2:
            y = int(ops[1])
        if ops[0][0] == 'D':
            cur = cur[0]
        elif ops[0][0] == 'A':
            cur = [cur, y]
        elif ops[0][0] == 'S':
            p[y] = cur
        else:
            cur = p.get(y, root)
        ans.append(cur[1])
    print(*ans)
