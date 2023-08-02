# Created by Bob at 2023/08/02 17:46
# https://leetcode.cn/problems/binary-tree-postorder-traversal/

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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        st = [root]
        while st:
            o = st.pop()
            ans.append(o.val)
            if o.left:
                st.append(o.left)
            if o.right:
                st.append(o.right)
        return ans[::-1]


# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().postorderTraversal(root)
    print("output:", serialize(ans))
