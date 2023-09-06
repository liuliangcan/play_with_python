# Problem: D - Two Sequences
# Contest: AtCoder - AtCoder Regular Contest 092
# URL: https://atcoder.jp/contests/arc092/tasks/arc092_b
# Memory Limit: 256 MB
# Time Limit: 3000 ms
import gc
import sys
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
PROBLEM = """https://atcoder.jp/contests/arc092/tasks/arc092_b

输入 n(1≤n≤2e5) 和两个长为 n 的数组 a b，元素范围在 [0,2^28)。
从 a 中选一个数 a[i]，从 b 中选一个数 b[j]，相加得到 a[i]+b[j]。这一共有 n^2 个数字。
输出这 n^2 个数的异或和。
输入
2
1 2
3 4
输出 2

输入
6
4 6 0 0 3 3
0 5 6 5 0 3
输出 8

输入
5
1 2 3 4 5
1 2 3 4 5
输出 2

输入
1
0
0
输出 0
"""
"""二进制题目，常用技巧之一是拆位，但这只能用于各个比特位互相独立的情况。
本题加法有进位，破坏了这种独立性，这要如何处理呢？

其实也可以拆位（我叫它加法拆位）。
按照 mod (2^k) 拆位，例如要计算从低到高第三个比特位，可以 mod 8（即 AND 7）。

记 s = a[i]%8 + b[j]%8。
要想知道这 n^2 个 s 中，从低到高第三个比特位有多少个 1，相当于求满足下式的 s 的个数：
100 <= s <= 111 或 1100 <= s <= 1111（数字为二进制）。
这可以在按照 mod 8 排序后，用五个指针做。一个指针遍历 a[i]，另外 4 个指针在 b 上，对应着上式的 4 个区间端点。

注意：相加可能会进位到第 29 个比特位，在枚举的时候请注意上界。

https://atcoder.jp/contests/arc092/submissions/44922461 


优化：
注意到 s <= 1<<(k+2)-1 是恒成立的，上面代码中的 q 恒等于 n-1。
而 n 个 n-1 的异或和一定是偶数（最低位一定是 0），所以可以完全去掉 q。

优化后 https://atcoder.jp/contests/arc092/submissions/44922567"""


#   2445    ms
def solve():
    n, = RI()
    a = RILST()
    b = RILST()
    ans = 0
    for k in range(29):
        gc.collect()  # 不加这句会MLE
        mask = (1 << (k + 1)) - 1
        a.sort(key=lambda x: x & mask)
        b.sort(key=lambda x: x & mask)
        cnt = 0
        i = j = p = q = n - 1
        l1, r1, l2, r2 = 1 << k, (1 << (k + 1)) - 1, 3 << k, (1 << (k + 2)) - 1
        for v in a:
            while i >= 0 and (v & mask) + (b[i] & mask) >= l1: i -= 1
            while j >= 0 and (v & mask) + (b[j] & mask) > r1: j -= 1
            while p >= 0 and (v & mask) + (b[p] & mask) >= l2: p -= 1
            while q >= 0 and (v & mask) + (b[q] & mask) > r2: q -= 1
            cnt ^= i ^ j ^ p ^ q  # cnt += j-i+p-q
        ans |= (cnt & 1) << k
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
