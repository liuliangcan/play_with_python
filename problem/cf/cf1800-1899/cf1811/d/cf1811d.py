# Problem: D. Umka and a Long Flight
# Contest: Codeforces - Codeforces Round 863 (Div. 3)
# URL: https://codeforces.com/contest/1811/problem/D
# Memory Limit: 256 MB
# Time Limit: 3000 ms

import sys
from functools import lru_cache
from math import log2

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/contest/1811/problem/D
定义斐波那契数列为fib=[1,1,2,3...]，定义第n个fib矩形的高是fib[n],宽fib[n+1]的长方形。
输入t(<=2e5)表示t组数据，每组数据：
输入n(<=44), x, y (为第n个fib矩形内的合法坐标点)，
你需要判断能否把矩形切分成恰好n+1个正方形方格，且同时满足3个条件：
1. (x,y)位置必须单独切分成1X1的小方格。
2. 至少有一对方块的边长相同。
3. 每个方格的边长都是斐波那契数。
"""
"""
直接dfs分治，注意加记忆化过不了。
显然n=1是能过的，看case1。
剩余情况画一下图，尝试把矩形的长边按照宽的位置切一刀，那么可以选左边或者右边切出来；这样会变成一个正方形和一个更小的n-1号fib矩形；
目标位置必须在矩形上才可以。否则返回false。
注意t<=2e5,因此组内需要保证复杂度<=500,加记忆可能导致内存问题，巨卡。不加记忆化由于n一直-1，因此最多是44。
当然可以写while写法，直接迭代n,x,y。
"""

fib = [1, 1]
for _ in range(44):
    fib.append(fib[-1] + fib[-2])


#     1309  ms
def solve():
    n, x, y = RI()

    # @lru_cache
    def f(n, x, y):
        if n == 1:
            return True
        h, w = fib[n], fib[n + 1]

        x = min(x, h - x + 1)
        if y > h:
            return f(n - 1, y - h, x)
        if y <= w - h:
            return f(n - 1, y, x)
        return False

    ans = f(n, x, y)
    # f.cache_clear()
    if ans:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    t, = RI()
    ans = []
    for _ in range(t):
        ans.append(solve())
        # f.cache_clear()
    print(*ans, sep='\n')
