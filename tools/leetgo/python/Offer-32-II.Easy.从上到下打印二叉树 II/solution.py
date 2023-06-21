# Created by Bob at 2023/06/21 15:58
# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/

from typing import *
from leetgo_py import *
from bisect import *
from collections import *
from heapq import *
from typing import List
from itertools import *
from math import inf
from functools import cache

# @lc code=begin
from sortedcontainers import SortedList

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = [root]
        while q:
            nq = []
            cur = []
            for u in q:
                cur.append(u.val)
                if u.left:
                    nq.append(u.left)
                if u.right:
                    nq.append(u.right)
            ans.append(cur)
            q = nq
        return ans



# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrder(root)
    print("output:", serialize(ans))
