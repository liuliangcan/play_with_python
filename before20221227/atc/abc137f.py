import sys
from collections import *
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *

if sys.hexversion == 50924784:
    sys.stdin = open('abcinput.txt')

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 998244353
"""https://atcoder.jp/contests/abc173/tasks/abc173_f

输入 n (2≤n≤2e5) 和一棵树的 n-1 条边（节点编号从 1 开始）。
定义 f(L,R) 表示用节点编号在 [L,R] 内的点组成的连通块的个数（边的两个端点必须都在 [L,R] 内）。
输出满足 1≤L≤R≤n 的所有 f(L,R) 的和。
输入
3
1 3
2 3
输出 7

输入
2
1 2
输出 3

输入
10
5 3
5 7
8 9
1 9
9 10
8 4
7 4
6 10
7 2
输出 113
https://atcoder.jp/contests/abc173/submissions/36127951

提示 1：假设一开始没有边，答案是多少？:ans = n * (n + 1) * (n + 2) // 6
方式1:长为1的线段有n个，长为2的线段有n-1个..长为n的线段有1个  复杂度O(n)
        = 1*n+2*(n-1)+3*(n-2)+..+(n-1)*2+n*1
方式2:考虑第i个数为结尾的线段个数  sum起来推公式，复杂度O(1)
        s[n] = (1)+(1+2)+(1+2+3)+...(1+2+..+n)
        a[n] = (n+1)*n/2 = C(n+1,2)
        s[n] = a[1]+a[2]+..+a[n] = C(2,2)+C(3,2)+..+C(n+1,2)
                                =① C(n+2,3)                  
                                = n*(n+1)*(n+2)//6
                                
    解释步骤①:C(n+2,3) = C(2,2)+C(3,2)+..+C(n+1,2) 
            考虑一个数列a[1]..a[n+2] 为了方便思考我们先把数列sort
            考虑问题:从这n+2个数中选3个数的方案数，
                思路1:显然ans=C(n+2,3)
                思路2:考虑取出的3个数中最小值是谁，显然只能是[a[1],a[n]]中的数,那么
                     如果取出的3个数中最小值是a[1],那么剩下2个数要从后边n+1个数中选:ans+=C(n+1,2)
                     如果取出的3个数中最小值是a[2],那么剩下2个数要从后边n个数中选:ans+=C(n,2)
                     如果取出的3个数中最小值是a[3],那么剩下2个数要从后边n-1个数中选:ans+=C(n-1,2)
                     ..                     
                     如果取出的3个数中最小值是a[n],那么剩下2个数要从后边2个数中选:ans+=C(2,2)
                     至此我们考虑了最小数是a[1]到a[n]的所有情况，保证不重不漏，加起来就是答案。
                     综上,ans=C(2,2)+C(3,2)+..+C(n+1,2)
                这两个思路解决了同一个问题,那么两边式子应该相等。即C(n+2,3)=C(2,2)+C(3,2)+..+C(n+1,2)
            那么可以扩展C(r,r)+C(r+1,r)+..+C(m,r) = C(m+1,r+1),其中m>=r
            
提示 2：把边一条一条地加到树上，每加一条边，答案减少了多少？（考虑哪些区间可以包含这条边）
令u<v，左端点可以取1~u，右端点可以取v~n

注意，处理一条边u-v时，只有严格包含u-v的区间，贡献才会减少1，不包含的区间依然是不连通的
"""


#   228   ms
def solve(n, es):
    # ans = 0
    # for i in range(1,n+1):
    #     ans += i*(n-i+1)
    ans = n * (n + 1) * (n + 2) // 6
    for u, v in es:
        if u > v:
            u, v = v, u
        ans -= u * (n - v + 1)
    print(ans)


if __name__ == '__main__':
    n, = RI()
    es = []
    for _ in range(n - 1):
        es.append(RILST())

    solve(n, es)
