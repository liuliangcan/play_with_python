# Problem: F. Copy or Prefix Sum
# Contest: Codeforces - Codeforces Round 701 (Div. 2)
# URL: https://codeforces.com/problemset/problem/1485/F
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
from collections import *

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1485/F

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤2e5。
每组数据输入 n(≤2e5) 和长为 n 的数组 b(-1e9≤b[i]≤1e9)，下标从 1 开始。

构造下标从 1 开始的数组 a，对于每个 i，满足 b[i] = a[i] 或者 b[i] = a[1] + a[2] + ... + a[i]。
输出有多少个不同的 a，模 1e9+7。
输入
4
3
1 -1 1
4
1 2 3 4
10
2 -1 1 -2 2 3 -5 0 2 -1
4
0 0 0 1
输出
3
8
223
1
"""
"""https://codeforces.com/contest/1485/submission/202820084

提示 1：两个 a 不同，当且仅当这两个 a 的前缀和不同。那么考虑 a 的前缀和有多少不同的。

提示 2：设 a 的前缀和为 s，则有：
s1 = a1 = b1
s2 = s1 + a2 = b2 或 s1 + b2
s3 = s2 + a3 = b3 或 s2 + b3
……
画出的分支图以及样例一见右。注意对于样例一，b3=b1+b2+b3，所以下面只有一个分支

提示 3：定义 f[i] 表示从 a[i] 开始的不同后缀的个数。
右图最左边的 1 这棵树就是 f[1]，-1 这棵树就表示 f[2]，右下的 1 这棵树就表示 f[3]。
设 j 是最小的满足 a[i] + ... + a[j-1] = 0 的下标，那么
f[i] = f[i+1] + ... + f[j]
如果 j 不存在，那么
f[i] = f[i+1] + ... f[n] + 1
所以，记录 a 的后缀和的位置信息，可以算出 j。记录 f 的后缀和，可以 O(1) 算出 f[i]。
答案为 f[1]。"""
"""
- 每个a[i]有两种情况:
    1. ai = bi
    2. ai = bi - sum,   其中sum = sum(a[:i])
- 若每个位置都有两种情况，最终构造的数组有2^n种。
- 然而当sum=0时，ai只有一种情况。需要特殊处理sum
- sum每次要么变成bi;要么+=bi
---
- 记f[s]代表当前和为s的方案数。对每个v in b 有：
    - f[s+v] = f[s]   , ai位置填v,sum+=v,这时要对应增长
    - f[v] = sum(f)   , ai位置填v-s,sum=v,这时无论前边是啥都可以，因此f[v]=sum(f)
- 记ans = sum(f)，那么每次转移后，ans=sum(f)*2-f[0](重复的部分),s==0时，加v和直接填v是一样的，去掉一次。
"""
"""https://www.luogu.com.cn/blog/doubeecat/solution-cf1485f"""

#   264    ms
def solve():
    n, = RI()
    b = RILST()
    f = Counter([0])  # cnt[s]代表遍历到当前数字时，前缀和为s时的方案数
    s = 0  # f下标的移位
    ans = 1
    for v in b:
        t = f[s]  # f[s]其实是f[0]因为下标整体偏移了s
        f[s] = ans
        s += v
        ans = (ans+ans-t)%MOD
    print(ans)


#   155    ms
def solve1():
    n, = RI()
    b = RILST()
    cnt = Counter([0])  # cnt[s]代表遍历到当前数字时，前缀和为s时的方案数
    total_add = 0  # 全局移位，即每个s都加上
    ans = 1
    for v in b:
        t = (ans - cnt[total_add]) % MOD  # t 表示 i-1 的所有方案中 sum 不为 0 的情形 对应两种世界线都可以走的情况
        cnt[total_add] += t  # 因为之后 bi 会加到 total_add 上 所以此处对应 sum 直接变成 bi 的情况。
        ans = (ans + t) % MOD
        total_add += v  # 本来的情况直接加上 bi 的情形
    print(ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
