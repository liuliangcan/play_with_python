"""logtrick  res：{value:cnt} 代表每种值的数量，size是nlogU
如果题目要求一个数组的所有子段的 and_/or_/gcd/lcm，可以使用这个技巧
当固定一个子段端点，另一个端点延伸时，子段的值是单调的，一定只会有logU种变化。
and_:只会减一位，因此最多减logU次
or_:只会增一会，因此最多增logU次
gcd:只会减，且每次最少减半。因此最多减logU次（更紧的界是 欧米伽(U) ，代表这个数质因数指数和）
lcm:只会增，且每次最少乘2。这时需要设置一个上界U，那么也是logU次。

因此整个数组的子段与和只会有nlogU种。且固定一个端点时，是连续的。
可以用一个nlogU大小的字典储存和，且计算有多少个这种段。
具体可以dp转移计算。dp内顺序储存每个值的前后边界，计算后进行区间合并，且利用双指针的写法在原数组上操作。
dp长度不超过logU

-- 20250117 由于存在单调性，有些题可以用技巧滑窗，做到真正的O(n),注意不是按位拆分那种
-- 维护的窗口内，左边是一个栈，在原数组上维护到l到栈底mid的或值；右边是栈底到r的或，这样窗口的或就是两部分计算
    栈的内容可以递推，每次栈没了再建新栈即可，每个数只会进出栈一次，因此是On
https://leetcode.cn/problems/shortest-subarray-with-or-at-least-k-ii/solutions/

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        mid = 0
        ans = inf
        s = 0
        for i, v in enumerate(nums):
            s |= v
            while l <= i and s|nums[l] >= k:
                ans = min(ans, i-l+1)
                l+=1
                if l > mid:
                    for j in range(i-1,l-1,-1):
                        nums[j] |= nums[j+1]
                    mid = i
                    s = 0
        return ans if ans < inf else -1
"""
from collections import defaultdict
from operator import and_
from typing import List


def log_trick_v_cnt(nums: List[int], op=and_):
    """获取nums的所有子段'与值'，返回所有值的个数，共nlogU个。时间复杂度O(nlogU)"""
    res = defaultdict(int)
    dp = []  # 顺序储存 [左边界，右边界),值
    for pos, cur in enumerate(nums):
        for v in dp:
            v[2] = op(v[2], cur)
        dp.append([pos, pos + 1, cur])

        ptr = 0
        for v in dp[1:]:  # 双指针向前合并去重
            if dp[ptr][2] != v[2]:
                ptr += 1
                dp[ptr] = v
            else:
                dp[ptr][1] = v[1]
        # dp = dp[: ptr + 1]
        del dp[ptr + 1:]

        for l, r, v in dp:
            res[v] += r - l

    return res


def log_trick_vs(nums: List[int], op=and_):
    """获取nums的所有子段的'与值'，返回所有值，共nlogU个。由于不计算个数，不需要计算左右边界，因此比上边常数低，快1/3左右---注意会直接修改原数组，可酌情拷贝使用-----"""
    res = set()
    for i, v in enumerate(nums):
        res.add(v)
        for j in range(i - 1, -1, -1):
            if op(nums[j], v) == nums[j]: break
            nums[j] = op(nums[j], v)
            res.add(nums[j])

    return res
