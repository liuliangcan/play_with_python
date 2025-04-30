import random
from collections import defaultdict

"""给你一个整数数组a和整数k，请你统计有多少个子数组满足“子数组的最大值至少出现k次”
"""


def solve1(a, k):  # n方暴力
    n = len(a)
    ans = 0
    for l in range(n):
        mx = a[l]
        cnt = 0
        for r in range(l, n):
            if a[r] == mx:
                cnt += 1
            elif a[r] > mx:
                mx = a[r]
                cnt = 1
            if cnt >= k:
                ans += 1
    return ans


def solve2(a, k):  # 单调栈+乘法原理
    n = len(a)
    pos = defaultdict(list)
    left = [-1] * n
    st = []
    for i, v in enumerate(a):
        pos[v].append(i)
        while st and a[st[-1]] <= v:
            st.pop()
        if st:
            left[i] = st[-1]
        st.append(i)
    right = [n] * n
    st = []
    for i, v in enumerate(a):
        while st and a[st[-1]] < v:
            right[st.pop()] = i
        st.append(i)
    ans = 0
    for v, p in pos.items():
        if len(p) < k: continue
        p = [left[p[0]]] + p
        l = 1
        for r in range(k, len(p)):
            if left[p[l]] == left[p[r]] and right[p[l]] == right[p[r]]:
                ans += (p[l] - max(p[l - 1], left[p[l]])) * (right[p[r]] - p[r])
            l += 1
    return ans


def solve3(a, k): # 单调栈+乘法原理
    ans = 0
    a.append(max(a)+1)  # 增加哨兵，由于是出栈贡献，防止最大值遍历不到。
    st = [-1]  # 哨兵，维护单掉不升栈，栈顶如果有k个连续相同，可以贡献它
    for i, v in enumerate(a):
        while len(st) > 1 and a[st[-1]] < v:
            j = st[-1]
            if len(st) > k and a[st[-k]] == a[j]:
                ans += (st[-k] - st[-k-1]) * (i - j)
            st.pop()
        st.append(i)
    return ans


# a = [1, 2]
# k = 1
# print(solve2(a, k))
# print(solve3(a, k))
MX = 100000
for _ in range(1000):
    n = random.randint(1, MX)
    k = random.randint(1, n)
    a = [random.randint(1, MX) for _ in range(n)]

    if solve2(a, k) != solve3(a, k):
        print(n, k)
        print(a)
        print(solve2(a, k))
        print(solve3(a, k))
"""
1 1 1 1 0 1 1

输出
2 
"""
