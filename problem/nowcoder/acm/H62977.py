# Problem: 三维偏序
# Contest: NowCoder
# URL: https://ac.nowcoder.com/acm/contest/62977/H?&headNav=acm
# Memory Limit: 524288 MB
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
PROBLEM = """
"""


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


class BIT:
    def __init__(self, n):
        self.c = [0] * (n + 1)
        self.n = n

    def add(self, i, v):
        while i <= self.n:
            self.c[i] += v
            i += i & -i

    def sum_prefix(self, i):
        ans = 0
        while i:
            ans += self.c[i]
            i -= i & -i
        return ans

    def sum(self, l, r):
        return self.sum_prefix(r) - self.sum_prefix(l - 1)


#    1208ms
def solve():
    n, = RI()
    a = RILST()
    idx, cnt = BIT(n), CuteSortedList()  # 计算下标和、储存下标顺序

    ans = [0] * n  # 最大的数一定是0，避免处理delay最后一组
    q = []  # delay处理，为了处理相同的值时，全部下标已处理完
    for v, i in sorted(zip(a, range(1, n + 1))):
        while q and v != q[-1][0]:  # 如果是新的值，处理delay的数据
            _, ii = q.pop()
            if len(cnt) < ii:  # 个数不够，-1
                ans[ii - 1] = -1
                continue
            r = cnt[ii - 1]  # 前ii个下标
            # 把ii+1~r的数全挪到1~ii-1，则是sum(ii+1,r)-sum(1,ii-1),但idx存的是已访问的下标和，那么左侧需要用面积-已访问
            ans[ii - 1] = idx.sum(ii + 1, r) - (1+ii-1)*(ii-1)//2 + idx.sum_prefix(ii-1)

        idx.add(i, i)
        cnt.add(i)
        q.append((v, i))

    print(' '.join(map(str, ans)))


#    1313ms
def solve2():
    n, = RI()
    a = RILST()
    idx, cnt = BIT(n), CuteSortedList()  # 计算下标和、储存下标顺序
    for i in range(1, n + 1):
        idx.add(i, i)
    ans = [0] * n  # 最大的数一定是0，避免处理delay最后一组
    q = []  # delay处理，为了处理相同的值时，全部下标已处理完
    for v, i in sorted(zip(a, range(1, n + 1))):
        while q and v != q[-1][0]:  # 如果是新的值，处理delay的数据
            _, ii = q.pop()
            if len(cnt) < ii:  # 个数不够，-1
                ans[ii - 1] = -1
                continue
            r = cnt[ii - 1]  # 前ii个下标
            # 把ii+1~r的数全挪到1~ii-1，则是sum(ii+1,r)-sum(1,ii-1),但idx存的是未访问的下标，那么右侧需要用面积-已访问
            ans[ii - 1] = (ii + 1 + r) * (r - ii) // 2 - idx.sum(ii + 1, r) - idx.sum_prefix(ii)

        idx.add(i, -i)
        cnt.add(i)
        q.append((v, i))

    print(' '.join(map(str, ans)))


#    1349ms
def solve1():
    n, = RI()
    a = RILST()
    idx, cnt = BIT(n), CuteSortedList()  # 计算下标和、储存下标顺序
    for i in range(1, n + 1):
        idx.add(i, i)
    ans = [-1] * n
    q = []  # delay处理，为了处理相同的值时，全部下标已处理完
    for v, i in sorted(zip(a, range(1, n + 1))):
        while q and v != q[-1][0]:  # 如果是新的值，处理之前储存的值
            _, ii = q.pop()
            if len(cnt) < ii:  # 个数不够，-1
                continue
            r = cnt[ii - 1]  # 前ii个下标
            if r == ii:  # 左边填满了
                ans[ii - 1] = 0
                continue
            ans[ii - 1] = (ii + 1 + r) * (r - ii) // 2 - idx.sum(ii + 1, r) - idx.sum_prefix(ii)

        idx.add(i, -i)
        cnt.add(i)
        q.append((v, i))

    for _, ii in q:  # 处理遗留的值
        if len(cnt) < ii:  # 个数不够，-1
            continue
        r = cnt[ii - 1]
        if r == ii:
            ans[ii - 1] = 0
            continue
        ans[ii - 1] = (ii + 1 + r) * (r - ii) // 2 - idx.sum(ii + 1, r) - idx.sum_prefix(ii)

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
