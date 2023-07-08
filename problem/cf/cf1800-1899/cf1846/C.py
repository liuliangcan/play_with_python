# Problem: C. Rudolf and the Another Competition
# Contest: Codeforces - Codeforces Round 883 (Div. 3)
# URL: https://codeforces.com/contest/1846/problem/C
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
PROBLEM = """Rudolf参加了一场按照ICPC规则进行的程序设计比赛。规则规定，每解决一个问题，参赛者将获得1分，并且将承担从比赛开始到解决问题的时间总和的惩罚。在最终排名中，分数最高的参赛者将排名靠前，如果分数相同，则惩罚时间较低的参赛者将排名靠前。

总共有n个参赛者报名参加比赛。Rudolf是参赛者索引为1的参赛者。已知将提出m个问题，并且比赛将持续h分钟。

一种强大的人工智能预测了ti,j的值，它代表第i个参赛者解决第j个问题所需的时间。

Rudolf意识到解决问题的顺序将影响最终结果。例如，如果h=120，并且解决问题的时间为[20,15,110]，那么如果Rudolf按顺序解决问题：

3,1,2，他只能解决第三个问题，并获得1分和110的惩罚时间。
1,2,3，他将在比赛开始后20分钟解决第一个问题，在20+15=35分钟后解决第二个问题，他将没有时间解决第三个问题。因此，他将获得2分和20+35=55的惩罚时间。
2,1,3，他将在比赛开始后15分钟解决第二个问题，在15+20=35分钟后解决第一个问题，他将没有时间解决第三个问题。因此，他将获得2分和15+35=50的惩罚时间。
Rudolf对于他在比赛中将获得的名次感兴趣，如果每位参赛者按照人工智能的预测选择最佳顺序解决问题。假设在分数和惩罚时间相同的情况下，Rudolf将获得最佳名次。

输入
第一行包含一个整数t（1≤t≤103）- 测试用例的数量。

接下来是测试用例的描述。

每个测试用例的第一行包含三个整数n，m，h（1≤n⋅m≤2⋅105，1≤h≤106）- 参赛者数量，问题数量和比赛持续时间。

然后有n行，每行包含m个整数ti,j（1≤ti,j≤106）- 第i个参赛者解决第j个问题所需的分钟数。

对于所有测试用例，n⋅m的总和不超过2⋅105。

输出
对于每个测试用例，输出一个整数- Rudolf在最终排名中的位置，如果所有参赛者按照最佳顺序解决问题。
"""


#       ms
def solve():
    n, m, h = RI()
    a = []
    one = 0
    for i in range(n):
        t = RILST()
        t.sort()
        x = y = s = 0
        for v in t:
            y += v
            if y <= h:
                x += 1
                s += y
            else:
                break
        if i == 0:
            one = (-x, s)
        a.append((-x, s))
    a.sort()
    print(bisect_left(a, one) + 1)


if __name__ == '__main__':
    t = 1
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
