# Created by Bob at 2023/01/31 17:52
# https://leetcode.cn/problems/he-bing-liang-ge-pai-xu-de-lian-biao-lcof/


"""
剑指 Offer 25. 合并两个排序的链表 (Easy)

输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
**示例1：**
```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```
**限制：**
`0 <= 链表长度 <= 1000`
注意：本题与主站 21 题相同：
[https://leetcode-cn.com/problems/merge-two-sorted-lists/](https://leetcode-cn.com/problems/merge-two-sorted-lists/)
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        x = dummy
        p, q = l1, l2
        while p and q:
            if p.val < q.val:
                x.next = p
                p = p.next
            else:
                x.next = q
                q = q.next
            x = x.next
        while p:
            x.next = p
            p = p.next
            x = x.next
        while q:
            x.next = q
            q = q.next
            x = x.next
        return dummy.next

# @lc code=end
