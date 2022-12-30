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
from types import GeneratorType

if sys.hexversion == 50924784:
    sys.stdin = open('cfinput.txt')
    RI = lambda: map(int, input().split())
else:
    input = sys.stdin.readline
    input_int = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    RI = lambda: map(int, input_int().split())

RS = lambda: input().strip().split()
RILST = lambda: list(RI())

MOD = 10 ** 9 + 7
"""https://codeforces.com/problemset/problem/1032/C

输入 n (≤1e5) 和一个长为 n 的数组 a (1≤a[i]≤2e5)。

构造一个长为 n 的数组 b，满足：
1. 1≤b[i]≤5；
2. 如果 a[i]<a[i+1]，则 b[i]<b[i+1]；
3. 如果 a[i]>a[i+1]，则 b[i]>b[i+1]；
4. 如果 a[i]=a[i+1]，则 b[i]≠b[i+1]；
如果不存在这样的 b 则输出 -1，否则输出任意一个满足要求的 b。
1 1 4 2 2
"""

D = list(range(1, 6))


# 124 ms
def solve1(n, a):
    if n == 1:
        return print(1)
    b = [1] * n
    if a[0] > a[1]:
        b[0] = 5

    for i in range(1, n):
        x, y = a[i - 1], a[i]
        if y < x:  # 降
            b[i] = b[i - 1] - 1
            if b[i] < 1:
                return print(-1)
            if i < n - 1:
                if y < a[i + 1]:  # i是谷，则直接置1最优
                    b[i] = 1
                elif y == a[i + 1]:
                    # i和右边相同:
                    # 若i+1后要降，则i+1置5最优，i置1;
                    # 若后边升，不操作:i+1尽量小(1)优，i不变(不要趋向1,但可能已经是1，则i+1只能是2)
                    if i < n - 2 and a[i + 1] > a[i + 2]:
                        b[i] = 1
        elif y > x:  # 升
            b[i] = b[i - 1] + 1
            if b[i] > 5:
                return print(-1)
            if i < n - 1:
                if y > a[i + 1]:
                    b[i] = 5
                elif y == a[i + 1]:
                    if i < n - 2 and a[i + 1] < a[i + 2]:
                        b[i] = 5
        else:  # 相同
            b[i] = 3 if b[i - 1] == 2 else 2  # 先随便置一个数
            if i < n - 1:
                if y < a[i + 1]:  # 若后边升，则置尽量小1/2
                    b[i] = 2 if b[i - 1] == 1 else 1
                elif y > a[i + 1]:  # 若后边降，则置尽量大5/4
                    b[i] = 4 if b[i - 1] == 5 else 5
                # else:  # 若相同，置一个不耽误右边值变成1/5的数(2/3/4任选)
                #     b[i] = 3 if b[i - 1] == 2 else 2

    print(' '.join(map(str, b)))


# 	389 ms
def solve2(n, a):
    if n == 1:
        return print(1)
    f = [[0] * 5 for _ in range(n)]
    f[0] = [1] * 5
    for i in range(1, n):
        x, y = a[i - 1], a[i]
        flag = 0
        if y < x:  # 降
            for j in range(5):
                if any(k for k in f[i - 1][j + 1:]):
                    flag = f[i][j] = 1
        elif y > x:
            for j in range(5):
                if any(k for k in f[i - 1][:j]):
                    flag = f[i][j] = 1
        else:
            for j in range(5):
                if any(f[i - 1][k] for k in range(5) if k != j):
                    flag = f[i][j] = 1
        if not flag:
            return print(-1)
    # print(f)
    b = [f[-1].index(1)]
    for i in range(n - 2, -1, -1):
        x, y = a[i], a[i + 1]
        for j in range(5):
            if f[i][j] and ((x < y and j < b[-1]) or (x > y and j > b[-1]) or (x == y and j != b[-1])):
                b.append(j)
                break
    # print(b)
    print(' '.join(map(lambda x: str(x + 1), b[::-1])))


# 249	 ms
def solve1(n, a):
    if n == 1:
        return print(1)
    f = [[0] * 5 for _ in range(n)]
    f[0] = [1] * 5
    for i in range(1, n):
        x, y = a[i - 1], a[i]
        flag = 0
        g = f[i - 1]
        if y < x:  # 降
            for j in range(5):
                for k in range(j + 1, 5):
                    if g[k]:
                        flag = f[i][j] = 1
                        break
        elif y > x:
            for j in range(5):
                for k in range(j - 1, -1, -1):
                    if g[k]:
                        flag = f[i][j] = 1
                        break
        else:
            for j in range(5):
                for k in range(5):
                    if k != j and g[k]:
                        flag = f[i][j] = 1
                        break
        if not flag:
            return print(-1)
    # print(f)
    b = [f[-1].index(1)]
    for i in range(n - 2, -1, -1):
        x, y = a[i], a[i + 1]
        for j in range(5):
            if f[i][j] and ((x < y and j < b[-1]) or (x > y and j > b[-1]) or (x == y and j != b[-1])):
                b.append(j)
                break
    # print(b)
    print(' '.join(map(lambda x: str(x + 1), b[::-1])))


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


def solve(n, a):
    bo = [1] * n
    up = [5] * n
    for i in range(1, n):
        x, y = a[i - 1], a[i]
        if y > x:
            bo[i] = bo[i - 1] + 1
        elif y < x:
            up[i] = up[i - 1] - 1
        if up[i] < bo[i]:
            return print(-1)

    for i in range(n - 2, -1, -1):
        x, y = a[i], a[i + 1]
        if x > y:
            bo[i] = bo[i + 1] + 1
        elif x < y:
            up[i] = up[i + 1] - 1

        if up[i] < bo[i]:
            return print(-1)
    b = [0] * n

    # print(a)
    # print(up)
    # print(bo)

    ok = False
    def dfs1(i):
        # print(b)
        if i == n:
            nonlocal ok
            ok = True
            return True
        for j in range(bo[i], up[i] + 1):
            if i > 0:
                if a[i] == a[i - 1] and j == b[i - 1]:
                    continue
                if a[i] > a[i - 1] and j <= b[i - 1]:
                    continue
                # if i==3 :
                #     print(a[i] ,a[i - 1] , j , b[i])
                if a[i] < a[i - 1] and j >= b[i - 1]:
                    break
            b[i] = j
            if dfs(i + 1):
                return True
        return False

    @bootstrap
    def dfs(i):
        nonlocal ok
        if i == n:
            ok = True
            yield None

        for j in range(bo[i], up[i] + 1):
            if i > 0:
                if a[i] == a[i - 1] and j == b[i - 1]:
                    continue
                if a[i] > a[i - 1] and j <= b[i - 1]:
                    continue
                # if i==3 :
                #     print(a[i] ,a[i - 1] , j , b[i])
                if a[i] < a[i - 1] and j >= b[i - 1]:
                    break
            b[i] = j
            yield dfs(i + 1)
            if ok:  # 注意 dfs完成后立刻判断，否则会继续for造成数据错误
                break
        yield None

    dfs(0)
    if ok:
        print(' '.join(map(str, b)))
    else:
        print(-1)


if __name__ == '__main__':
    n, = RI()
    a = RILST()


    solve(n, a)
