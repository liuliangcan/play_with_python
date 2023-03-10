# Problem: 有效类型
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4868/
# Memory Limit: 256 MB
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

MOD = 10 ** 9 + 7


#       ms
def solve_tle():
    n, = RI()
    words = list(RS())
    if words == ['int']:
        return print('int')
    p = words.count('pair')
    it = words.count('int')
    if p + 1 != it or words[0] != 'pair' or words[-1] != 'int':
        return print('Error occurred')
    s = []
    for w in words:
        s.append([0, w])
        if w == 'int':
            s[-1][0] = 1
        if len(s) < 3:
            continue
        while len(s) >= 3 and s[-1][0] and s[-2][0] and s[-3][1] == 'pair':
            _, y = s.pop()
            _, x = s.pop()
            s[-1] = [1, f'pair<{x},{y}>']

    if len(s) == 1:
        return print(s[0][1])
    print('Error occurred')


#       ms
def solve1():
    n, = RI()
    words = list(RS())
    if words == ['int']:
        return print('int')
    p = words.count('pair')
    it = words.count('int')
    if p + 1 != it or words[0] != 'pair' or words[-1] != 'int':
        return print('Error occurred')
    s = []
    ans = [''] * len(words)
    for i, w in enumerate(words):
        s.append([0, i, i])
        if w == 'int':
            s[-1][0] = 1

        while len(s) >= 3 and s[-1][0] and s[-2][0] and s[-3][1] == s[-3][2] and words[s[-3][1]] == 'pair':
            _, _, y = s.pop()
            _, _, x = s.pop()
            ans[s[-1][1]] += '<'
            ans[y] += '>'
            ans[x] += ','
            s[-1] = [1, s[-1][1], y]

    if len(s) == 1:
        p = []
        for x, y in zip(words, ans):
            p.append(x)
            p.append(y)

        return print(''.join(p))
    print('Error occurred')

#       ms
def solve2():
    n, = RI()
    words = list(RS())
    if words == ['int']:
        return print('int')
    p = words.count('pair')
    it = words.count('int')
    if p + 1 != it or words[0] != 'pair' or words[-1] != 'int':
        return print('Error occurred')
    s = []
    ans = [''] * len(words)
    for i, w in enumerate(words):
        s.append([0,  i])
        if w == 'int':
            s[-1][0] = 1

        while len(s) >= 3 and s[-1][0] and s[-2][0] and s[-3][0] == 0:
            _,  y = s.pop()
            _,  x = s.pop()
            ans[s[-1][1]] += '<'
            ans[y] += '>'
            ans[x] += ','
            s[-1] = [1,  y]

    if len(s) == 1:
        p = []
        for x, y in zip(words, ans):
            p.append(x)
            p.append(y)

        return print(''.join(p))
    print('Error occurred')


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
    words = list(RS())
    n = len(words)
    i = 0
    ans = []
    flag = True  # 这是由于bootstrap做法不能提前return 要用flag去分支

    @bootstrap
    def dfs():
        nonlocal i, flag
        if i >= n:
            i += 1
            flag = False

        if flag:
            o = words[i]
            i += 1
            if o == 'int':
                ans.append('int')
            else:
                ans.append('pair<')
                yield dfs()
                ans.append(',')
                yield dfs()
                ans.append('>')
        yield

    dfs()
    if i != n:
        return print('Error occurred')
    print(''.join(ans))

if __name__ == '__main__':
    solve()
