# Problem: 爱睡大觉的小C
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/63602/F
# Memory Limit: 524288 MB
# Time Limit: 2000 ms

import sys
from collections import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
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


#   链式并查集卡常 ms
def solve():
    n, k = RI()
    a = RILST()
    pre, suf = list(range(n + 1)), list(range(n + 2))
    a = [0] + a

    def find(fa, x):
        t = x
        while x != fa[x]:
            x = fa[x]
        while t != x:
            t, fa[t] = fa[t], x
        return x

    def union(fa, x, y):
        x, y = find(fa, x), find(fa, y)
        fa[x] = y
        return y

    def delete(i):
        return union(pre, i, i - 1), union(suf, i, i + 1)

    ans = 0
    for v, i in sorted(zip(a[1:], range(1, n + 1))):
        x, y = delete(i)
        p = []
        for _ in range(k):
            # while x > 0 and a[x] <= v:
            #     x = delete(x)[0]
            if x == 0:
                p.append(0)
                break
            p.append(x)
            x = find(pre, x - 1)

        q = []
        for _ in range(k):
            # 题目保证没有重复元素， 这块是没用的:因为所有<=v的位置已经delete
            # while y <= n and a[y] <= v:
            #     y = delete(y)[1]
            if y > n:
                q.append(n + 1)
                break
            q.append(y)
            y = find(suf, y + 1)

        p = p[::-1] + q
        l = 1
        # c = 0
        if len(p) < k - 3: break  # 没有k-1个大于v的元素
        for j in range(1, len(p) - 1):
            if j - l + 1 > k - 1:
                l += 1
            if j - l + 1 == k - 1:
                ans += v * (min(p[l], i) - p[l - 1]) * (p[j + 1] - max(p[j], i))
        # print(i,v,c,p,q)
        # ans += c * v
    c = 0
    for i in range(k, n + 1):
        c += n - i + 1
    # print(c,((1+n-k+1)*(n-k+1)//2))
    print(f"{ans / c:.2f}")


#   tle    ms
def solve1():
    n, k = RI()
    a = RILST()
    pre, suf = list(range(n + 1)), list(range(n + 2))
    a = [0] + a

    def find(fa, x):
        t = x
        while x != fa[x]:
            x = fa[x]
        while t != x:
            t, fa[t] = fa[t], x
        return x

    def union(fa, x, y):
        x, y = find(fa, x), find(fa, y)
        fa[x] = y
        return y

    def delete(i):
        return union(pre, i, i - 1), union(suf, i, i + 1)

    ans = 0
    for v, i in sorted(zip(a[1:], range(1, n + 1))):
        x, y = delete(i)
        p = []
        for _ in range(k):
            while x > 0 and a[x] <= v:
                x = delete(x)[0]
            if x == 0:
                break
            p.append(x)
            x = find(pre, x - 1)
        if len(p) != k:
            p.append(0)
        q = []
        for _ in range(k):
            while y <= n and a[y] <= v:
                y = delete(y)[1]
            if y > n:
                break
            q.append(y)
            y = find(suf, y + 1)
        if len(q) != k:
            q.append(n + 1)
        p = p[::-1] + q
        dq = deque()
        c = 0
        for j in range(1, len(p) - 1):
            dq.append(j)
            if len(dq) > k - 1:
                dq.popleft()
            if len(dq) == k - 1:
                c += (min(p[dq[0]], i) - p[dq[0] - 1]) * (p[dq[-1] + 1] - max(p[dq[-1]], i))
        # print(i,v,c,p,q)
        ans += c * v
    c = 0
    for i in range(k, n + 1):
        c += n - i + 1
    # print(c,((1+n-k+1)*(n-k+1)//2))
    print(f"{ans / c:.2f}")

# 模拟双链表ac 1186ms
if __name__ == '__main__':
    n, k = RI()
    a = RILST()
    left, right = [0] + list(range(n+1)), list(range(n + 2))[1:]  # left多开1位避免讨论边界
    a = [0] + a


    # def delete(i):
    #     left[right[i]] = left[i]
    #     right[left[i]] = right[i]


    ans = 0
    for v, i in sorted(zip(a[1:], range(1, n + 1))):
        l, r = left[i], right[i]
        p = []
        for _ in range(k):
            if l == 0:
                p.append(0)
                break
            p.append(l)
            l = left[l]
        q = []
        for _ in range(k):
            if r > n:
                q.append(n + 1)
                break
            q.append(r)
            r = right[r]
        # delete(i)
        left[right[i]] = left[i]
        right[left[i]] = right[i]
        p = p[::-1] + q
        l = 1
        # c = 0
        for j in range(1, len(p) - 1):
            if j - l + 1 > k - 1:
                l += 1
            if j - l + 1 == k - 1:
                # lt = p[l] if p[l] < i else i
                # rt = p[j] if p[j] > i else i
                ans += v * (min(p[l], i) - p[l - 1]) * (p[j + 1] - max(p[j], i))

        # ans += c * v
    # c = 0
    # for i in range(k, n + 1):
    #     c += n - i + 1
    # print(c,((1+n-k+1)*(n-k+1)//2))
    print(f"{ans / ((1 + n - k + 1) * (n - k + 1) // 2):.2f}")
