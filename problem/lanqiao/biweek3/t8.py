import sys
from collections import *
from heapq import *
from math import  inf

if not sys.version.startswith('3.5.3'):  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """
"""




class PrimeTable:
    def __init__(self, n: int) -> None:
        self.n = n
        self.primes = primes = []  # 所有n以内的质数
        self.min_div = min_div = [0] * (n + 1)  # md[i]代表i的最小(质)因子
        min_div[1] = 1

        # 欧拉筛O(n)，顺便求出min_div
        for i in range(2, n + 1):
            if not min_div[i]:
                primes.append(i)
                min_div[i] = i
            for p in primes:
                if i * p > n: break
                min_div[i * p] = p
                if i % p == 0:
                    break

    def prime_factorization(self, x: int):
        """分解质因数，复杂度；建议x不要超过n^2,这样可以在prime里枚举
        1. 若x>n则需要从2模拟到sqrt(x)，如果中间x降到n以下则走2；最坏情况，不含低于n的因数，则需要开方复杂度
        2. 否则x质因数的个数，那么最多就是O(lgx)"""
        n, min_div = self.n, self.min_div
        for p in self.primes:  # 在2~sqrt(x)的质数表上遍历，会快一些
            if x <= n or p * p > x:
                break
            if x % p == 0:
                cnt = 0
                while x % p == 0: cnt += 1; x //= p
                yield p, cnt
        if x > n*n:
            for p in range(n, int(x ** 0.5) + 1):  # 分解质因数不要直接遍历2~sqrt(x)的自然数，
                if x <= n: break
                if x % p == 0:
                    cnt = 0
                    while x % p == 0: cnt += 1; x //= p
                    yield p, cnt
        while 1 < x <= n:
            p, cnt = min_div[x], 0
            while x % p == 0: cnt += 1; x //= p
            yield p, cnt
        if x >= n and x > 1:
            yield x, 1



pt = PrimeTable(10 ** 4)

primes = pt.primes
# print(list(pt.prime_factorization(1)))
# print(list(pt.prime_factorization(10)))
# print(list(pt.prime_factorization(13)))

def solve():
    """01bfs"""
    n, a, b = RI()
    arr = RILST()

    def fff(x):
        res = 0
        for p in primes:
            if x <= 1: break
            while x % p == 0:
                res += p
                x //= p
        if x > 1: res += x
        return res % n + 1
    g = [[] for _ in range(2 * n + 3)]
    for i, v in enumerate(arr, start=1):
        f = sum(x * y for x, y in pt.prime_factorization(v)) % n + 1
        # f = fff(v)
        ff = f + n + 1  # 跳到虚拟节点，边权0;出虚拟节点，边权1
        g[ff].append((i, 1))
        g[i].append((ff, 0))
        if f <= n:  # 互跳节点
            g[i].append((f, 1))
            g[f].append((i, 1))

    q = deque([a])
    dis = [inf] * (2 * n + 3)
    dis[a] = 0
    while q:
        u = q.popleft()
        c = dis[u]
        if u == b:
            return print(c)
        for v, w in g[u]:
            if c + w < dis[v]:
                dis[v] = c + w
                if w:
                    q.append(v)
                else:
                    q.appendleft(v)
    print(-1)

def solve1():
    """dij 74ms"""
    n, a, b = RI()
    arr = RILST()
    g = [[] for _ in range(2 * n + 3)]
    for i, v in enumerate(arr, start=1):
        f = sum(x * y for x, y in pt.prime_factorization(v)) % n + 1
        ff = f + n + 1  # 跳到虚拟节点，边权0.5，实际处理边权全部乘2
        g[ff].append((i, 1))
        g[i].append((ff, 1))
        if f <= n:  # 互跳节点
            g[i].append((f, 2))
            g[f].append((i, 2))

    q = [(0, a)]
    dis = [inf] * (2 * n + 3)
    dis[a] = 0
    while q:
        # print(q)
        c, u = heappop(q)
        if c > dis[u]: continue
        if u == b:
            return print(c // 2)
        for v, w in g[u]:
            if c + w < dis[v]:
                dis[v] = c + w
                heappush(q, (c + w, v))

    print(-1)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
