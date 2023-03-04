# Problem: 异或值
# Contest: AcWing
# URL: https://www.acwing.com/problem/content/4872/
# Memory Limit: 256 MB
# Time Limit: 1000 ms

import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """
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
        for i in range(self.bit_len - 1, -1, -1):
            nxt = (num >> i) & 1
            if nxt not in cur:
                cur[nxt] = {}
            cur = cur[nxt]
            cur[3] = cur.get(3, 0) + 1  # 这个节点被经过了几次
        cur[5] = num  # 记录这个数:'#'或者'end'等非01的当key都行;这里由于key只有01因此用5
        self.cnt += 1

    def find_max_xor_num(self, num):
        # 计算01字典树里任意数字异或num的最大值,只会处理最低bit_len位。
        # 贪心的从高位开始处理，显然num的某位是0，对应的优先应取1；相反同理
        cur = self.trie
        ret = 0
        for i in range(self.bit_len - 1, -1, -1):
            if (num >> i) & 1 == 0:  # 如果本位是0，那么取1才最大；取不到1才取0
                if 1 in cur:
                    cur = cur[1]
                    ret += ret + 1
                else:
                    cur = cur.get(0, {})
                    ret <<= 1
            else:
                if 0 in cur:
                    cur = cur[0]
                    ret += ret + 1
                else:
                    cur = cur.get(1, {})
                    ret <<= 1
        return ret

    def find_max_xor_any(self):
        """计算所有数字异或异或同一数字x时，结果里max的最小值"""

        def dfs(cur, bit):  # 计算当前层以下能取到的最小的最大值
            if bit < 0:
                return 0
            if 0 not in cur:  # 如果这层都是1，那么可以使x的这层是1，结果里的这层就是0，递归下一层即可。
                return dfs(cur[1], bit - 1)
            elif 1 not in cur:  # 如果这层都是0，使x这层是0，递归下一层。
                return dfs(cur[0], bit - 1)
            # 如果01都有，那么x这层不管是几，结果最大值里这层都是1，那么考虑走1还是走0方向，取min后加上本层的值。
            return min(dfs(cur[0], bit - 1), dfs(cur[1], bit - 1)) + (1 << bit)

        return dfs(self.trie, self.bit_len - 1)

    def count_less_than_limit_xor_num(self, num, limit):
        # 计算01字典树里有多少数字异或num后小于limit
        # 由于计算的是严格小于，因此只需要计算三种情况:
        # 1.当limit对应位是1，且异或值为0的子树部分，全部贡献。
        # 2.当limit对应位是1，且异或值为1的子树部分，向后检查。
        # 3.当limit对应为是0，且异或值为0的子树部分，向后检查。
        # 若向后检查取不到，直接剪枝break
        cur = self.trie
        ans = 0
        for i in range(self.bit_len - 1, -1, -1):
            a, b = (num >> i) & 1, (limit >> i) & 1
            if b == 1:
                if a == 0:
                    if 0 in cur:  # 右子树上所有值异或1都是0，一定小于1
                        ans += cur[0][3]
                    cur = cur.get(1)  # 继续检查右子树
                    if not cur: break  # 如果没有1，即没有右子树，可以直接跳出了
                if a == 1:
                    if 1 in cur:  # 右子树上所有值异或1都是0，一定小于1
                        ans += cur[1][3]
                    cur = cur.get(0)  # 继续检查左子树
                    if not cur: break  # 如果没有0，即没有左子树，可以直接跳出了
            else:
                cur = cur.get(a)  # limit是0，因此只需要检查异或和为0的子树
                if not cur: break  # 如果没有相同边的子树，即等于0的子树，可以直接跳出了
        return ans


#    封装成类卡常真是吐了   ms
def solve_tle():
    n, = RI()
    a = RILST()
    trie = TrieXor(bit_len=30)
    for x in a:
        trie.insert(x)
    ans = trie.find_max_xor_any()
    print(ans)


#   7224    ms
def solve1():
    n, = RI()
    a = RILST()
    trie = {}
    for x in a:
        cur = trie
        for i in range(29, -1, -1):
            nxt = (x >> i) & 1
            if nxt not in cur:
                cur[nxt] = {}
            cur = cur[nxt]

    def dfs(cur, bit):  # 计算当前层以下能取到的最小的最大值
        if bit < 0:
            return 0
        if 0 not in cur:  # 如果这层都是1，那么可以使x的这层是1，结果里的这层就是0，递归下一层即可。
            return dfs(cur[1], bit - 1)
        elif 1 not in cur:  # 如果这层都是0，使x这层是0，递归下一层。
            return dfs(cur[0], bit - 1)
        # 如果01都有，那么x这层不管是几，结果最大值里这层都是1，那么考虑走1还是走0方向，取min后加上本层的值。
        return min(dfs(cur[0], bit - 1), dfs(cur[1], bit - 1)) + (1 << bit)

    ans = dfs(trie, 29)
    print(ans)


#     1725   ms
def solve():
    n, = RI()
    a = RILST()

    def dfs(a, bit):  # 计算当前层以下能取到的最小的最大值
        if bit < 0:
            return 0
        x, y = [], []
        t = 1 << bit
        for v in a:
            if v & t:
                x.append(v)
            else:
                y.append(v)
        if not x: return dfs(y, bit - 1)
        if not y: return dfs(x, bit - 1)
        # 如果01都有，那么x这层不管是几，结果最大值里这层都是1，那么考虑走1还是走0方向，取min后加上本层的值。
        return min(dfs(x, bit - 1), dfs(y, bit - 1)) + t

    print(dfs(a, 29))


if __name__ == '__main__':
    solve()
