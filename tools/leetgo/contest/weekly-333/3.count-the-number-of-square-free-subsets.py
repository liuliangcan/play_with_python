# Created by Bob at 2023/02/19 10:30
# https://leetcode.cn/problems/count-the-number-of-square-free-subsets/
# https://leetcode.cn/contest/weekly-contest-333/problems/count-the-number-of-square-free-subsets/

"""
6364. 无平方子集计数 (Medium)

给你一个正整数数组 `nums` 。

如果数组 `nums` 的子集中的元素乘积是一个 **无平方因子数** ，则认为该子集是一个 **无平方** 子集。

**无平方因子数** 是无法被除 `1` 之外任何平方数整除的数字。

返回数组 `nums` 中 **无平方** 且 **非空** 的子集数目。因为答案可能很大，返回对 `10⁹ + 7`
取余的结果。

`nums` 的 **非空子集** 是可以由删除 `nums`
中一些元素（可以不删除，但不能全部删除）得到的一个数组。如果构成两个子集时选择删除的下标不同，则认为这两个子集不同。

**示例 1：**

```
输入：nums = [3,4,4,5]
输出：3
解释：示例中有 3 个无平方子集：
- 由第 0 个元素 [3] 组成的子集。其元素的乘积是 3 ，这是一个无平方因子数。
- 由第 3 个元素 [5] 组成的子集。其元素的乘积是 5 ，这是一个无平方因子数。
- 由第 0 个和第 3 个元素 [3,5] 组成的子集。其元素的乘积是 15 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 3 个无平方子集。
```

**示例 2：**

```
输入：nums = [1]
输出：1
解释：示例中有 1 个无平方子集：
- 由第 0 个元素 [1] 组成的子集。其元素的乘积是 1 ，这是一个无平方因子数。
可以证明给定数组中不存在超过 1 个无平方子集。
```

**提示：**

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 30`
"""

from bisect import *
from collections import *
from heapq import *
from typing import List

# @lc code=begin
from sortedcontainers import SortedList
PRIMES = 2,3,5,7,11,13,17,19,23,29
NSQ_TO_MASK = [0]*31  # 把2-30每个数都转化成它的质因子表示的位掩码
for i in range(2,31):
    for j, p in enumerate(PRIMES):
        if i % p == 0:
            if i%(p*p) == 0:  # 如果含有平方因子则标记为否
                NSQ_TO_MASK[i] = -1
                break
            NSQ_TO_MASK[i] |= 1<<j
MOD = 10**9+7
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        cnt = Counter(nums)  # 计数
        M = 1 << len(PRIMES)  # 掩码能组成状态的范围
        f = [0] * M  # 每个状态的种类
        f[0] = 1  # 空方案数为1
        for x, c in cnt.items():  # 虽然是全部枚举，但是1的mask是0因此会跳过
            mask = NSQ_TO_MASK[x]  # 取出掩码
            if mask > 0:  # x是nsq
                other = (M-1)^mask  # mask的补集
                j = other  # 下面这一段是标准的枚举other补集(包括空集)的代码
                while True:
                    f[j|mask] += f[j]*c  # 补集加j的状态数应该累加上j的状态数
                    f[j|mask] %= MOD
                    j = (j-1)&other
                    if j == other:break  # 由于是含空集，j会到0然后-1(二进制是全集)，&other就==other
        ans = sum(f)*pow(2,cnt[1],MOD) - 1  # -1去掉空集
        return ans % MOD

# @lc code=end
