"""
https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/
https://leetcode.cn/problems/maximum-strong-pair-xor-ii/
"""


class TrieXor:
    def __init__(self, nums=None, bit_len=31):
        # 01字典树，用来处理异或最值问题，本模板只处理数字最低的31位
        # 用nums初始化字典树，可以为空
        self.trie = {}
        self.cnt = 0  # 字典树插入了几个值
        if nums:
            for a in nums:
                self.insert(a)
        self.bit_len = bit_len

    def insert(self, num):
        # 01字典树插入一个数字num,只会处理最低bit_len位。
        cur = self.trie
        for i in range(self.bit_len, -1, -1):
            nxt = (num >> i) & 1
            if nxt not in cur:
                cur[nxt] = {}
            cur = cur[nxt]
            cur[3] = cur.get(3, 0) + 1  # 这个节点被经过了几次
        cur[5] = num  # 记录这个数:'#'或者'end'等非01的当key都行;这里由于key只有01因此用5
        self.cnt += 1

    def remove(self, v):
        cur = self.trie
        for i in range(self.bit_len, -1, -1):
            nxt = v >> i & 1
            cur[nxt][3] -= 1  # 3存着计数
            if not cur[nxt][3]:
                del cur[nxt]
                break
            cur = cur[nxt]

    def find_max_xor_num(self, num):
        # 计算01字典树里任意数字异或num的最大值,只会处理最低bit_len位。
        # 贪心的从高位开始处理，显然num的某位是0，对应的优先应取1；相反同理
        cur = self.trie
        res = 0
        for i in range(self.bit_len, -1, -1):
            c = num >> i & 1
            op = c ^ 1  # 有对面的数，这位异或才能是1
            if op in cur:
                cur = cur[op]
                res |= 1 << i
            else:
                cur = cur[c]

        return res

    def count_less_than_limit_xor_num(self, num, limit):
        # 计算01字典树里有多少数字异或num后小于limit
        # 由于计算的是严格小于，因此只需要计算三种情况:
        # 1.当limit对应位是1，且异或值为0的子树部分，全部贡献。
        # 2.当limit对应位是1，且异或值为1的子树部分，向后检查。
        # 3.当limit对应为是0，且异或值为0的子树部分，向后检查。
        # 若向后检查取不到，直接剪枝break
        cur = self.trie
        res = 0
        for i in range(self.bit_len, -1, -1):
            a, b = (num >> i) & 1, (limit >> i) & 1
            if b == 1:
                if a in cur:
                    res += cur[a][3]
                cur = cur.get(a ^ 1)
            else:
                cur = cur.get(a)  # limit是0，因此只需要检查异或和为0的子树
            if not cur: break  # 如果没有相同边的子树，即等于0的子树，可以直接跳出了
        return res

    def kth_xor_num(self, x, k):
        # 计算树里，异或x后的第k小数是谁(k base1)
        cur = self.trie
        res = 0
        for i in range(self.bit_len, -1, -1):
            c = x >> i & 1
            left = cur.get(c, {}).get(3, 0)  # 本位是0的部分
            if k <= left:
                cur = cur[c]
            else:
                cur = cur[c ^ 1]
                k -= left
                res |= 1 << i
        return res
