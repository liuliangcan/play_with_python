# Created by Bob at 2023/06/21 15:55
# https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/

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
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            u = q.popleft()
            ans.append(u.val)
            if u.left:
                q.append(u.left)
            if u.right:
                q.append(u.right)
        return ans


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().levelOrder(root)
    print("output:", serialize(ans))
