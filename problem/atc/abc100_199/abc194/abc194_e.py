# Problem: E - Mex Min
# Contest: AtCoder - AtCoder Beginner Contest 194
# URL: https://atcoder.jp/contests/abc194/tasks/abc194_e
# Memory Limit: 1024 MB
# Time Limit: 4000 ms

import sys
from collections import *
from itertools import *
from functools import reduce
from heapq import *
from math import inf
from operator import iadd

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')
# print = lambda d: sys.stdout.write(str(d) + "\n")  # 打开可以快写，但是无法使用print(*ans,sep=' ')这种语法,需要print(' '.join(map(str, p)))，确实会快。

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右下左上
DIRS8 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0),
         (-1, 1)]  # →↘↓↙←↖↑↗
MOD = 10 ** 9 + 7
# MOD = 998244353
PROBLEM = """https://atcoder.jp/contests/abc194/tasks/abc194_e

输入 n m(1≤m≤n≤1.5e6) 和长为 n 的数组 a(0≤a[i]<n)。
定义 mex(b) 为不在数组 b 中的最小非负整数。
遍历 a 的所有长为 m 的连续子数组 b，输出 mex(b) 的最小值。
输入
3 2
0 0 1
输出 1

输入
3 2
1 1 1
输出 0

输入
3 2
0 1 0
输出 2

输入
7 3
0 0 1 2 0 1 0
输出 2
"""
"""方法一：通用的做法是值域树状数组二分。（留给大家思考）

方法二：更巧妙的做法。

提示 1：先把前 m 个数的 mex 算出来，答案至多是它。

提示 2：我们只需要知道最小的 mex 是多少，因此当一个数滑出窗口时，只要窗口内没有这个数，那么就用这个数更新答案的最小值。

https://atcoder.jp/contests/abc194/submissions/45036824"""


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


#   722    ms
def solve():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    for v in a[:m]:
        cnt[v] += 1
    lost = [v for v in range(m + 1) if not cnt[v]]  # 维护缺失值  只有这个地方筛了，才会从500降到300ms

    ans = 0
    while cnt[ans]:
        ans += 1
    for i, v in enumerate(a[m:]):
        cnt[v] += 1
        w = a[i]
        cnt[w] -= 1
        if not cnt[w]:
            heappush(lost, w)
        while cnt[lost[0]]:
            heappop(lost)
        if lost[0] < ans:
            ans = lost[0]

    print(ans)


#   722    ms
def solve9():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    lost = list(range(m + 1))  # 维护缺失值

    ans = inf
    l = 0
    for r, v in enumerate(a):
        cnt[v] += 1
        if r - l + 1 > m:
            w = a[l]
            l += 1
            cnt[w] -= 1
            if not cnt[w]:
                heappush(lost, w)
        if r - l + 1 == m:
            while lost and cnt[lost[0]]:
                heappop(lost)
            ans = min(ans, lost[0])

    print(ans)


#   737    ms
def solve8():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    lost = list(range(n + 1))  # 维护缺失值

    ans = inf
    l = 0
    for r, v in enumerate(a):
        cnt[v] += 1
        if r - l + 1 > m:
            w = a[l]
            l += 1
            cnt[w] -= 1
            if not cnt[w]:
                heappush(lost, w)
        if r - l + 1 == m:
            while lost and cnt[lost[0]]:
                heappop(lost)
            ans = min(ans, lost[0])

    print(ans)


#   1490    ms
def solve7():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    lost = CuteSortedList(list(range(m + 1)))  # 维护缺失值

    ans = inf
    l = 0
    for r, v in enumerate(a):
        cnt[v] += 1
        if cnt[v] == 1 and v <= m:
            lost.remove(v)
        if r - l + 1 > m:
            w = a[l]
            l += 1
            cnt[w] -= 1
            if not cnt[w] and w <= m:
                lost.add(w)
        if r - l + 1 == m:
            ans = min(ans, lost[0])

    print(ans)


#   1217    ms
def solve6():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    lost = CuteSortedList(list(range(n + 2)))

    ans = inf
    l = 0
    for r, v in enumerate(a):
        cnt[v] += 1
        if cnt[v] == 1:
            lost.remove(v)
        if r - l + 1 > m:
            w = a[l]
            l += 1
            cnt[w] -= 1
            if not cnt[w]:
                lost.add(w)
        if r - l + 1 == m:
            ans = min(ans, lost[0])

    print(ans)


#   3122    ms
def solve5():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    c = [0] * (n + 1)

    def add(i, v):
        while i <= n:
            c[i] += v
            i += i & -i

    def get(i):
        s = 0
        while i:
            s += c[i]
            i -= i & -i
        return s

    def ok(x):
        return get(x) < x

    ans = inf
    l = 0
    for r, v in enumerate(a):
        cnt[v] += 1
        if cnt[v] == 1:
            add(v + 1, 1)
        if r - l + 1 > m:
            w = a[l]
            l += 1
            cnt[w] -= 1
            if not cnt[w]:
                add(w + 1, -1)
        if r - l + 1 == m:
            ans = min(ans, lower_bound(1, n, ok) - 1)

    print(ans)


#   299    ms
def solve4():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)

    for v in a[:m]:
        cnt[v] += 1

    ans = 0
    while cnt[ans]:
        ans += 1

    for i, v in enumerate(a[m:]):
        cnt[v] += 1
        w = a[i]
        cnt[w] -= 1

        if not cnt[w] and w < ans:
            ans = w
    print(ans)


#   318    ms
def solve3():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)

    for v in a[:m]:
        cnt[v] += 1

    def get(s):
        for i in count(s):
            if not cnt[i]:
                return i

    mex = get(0)
    ans = mex
    for i in range(m, n):
        v = a[i]
        cnt[v] += 1
        p = a[i - m]
        cnt[p] -= 1
        if not cnt[p] and cnt[p] < mex:
            mex = p
        elif v == mex:
            mex = get(mex + 1)
        if mex < ans:
            ans = mex
    print(ans)


#     340  ms
def solve2():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    q = deque()
    for v in a[:m]:
        cnt[v] += 1
        q.append(v)

    def get(s):
        for i in count(s):
            if not cnt[i]:
                return i

    mex = get(0)
    ans = mex
    for v in a[m:]:
        q.append(v)
        cnt[v] += 1
        p = q.popleft()
        cnt[p] -= 1
        if not cnt[p] and cnt[p] < mex:
            mex = p
        elif v == mex:
            mex = get(mex + 1)
        if mex < ans:
            ans = mex
    print(ans)


#   362    ms
def solve1():
    n, m = RI()
    a = RILST()
    cnt = [0] * (n + 1)
    q = deque()
    for v in a[:m]:
        cnt[v] += 1
        q.append(v)
    mex = 0
    for i in count(0):
        if not cnt[i]:
            mex = i
            break
    ans = mex
    for v in a[m:]:
        q.append(v)
        cnt[v] += 1
        p = q.popleft()
        cnt[p] -= 1
        if not cnt[p] and cnt[p] < mex:
            mex = p
        elif v == mex:
            for i in count(mex + 1):
                if not cnt[i]:
                    mex = i
                    break
        if mex < ans:
            ans = mex
    print(ans)


if __name__ == '__main__':
    t = 0
    if t:
        t, = RI()
        for _ in range(t):
            solve()
    else:
        solve()
