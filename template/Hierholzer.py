"""Hierholzer 算法求一条欧拉回路

求任意欧拉回路，带边：https://leetcode.cn/problems/valid-arrangement-of-pairs/description/
按字典序求欧拉回路，把边堆化或者排序：https://leetcode.cn/problems/reconstruct-itinerary/description/
不会看：https://leetcode.cn/problems/cracking-the-safe/solutions/393529/po-jie-bao-xian-xiang-by-leetcode-solution/
"""


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = defaultdict(list)
        indeg = defaultdict(int)
        for u, v in pairs:
            g[u].append(v)
            indeg[v] += 1
        start = pairs[0][0]
        for k, v in g.items():
            if len(v) > indeg[k]:
                start = k
                break
        ans = []

        def dfs(u):
            while g[u]:
                v = g[u].pop()
                dfs(v)
                ans.append((u, v))

        dfs(start)
        return ans[::-1]
