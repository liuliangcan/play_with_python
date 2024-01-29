"""试填法：位运算贪心
存在这么一种题：题目运算有明显的位运算特征，最终询问一个满足条件的数字的“最大”或“最小”。
但这题又可能无法简单的拆位处理，每位之间并不完全独立。或者运算跟次数有关。如：
    运算时，两个数整体运算，对贡献是有影响的（比如运算一次，每个位都变了，限制是运算次数），那么这题可能无法简单拆位处理。
这时可以考虑用试填法：从高位开始试填。题目就变成了如何验证。有的题目不一定有明显的验证性质，需要转化。
若问最大化：那么通常初始化ans为0，从最高位开始尝试填1，并用当前答案验证，若可以则填1否则填0.
若问最小化：通常mask=(1<<logU)-1，初始化ans为mask,从最高位开始尝试填0。
时间复杂度通常是O(nlogU),其中n是验证时间

最小化：https://leetcode.cn/problems/minimize-or-of-remaining-elements-using-operations/description/
最大化：
    https://codeforces.com/contest/1721/submission/189632358
    https://codeforces.com/problemset/problem/981/D
"""

# https://leetcode.cn/problems/minimize-or-of-remaining-elements-using-operations/description/
class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:
        mask = (1 << 30) - 1
        n = len(nums)

        def check(p):
            cnt = 0
            s = mask
            for v in nums:
                s &= v
                if (s & p) == s:
                    cnt += 1
                    s = mask
                    if cnt >= n - k:
                        return True
            return False

        ans = mask
        for i in range(29, -1, -1):
            p = ans ^ (1 << i)
            if check(p):
                ans = p
        return ans

# https://codeforces.com/contest/1721/submission/189632358
def solve():
    n, = RI()
    a = RILST()
    b = RILST()

    def ok(mask):
        cnt = Counter()
        for v in a:
            cnt[v & mask] += 1
        for v in b:
            cnt[~v & mask] -= 1
        return all(v == 0 for v in cnt.values())

    ans = 0
    for k in range(29, -1, -1):
        p = ans | (1 << k)
        if ok(p):
            ans = p

    print(ans)