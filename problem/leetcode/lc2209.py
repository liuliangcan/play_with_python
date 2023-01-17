from collections import deque
from heapq import *
from itertools import accumulate
from typing import List


# https://leetcode.cn/problems/minimum-white-tiles-after-covering-with-carpets/
class Solution:
    def minimumWhiteTiles(self, floor: str, k: int, w: int) -> int:
        floor = list(map(int, floor))
        n = len(floor)
        r = [0] * n
        q = deque()
        s = 0
        for i, v in enumerate(floor):
            q.append(i)
            s += v
            while i - q[0] >= w:
                s -= floor[q.popleft()]
            r[i] = s
        f = list(accumulate(r, max))
        for j in range(1, k):
            g = f[:]
            for i in range(j * w, n):
                g[i] = max(g[i - 1], f[i - w] + r[i])
            f = g

        return floor.count(1) - max(f)


"""滑窗+dp
先用滑窗计算出以i为右端点的单个地毯能盖几个白块，记作r[i]。补充：滑窗个p，前缀和就可以了。
定义：令f[i][j]为用了i张地毯，前i个块能覆盖的最多的白块。
转移：考虑最后一张地毯的位置，显然f[i][j] = f[i-1][j-w] + r[j]
答案：最多能覆盖的白块为max(f[-1])
初始：一开始都是0，可以右移一位优化，我这里提前计算了只用单张的，而后续的不会访问f[-1],因此不用右移。
实现时用滚动数组优化。
"""
floor = "10110101"
numCarpets = 2
carpetLen = 2
assert Solution().minimumWhiteTiles(floor, numCarpets, carpetLen) == 2

floor = "11111"
numCarpets = 2
carpetLen = 3
assert Solution().minimumWhiteTiles(floor, numCarpets, carpetLen) == 0

floor = "0001000000000000000010000010000000001000000000001010000000000000000000101001000100000010001000"
numCarpets = 7
carpetLen = 1
assert Solution().minimumWhiteTiles(floor, numCarpets, carpetLen) == 5
