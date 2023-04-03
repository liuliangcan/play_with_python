# Created by Bob at 2023/04/03 15:36
# https://leetcode.cn/problems/minimum-reverse-operations/

"""
2612. 最少翻转操作数 (Hard)
给你一个整数 `n` 和一个在范围 `[0, n - 1]` 以内的整数 `p` ，它们表示一个长度为 `n` 且下标从
**0** 开始的数组 `arr` ，数组中除了下标为 `p` 处是 `1` 以外，其他所有数都是 `0` 。

同时给你一个整数数组 `banned` ，它包含数组中的一些位置。 `banned` 中第 **i** 个位置表示
`arr[banned[i]] = 0` ，题目保证 `banned[i] != p` 。

你可以对 `arr` 进行 **若干次** 操作。一次操作中，你选择大小为 `k` 的一个 **子数组** ，并将它
**翻转** 。在任何一次翻转操作后，你都需要确保 `arr` 中唯一的 `1` 不会到达任何 `banned`
中的位置。换句话说， `arr[banned[i]]` 始终 **保持** `0` 。

请你返回一个数组 `ans` ，对于 `[0, n - 1]` 之间的任意下标 `i` ， `ans[i]` 是将
`1` 放到位置 `i` 处的 **最少** 翻转操作次数，如果无法放到位置 `i` 处，此数为 `-1` 。

- **子数组** 指的是一个数组里一段连续 **非空** 的元素序列。
- 对于所有的 `i` ， `ans[i]` 相互之间独立计算。
- 将一个数组中的元素 **翻转** 指的是将数组中的值变成 **相反顺序** 。

**示例 1：**

```
输入：n = 4, p = 0, banned = [1,2], k = 4
输出：[0,-1,-1,1]
解释：k = 4，所以只有一种可行的翻转操作，就是将整个数组翻转。一开始 1 在位置 0 处，所以将它翻转到位置 0
处需要的操作数为 0 。
我们不能将 1 翻转到 banned 中的位置，所以位置 1 和 2 处的答案都是 -1 。
通过一次翻转操作，可以将 1 放到位置 3 处，所以位置 3 的答案是 1 。

```

**示例 2：**

```
输入：n = 5, p = 0, banned = [2,4], k = 3
输出：[0,-1,-1,-1,-1]
解释：这个例子中 1 一开始在位置 0 处，所以此下标的答案为 0 。
翻转的子数组长度为 k = 3 ，1 此时在位置 0 处，所以我们可以翻转子数组 [0, 2]，但翻转后的下标 2 在
banned 中，所以不能执行此操作。
由于 1 没法离开位置 0 ，所以其他位置的答案都是 -1 。

```

**示例 3：**

```
输入：n = 4, p = 2, banned = [0,1,3], k = 1
输出：[-1,-1,0,-1]
解释：这个例子中，我们只能对长度为 1 的子数组执行翻转操作，所以 1 无法离开初始位置。

```

**提示：**

- `1 <= n <= 10⁵`
- `0 <= p <= n - 1`
- `0 <= banned.length <= n - 1`
- `0 <= banned[i] <= n - 1`
- `1 <= k <= n `
- `banned[i] != p`
- `banned` 中的值 **互不相同** 。
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


class DSU:
    def __init__(self, n):
        self.fathers = list(range(n))
        self.size = [1] * n  # 本家族size
        self.edge_size = [0] * n  # 本家族边数(带自环/重边)
        self.n = n
        self.setCount = n  # 共几个家族

    def find_fa(self, x):
        fs = self.fathers
        t = x
        while fs[x] != x:
            x = fs[x]
        while t != x:
            fs[t], t = x, fs[t]
        return x

    def union(self, x: int, y: int) -> bool:
        x = self.find_fa(x)
        y = self.find_fa(y)

        if x == y:
            self.edge_size[y] += 1
            return False
        # if self.size[x] > self.size[y]:  # 注意如果要定向合并x->y，需要干掉这个；实际上上边改成find_fa后，按轶合并没必要了，所以可以常关
        #     x, y = y, x
        self.fathers[x] = y
        self.size[y] += self.size[x]
        self.edge_size[y] += 1 + self.edge_size[x]
        self.setCount -= 1
        return True


class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        ans = [-1] * n
        ans[p] = 0
        if k == 1:
            return ans
        if k == n:
            if p != n - 1 - p and n - 1 - p not in banned:
                ans[n - 1 - p] = 1
            return ans
        dsu = DSU(n + 2)
        for x in banned:
            dsu.union(x, x + 2)

        dsu.union(p, p + 2)
        q = deque([p])
        while q:
            u = q.popleft()
            d = ans[u] + 1
            mn = max(u - k + 1, k - u - 1)
            mx = min(u + k - 1, 2 * n - k - 1 - u)

            while mn <= mx:
                mn = dsu.find_fa(mn)
                if mn <= mx:
                    ans[mn] = d
                    q.append(mn)
                    dsu.union(mn, mn + 2)
                    mn += 2

        # s = [SortedList(range(0, n, 2)), SortedList(range(1, n, 2))]
        # s[0].discard(p)
        # s[1].discard(p)
        # for x in banned:
        #     s[0].discard(x)
        #     s[1].discard(x)
        # q = deque([p])
        # while q:
        #     u = q.popleft()
        #     d = ans[u] + 1
        #     mn = max(u - k + 1, k - u - 1)
        #     mx = min(u + k - 1, 2 * n - k - 1 - u)
        #     p = s[mn & 1]
        #     l, r = p.bisect_left(mn), p.bisect_right(mx)
        #     t = p[l:r]
        #     for x in t:
        #         ans[x] = d
        #         q.append(x)
        #         p.remove(x)
        return ans

# @lc code=end
