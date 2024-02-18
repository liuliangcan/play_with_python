import random

class StringHash:
    """字符串哈希，用O(n)时间预处理，用O(1)时间获取段的哈希值"""
    def __init__(self, s):
        n = len(s)
        self.BASE = BASE = 131+random.randint(37, 100)  # 进制 131,131313
        self.MOD = MOD = 10 ** 9 + random.randint(7, 10000)  # 10**9+7,998244353,10**13+7
        self.h = h = [0] * (n + 1)
        self.p = p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * BASE) % MOD
            h[i] = (h[i - 1] * BASE % MOD + ord(s[i - 1])) % MOD

    def get_hash(self, l, r):
        """用O(1)时间获取开区间[l,r)（即s[l:r]）的哈希值"""
        return (self.h[r] - self.h[l] * self.p[r - l] % self.MOD) % self.MOD

    # # 用O(1)时间获取开区间[l,r)（即s[l:r]）的哈希值
    # def __getitem__(self, index):
    #     if isinstance(index, slice):
    #         l, r, step = index.indices(len(self.h)-1)
    #         if step != 1:
    #             raise Exception('StringHash slice 步数仅限1'+str(index))
    #         return (self.h[r] - self.h[l] * self.p[r - l] % self.MOD) % self.MOD
    #     else:
    #         return (self.h[index+1] - self.h[index] * self.p[index+1 - index] % self.MOD) % self.MOD