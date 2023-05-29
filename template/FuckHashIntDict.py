"""
由于CF会有老哥精心构造数据卡哈希，即输入为int时，构造int序列发生大量碰撞导致时间复杂度达到O(n^2)。
解决方案:
- Counter，有时和输入顺序无关，可以直接对输入排序。
- 无法排序的情况下，把每个数字异或一个随机数即可。取的时候也异或它。
这里封装一下。
"""
from bisect import bisect_left
from collections import Counter
from random import randrange

RANDOM = randrange(2 ** 62)


class FuckHashIntDict(dict):

    def __init__(self, seq):
        if seq is not None:
            import _collections_abc
            if isinstance(seq, _collections_abc.Mapping):
                super().__init__({k ^ RANDOM: v for k, v in seq.items()})
            else:
                super().__init__()
                for v in seq:
                    self[v] += 1

    def __missing__(self, key):
        return 0

    def __setitem__(self, key, value):
        super().__setitem__(key ^ RANDOM, value)

    def __getitem__(self, item):
        return super().__getitem__(item ^ RANDOM)

    def __contains__(self, item):
        return super().__contains__(item ^ RANDOM)

    def items(self):
        for k, v in super().items():
            yield k ^ RANDOM, v

    def keys(self):
        for k in super().keys():
            yield k ^ RANDOM

    def __repr__(self):
        return '{0}'.format({k ^ RANDOM: v for k, v in super().items()})


class SortedCounter:
    """排序计数，不支持修改"""

    def __init__(self, a):
        a.sort()
        keys, cnt = [], []
        for i, v in enumerate(a):
            if i == 0 or v != a[i - 1]:
                keys += [v]
                cnt += [1]
            else:
                cnt[-1] += 1
        self.keys, self.cnt = keys, cnt

    def __getitem__(self,k):
        pos = bisect_left(self.keys,k)
        if pos >= len(self.keys) or self.keys[pos] != k:
            raise Exception(f'{k} not in SortedCounter')
        return self.cnt[pos]
    def items(self):
        for k, v in zip(self.keys, self.cnt):
            yield k, v

    def keys(self):
        for k in self.keys:
            yield k

    def __repr__(self):
        return '{0}'.format({k : v for k, v in self.items()})

# a = [1, 2, 3, 4, 5, 5]
# f = FuckHashIntDict(a)
# print(Counter(a))
# print(f)
# print(f.get(6,7))
# print(SortedCounter(a))