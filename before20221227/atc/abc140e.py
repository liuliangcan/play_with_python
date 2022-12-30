import sys
from collections import *
from contextlib import redirect_stdout
from itertools import *
from math import sqrt
from array import *
from functools import lru_cache
import heapq
import bisect
import random
import io, os
from bisect import *
from io import StringIO

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())

MOD = 998244353
"""https://atcoder.jp/contests/abc140/tasks/abc140_e

输入 n(≤1e5) 和一个 1~n 的排列 p。
输出 p 中所有长度至少为 2 的子数组的第二大元素的和。
输入
3
2 3 1
输出 5

输入
5
1 2 3 4 5
输出 30

输入
8
8 2 7 3 4 5 6 1
输出 136
https://atcoder.jp/contests/abc140/submissions/36373341

方法一：贡献法，对每个 p[i]，求上个、上上个、下个、下下个更大元素的位置，分别记作 L LL R RR。
具体求法见双周赛第四题（链接见右）。
那么 p[i] 对答案的贡献为 p[i] * ((L-LL)*(R-i) + (RR-R)*(i-L))。

方法二：对于排列，其实不需要单调栈。
用双向链表思考（实现时用的数组）：
把 p 转换成双向链表，按元素值从小到大遍历 p[i]，那么方法一中的 4 个位置就是 p[i] 左边两个节点和右边两个节点。
算完 p[i] 后把 p[i] 从链表中删掉。
怎么用数组实现见代码。 

顺带一提，循环结束后，L[i] 和 R[i] 就是 p[i] 的上个/下个更大元素的位置。
如果要求更小元素位置，倒序遍历即可。
"""

"""贡献法，考虑每个数作为第二大的数都出现在几个子段里。
想到lc双周赛T4 2454. 下一个更大元素 IV https://leetcode.cn/problems/next-greater-element-iv/
用双单调栈，由于是作为第二大，因此找的子段必有且仅有如下特征之一:
    1) i在[left,i]这个子段里是最大的,且在[i,right]里是第二大
    2) i在[left,i]这个子段里是第二大,且在[i,right]里是最大的
因此要分别记两个left和right共4个数组。
最大，可以用传统1个单调栈搞（即找左右两遍第一个比i大的数)。
第二大，可以用双栈：
    右：遍历到i时，元素j从第二个栈弹出，代表i是j右边第二个比j大的数。(双周赛T4)
    左：
        对于栈1，若出完栈长度超过2，st[-2]可能是left[i]
        对于栈2，若出完栈栈内依然有元素，se[-1]可能是left[i]
        取max即可。
            这里补充证明：考虑左边比i大的第二个数j，设为a[j],第一个数设为a[k]
                显然有j<k<i,a[j]>a[i],a[k]>a[i],其中j+1..k-1之间的元素均<a[i]
                考虑a[j]和a[k]的相对大小,
                若a[j]<a[k],a[j]会被a[k]从栈1pop到栈2，这时，a[j]将是栈2的栈顶第一个大于a[i]的元素,
                    而此时若栈1有超过2个元素，则st[-2]一定<j，得证。
                若a[j]>a[k],a[j]不会被a[k]pop,留在栈1的st[-2]的位置上，得证。
"""


#     169 	 ms
def solve1(n, a):
    st = []  # 单减栈
    se = []  # 第二个栈
    left1, right1 = [-1] * n, [n] * n  # i作为最大值左右两边能管辖的范围
    left2, right2 = [-1] * n, [n] * n  # i作为最大或次大值左右两边能管辖的范围(单边)
    for i, v in enumerate(a):
        while se and a[se[-1]] < v:
            right2[se.pop()] = i
        if se:
            left2[i] = se[-1]
        t = []
        while st and a[st[-1]] < v:
            right1[st[-1]] = i
            t.append(st.pop())
        if st:
            left1[i] = st[-1]
        if len(st) >= 2:
            left2[i] = max(left2[i], st[-2])
        se += t[::-1]
        st.append(i)

    ans = 0
    for i, v in enumerate(a):
        ans += v * (i - left1[i]) * (right2[i] - right1[i]) + v * (right1[i] - i) * (left1[i] - left2[i])
    print(ans)
    # print(a)
    # print(left1)
    # print(right1)
    # print(left2)
    # print(right2)


#    120  	 ms 双向链表删除最小值
def solve(n, a):
    pos = [0] * (n + 1)
    prev = [0] * (n + 1)
    nxt = [0] * (n + 1)
    for i, v in enumerate(a):
        pos[v] = i
        prev[i] = i - 1
        nxt[i] = i + 1
    ans = 0
    for i in range(1, n + 1):
        p = pos[i]
        l = prev[p]
        ll = l if l < 0 else prev[l]
        r = nxt[p]
        rr = r if r >= n else nxt[r]
        ans += i * (p - l) * (rr - r) + i * (r - p) * (l - ll)
        nxt[l] = r
        prev[r] = l

    print(ans)


def main():
    n, = RI()
    a = RILST()
    solve(n, a)


if __name__ == '__main__':
    # testcase 2个字段分别是input和output
    test_cases = (
        (
            """
3
2 3 1
""",
            """
5
"""
        ),
        (
            """
5
1 2 3 4 5
""",
            """
30
"""
        ),
        (
            """
8
8 2 7 3 4 5 6 1
""",
            """
136
"""
        )
    )
    if os.path.exists('test.test'):
        total_result = 'ok!'
        for i, (in_data, result) in enumerate(test_cases):
            result = result.strip()
            with StringIO(in_data.strip()) as buf_in:
                RI = lambda: map(int, buf_in.readline().split())
                RS = lambda: map(bytes.decode, buf_in.readline().strip().split())
                with StringIO() as buf_out, redirect_stdout(buf_out):
                    main()
                    output = buf_out.getvalue().strip()
                if output == result:
                    print(f'case{i}, result={result}, output={output}, ---ok!')
                else:
                    print(f'case{i}, result={result}, output={output}, ---WA!---WA!---WA!')
                    total_result = '---WA!---WA!---WA!'
        print('\n', total_result)
    else:
        main()
