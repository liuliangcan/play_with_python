# Problem: C. Bank Hacking
# Contest: Codeforces - Codeforces Round 408 (Div. 2)
# URL: https://codeforces.com/problemset/problem/796/C
# Memory Limit: 256 MB
# Time Limit: 2000 ms

import sys
import random
from types import GeneratorType
import bisect
import io, os
from bisect import *
from collections import *
from contextlib import redirect_stdout
from itertools import *
from array import *
from functools import lru_cache, reduce
from heapq import *
from math import sqrt, gcd, inf

if sys.version >= '3.8':  # ACW没有comb
    from math import comb

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
RANDOM = random.randrange(2 ** 62)
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://codeforces.com/problemset/problem/796/C

输入 n(1≤n≤3e5) 和长为 n 的数组 a(-1e9≤a[i]≤1e9) 表示树上每个点的点权，然后输入这棵树的 n-1 条边（节点编号从 1 开始）。
执行如下操作恰好一次：
选一个点作为根节点，根节点的点权不变，它的儿子的点权增加 1，其余点的点权增加 2。
最小化这棵树的最大点权，并输出。
输入
5
1 2 3 4 5
1 2
2 3
3 4
4 5
输出 5

输入
7
38 -29 87 93 39 28 -55
1 2
2 5
3 2
2 4
1 7
7 6
输出 93

输入
5
1 2 7 6 7
1 5
5 3
3 4
2 4
输出 8
"""
"""做法不止一种，这里说说最简单的用平衡树/最大堆的模拟做法。
先把所有 a[i] 加入集合（平衡树/最大堆），然后从 1 开始枚举 i，以及 i 的邻居（点权要加 1），从集合中去掉这些点的点权后，集合中的最大值就是「其余点」的点权最大值了（点权要加 2），统计完最大值后，再把 i 和 i 的邻居的点权重新加回来。
每次枚举计算出的最大值，再取最小值，就是答案。
用最大堆实现的话可以用 lazy 删除，具体见下面代码。

https://codeforces.com/problemset/submission/796/215802020"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(闭区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi+1。
    虽然实现是开区间写法，但为了思考简单，接口以[左闭,右闭]方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    hi += 1
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


"""二分，最小化最大值
显然是单调的。
设这个值是x，那么所有val<=x-2的节点都不用管，它们可以在任意位置。
val==x的节点只能是根，否则加1就超了。 root=i
val==x-1的节点只能是根的儿子。 root in neighbor[i]
val>x 直接说明x不合法：猜的小了。
那么可以通过根来判断x是否合法。
"""


#    530   ms
def solve1():
    n, = RI()
    a = RILST()
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    def ok(x):  # 最大值是x行不行
        roots = set()  # 根可能是谁
        for i, v in enumerate(a):
            if v > x:  # 超过了
                return False
            elif v == x:  # 只能当根
                if roots and i not in roots:  # 如果有候选根，那么判断i是否在候选
                    return False
                roots = {i}  # 根只能是i
            elif v == x - 1:  # 可以当根的儿子，那么尝试找根
                if not roots:
                    roots |= set(g[i] + [i])
                else:
                    roots &= set(g[i] + [i])
                    if not roots:
                        return False

        return True

    print(lower_bound(min(a), max(a) + 2, ok))


class CuteSortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi

        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    # def __getitem__(self, index):
    #     """Lookup value at `index` in sorted list."""
    #     pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
    #     return self._lists[pos][idx]
    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        if isinstance(index, slice):
            _lists = self._lists
            start, stop, step = index.indices(self._len)
            if step == 1 and start < stop:  # 如果是正向的步进1，找到起起止点，然后把中间的拼接起来即可
                if start == 0 and stop == self._len:  # 全部
                    return reduce(iadd, self._lists, [])
                start_pos, start_idx = self._fen_findkth(start)
                start_list = _lists[start_pos]
                stop_idx = start_idx + stop - start

                # Small slice optimization: start index and stop index are
                # within the start list.

                if len(start_list) >= stop_idx:
                    return start_list[start_idx:stop_idx]

                if stop == self._len:
                    stop_pos = len(_lists) - 1
                    stop_idx = len(_lists[stop_pos])
                else:
                    stop_pos, stop_idx = self._fen_findkth(stop)

                prefix = _lists[start_pos][start_idx:]
                middle = _lists[(start_pos + 1):stop_pos]
                result = reduce(iadd, middle, prefix)
                result += _lists[stop_pos][:stop_idx]
                return result
            if step == -1 and start > stop:  # 如果是负向的步进1，直接翻转调用自己再翻转即可
                result = self.__getitem__(slice(stop + 1, start + 1))
                result.reverse()
                return result

            indices = range(start, stop, step)  # 若不是步进1，只好一个一个取
            return list(self.__getitem__(index) for index in indices)

        else:
            pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
            return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))


#    1762   ms
def solve():
    n, = RI()
    a = RILST()
    g = [[] for i in range(n)]
    for _ in range(n - 1):
        u, v = RI()
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)
    sl = CuteSortedList(a)
    ans = inf
    for i in range(n):
        p = a[i]
        sl.remove(a[i])
        for j in g[i]:
            sl.remove(a[j])
            p = max(p, a[j] + 1)
        if sl:
            p = max(p, sl[-1] + 2)
        ans = min(ans, p)
        sl.add(a[i])
        for j in g[i]:
            sl.add(a[j])

    print(ans)

if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
