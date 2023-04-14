# Problem: E. A Bit Similar
# Contest: Codeforces - Educational Codeforces Round 101 (Rated for Div. 2)
# URL: https://codeforces.com/problemset/problem/1469/E
# Memory Limit: 1024 MB
# Time Limit: 2000 ms

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
from math import sqrt, gcd, inf, log2

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://codeforces.com/problemset/problem/1469/E

输入 T(≤1e4) 表示 T 组数据。所有数据的 n 之和 ≤1e6。
每组数据输入 n k(1≤k≤n≤1e6) 和长为 n 的 01 字符串 s。

定义两个长为 k 的字符串 x 和 y「一点点相同」：存在某个下标 i，使得 x[i] = y[i]。
你需要找到一个长为 k 的字典序最小的 01 串 t，使得 t 与 s 的每个长为 k 的子串都「一点点相同」。
如果不存在这样的 t，输出 NO；否则输出 YES 和 t。
"""
"""
输入
7
4 2
0110
4 2
1001
9 3
010001110
9 3
101110001
10 3
0101110001
10 10
1111111111
11 10
11111111110
输出
YES
11
YES
00
YES
010
YES
101
NO
YES
0000000001
YES
0000000010"""
"""https://codeforces.com/contest/1469/submission/201846228

提示 1：设 ~t 为 t 取反后的结果，如果 ~t 在 s 中，那么这个 t 是不合法的。
由于 s 有 n-k+1 个长为 k 的子串，如果 2^k > n-k+1，那么肯定存在 t，使得 ~t 不在这 n-k+1 个子串中。
注：根据 de Bruijn sequence，当 2^k = n-k+1 时，可以构造出这样的字符串，使得这 n-k+1 个子串都互不相同。

提示 2：分类讨论：如果 k 比较小（2^k <= n-k+1），那么 t 可能不存在，此时可以暴力枚举（滑窗）所有长为 k 的子串（转换成 int），存到一个哈希表/数组 set 中，然后从小到大枚举 t，如果 ~t 不在 set 中，那么这个 t 就是答案。（也可以从大到小枚举 ~t，如果 ~t 不在 set 中那么 ~(~t) 就是答案）
如果 k 比较大，那么只需要关心 t 的长为 log2(n) 的后缀填什么，而 t 的长为 k-log2(n) 的前缀全填 0 就行。
做法是在 s 中找 ~t，即先出现 k-log2(n) 个 1，然后把这之后 log2(n) 个字符的 int 值记到 set 中。最后再和上面一样枚举 t 或者 ~t。
统计 1 的个数可以用滑窗。

时间复杂度 O(nlogn)。"""

"""贪心+二进制运算
- 长度为n的字符串里的长为k的子串，最多有min(2^k,n-k+1)种情况。只需要贪心地-依次状压枚举t in range(0,2^k)检查这个t是否合法即可。
    - 检查方案是：对t取反，看看~t是否在s的子串里，那么这个方案就不合法。因为这个t就无法匹配~t这个子串；
    - 否则就合法，因为：
        - 对t来说，任意长度相同的t',有且仅有一个t'和t没有交集，就是~t，其它的都是有交集的。因为每一位上只有01两种情况
- 显然当k足够小时，直接枚举就可以。宽松的判断可以直接if k < 20这样。
---
- 但是当k巨大时，就不能完全枚举了。这时只需要枚举k子串的`长度足够`的尾缀，前边全填0即可。具体是：当2^k>n-k+1时，一定有答案。
    - 这是因为我们能构造2^k个串，这里一定有一个串取反不在s的子串里。因此一定有答案。
- 那么最少枚举多少种情况就一定有答案了呢？设为2^k2=p，要让p>n-k+1才行，p>=n-k+2。最少要p.bit_length()位，记为k2。这是一个较紧的界。
    - 这里k2指尾缀最少要多少位，当然多一点也是可以以的，只要复杂度能过(因为答案要贪心枚举range(2^k2))。
    - 灵神的题解里给了一个较为宽松的界：k2=n.bit_length()-1。在k>log2(n-k+1)的情况下，这个数只会>=p.bit_length()。
    - 但用k2=n.bit_length()-1，需要特判n==1；如果用k2=n.bit_length()，就没有这个问题。
- 当尾缀必有答案时，我们可以让前缀left=k-k2的部分全为0。
    - 这里要注意了，考虑s中每个长为k的子串，如果前半部分left中有0，那么后缀是任意的，完全不会限制后缀的发挥。
    - 因此我们只需考虑这些子串中，前半部分全1的串，只能通过后半部分匹配，看看能得到的最小值是几。
"""

#   374    ms
def solve2():
    n, k = RI()
    s, = RS()
    k2 = (n-k+2).bit_length()
    left = k - k2
    st = set()
    p = 0
    if left <= 0:
        mask = 2 ** k - 1
        for i, c in enumerate(s):
            p = ((p << 1) | int(c)) & mask
            if i + 1 >= k:
                st.add(p)
        for t in range(mask + 1):
            if t ^ mask not in st:
                print('YES')
                ans = bin(t)[2:]
                return print('0' * (k - len(ans)) + ans)
        print('NO')
    else:
        mask = 2 ** k2 - 1
        l = 0
        c1 = 0  # 记录左半部分left里1的个数，必须找到全1的段
        for r, c in enumerate(s):
            p = ((p << 1) | int(c)) & mask  # 记录右半部分的二进制压缩
            m = r - k2  # 左半部分最后一个位置
            if m >= 0:
                c1 += int(s[m])
            if r - l + 1 > k:
                c1 -= int(s[l])
                l += 1
            if m - l + 1 == left == c1:
                st.add(p)
        for t in range(mask + 1):
            if t ^ mask not in st:
                print('YES')
                ans = bin(t)[2:]
                return print('0' * (k - len(ans)) + ans)

#    327   ms
def solve1():
    n, k = RI()
    s, = RS()
    # if n == 1:
    #     print('YES')
    #     return print(int(s[0]))
    k2 = n.bit_length()
    left = k - k2
    st = set()
    p = 0
    if left <= 0:
        mask = 2 ** k - 1
        # print(mask)
        for i, c in enumerate(s):
            p = ((p << 1) | int(c)) & mask
            if i + 1 >= k:
                st.add(p)
        for t in range(mask + 1):
            if t ^ mask not in st:
                print('YES')
                ans = bin(t)[2:]
                return print('0' * (k - len(ans)) + ans)
        print('NO')
    else:
        mask = 2 ** k2 - 1
        l = 0
        c1 = 0  # 记录左半部分left里1的个数，必须找到全1的段
        for r, c in enumerate(s):
            p = ((p << 1) | int(c)) & mask  # 记录右半部分的二进制压缩
            m = r - k2  # 左半部分最后一个位置
            if m >= 0:
                c1 += int(s[m])
            if r - l + 1 > k:
                c1 -= int(s[l])
                l += 1
            if m - l + 1 == left == c1:
                st.add(p)
        for t in range(mask + 1):
            if t ^ mask not in st:
                print('YES')
                ans = bin(t)[2:]
                return print('0' * (k - len(ans)) + ans)


if __name__ == '__main__':
    t, = RI()
    for _ in range(t):
        solve()
