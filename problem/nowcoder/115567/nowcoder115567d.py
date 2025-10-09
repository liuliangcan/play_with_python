# Problem: 中位数+2
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/115567/D
# Memory Limit: 2048 MB
# Time Limit: 4000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())


class XorBasisQuick:
    """贪心法构造线性基，基于每个高位计算"""

    def __init__(self):
        self.b = []
        self.gauss = 0  # 前gauss个已经做过高斯消元

    def insert(self, x):
        for v in self.b:
            if x ^ v < x:
                x ^= v
        if x:
            self.b.append(x)

    def can_present(self, x):
        for v in self.b:
            x = min(x, x ^ v)
        return x == 0

    def find_max_xor(self):  # 这个很慢
        if self.gauss < len(self.b):
            self.do_gauss()
        res = 0
        for v in self.b:
            res ^= v
        return res

    def do_gauss(self):
        b = self.b
        n = len(b)
        for i in range(self.gauss, n):
            for j in range(i):
                # b[j] = min(b[j], b[j] ^ b[i])
                if b[j] ^ b[i] < b[j]:
                    b[j] ^= b[i]
        b.sort()
        self.gauss = n

    def kth(self, k):
        b = self.b
        if 1 << len(b) < k:
            return -1
        if self.gauss < len(b):
            self.do_gauss()
        k -= 1
        ans = 0
        for i, v in enumerate(b):
            if k >> i & 1:
                ans ^= v
        return ans


#       ms
def solve():
    n, = RI()
    a = RILST()
    xb = XorBasisQuick()
    for v in a:
        xb.insert(v)
    mid = (1 << len(xb.b)) // 2 + 1
    print(xb.kth(mid))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
