# Created by Bob at 2023/01/30 08:30
# https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/

"""
剑指 Offer 24. 反转链表 (Easy)

定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
**示例:**
```
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```
**限制：**
`0 <= 节点个数 <= 5000`
**注意**：本题与主站 206 题相同：
[https://leetcode-cn.com/problems/reverse-linked-list/](https://leetcode-cn.com/problems/reverse-linked-list/)
"""


# @lc code=begin

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(1)
        while head:
            p = head
            head = head.next
            p.next = dummy.next
            dummy.next = p
        return dummy.next

# @lc code=end
