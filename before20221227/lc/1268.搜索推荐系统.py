""" 题目
1268. 搜索推荐系统
给你一个产品数组 products 和一个字符串 searchWord ，products  数组中每个产品都是一个字符串。

请你设计一个推荐系统，在依次输入单词 searchWord 的每一个字母后，推荐 products 数组中前缀与 searchWord 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。

请你以二维列表的形式，返回在输入 searchWord 每个字母后相应的推荐产品的列表。



示例 1：

输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
输出：[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
解释：按字典序排序后的产品列表是 ["mobile","moneypot","monitor","mouse","mousepad"]
输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 ["mobile","moneypot","monitor"]
输入 mou， mous 和 mouse 后系统都返回 ["mouse","mousepad"]
示例 2：

输入：products = ["havana"], searchWord = "havana"
输出：[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
示例 3：

输入：products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
输出：[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
示例 4：

输入：products = ["havana"], searchWord = "tatiana"
输出：[[],[],[],[],[],[],[]]


提示：

1 <= products.length <= 1000
1 <= Σ products[i].length <= 2 * 10^4
products[i] 中所有的字符都是小写英文字母。
1 <= searchWord.length <= 1000
searchWord 中所有字符都是小写英文字母。
"""

""" 题解
字典树，每次查找前缀为word的前三个数据
把word前缀切片
"""

from typing import List
from bisect import *


class TrieNode:
    def __init__(self, cnt=0):
        self.cnt = cnt
        self.next = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            i = ord(c) - ord('a')
            if not cur.next[i]:  # 没有这个字符
                cur.next[i] = TrieNode()
            cur = cur.next[i]
            cur.cnt += 1
        cur.is_end = True

    def find(self, word):
        ans = []
        cur = self
        now_word = ''
        for c in word:
            now_word += c
            i = ord(c) - ord('a')
            if not cur.next[i]:
                return ans
            cur = cur.next[i]

        def dfs(root, now_word):
            if len(ans) >= 3:
                return ans
            if root.is_end:
                ans.append(now_word)
            for i in range(26):
                c = chr(ord('a') + i)
                if root.next[i]:
                    dfs(root.next[i], now_word + c)

        dfs(cur, now_word)
        return ans


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = TrieNode()
        for product in products:
            trie.insert(product)

        ans = []
        for i in range(len(searchWord)):
            ans.append(trie.find(searchWord[:i + 1]))

        from sortedcontainers import SortedList
        a = SortedList()
        return ans


if __name__ == '__main__':
    rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    print(Solution().rectangleArea(rectangles))