import sys

RI = lambda: map(int, sys.stdin.buffer.readline().split())
RS = lambda: map(bytes.decode, sys.stdin.buffer.readline().strip().split())
RILST = lambda: list(RI())
DEBUG = lambda *x: sys.stderr.write(f'{str(x)}\n')

MOD = 10 ** 9 + 7
PROBLEM = """https://www.lanqiao.cn/problems/2129/learning/
技能升级
- 把技能一字排开，每个技能加多次，相当于在这个位置选了多个连续的数(数列中取头部子段)。
- 那么选择方案一定是一些技能里，每个的前边的部分，设他们都>=p。那么每列的最小值也要>=p。
- p也可以理解成我们能选到的第m个数是几。
- 只有找到一个最大的p，整体的方案才能最大，因为实际选了p左边的所有数。
    - 注意可能存在多个相同的p，最终答案里我们只能取左边一段p。这会在后边处理，我们先找出p。
- 那么，二分的尝试p，以p为每个数列的最小值，看看能取到多少个数，要至少m个数才可以。
    - p越小，能取的数越多；p越大，能取的数越少。
    - 这是个左True，右False的模型。逆转后是找最后一个False，lower_bound()-1。
    - f(x)实现时用等差数列思想计算，不再赘述。
- 找到p后，枚举每个数列，以p为底，计算等差数列求和。
    - 同时由于p可能存在多个，需要减去右边多余的那段。
    - 可以直接记录所有数列一共取了cnt个数，cnt-m就是多的那些p。
"""


def lower_bound(lo: int, hi: int, key):
    """由于3.10才能用key参数，因此自己实现一个。
    :param lo: 二分的左边界(闭区间)
    :param hi: 二分的右边界(开区间)
    :param key: key(mid)判断当前枚举的mid是否应该划分到右半部分。
    :return: 右半部分第一个位置。若不存在True则返回hi。
    虽然实现是开区间写法，但为了和切片/数组下标统一，接口依然以[左闭,右开)方式放出。
    """
    lo -= 1  # 开区间(lo,hi)
    while lo + 1 < hi:  # 区间不为空
        mid = (lo + hi) >> 1  # py不担心溢出，实测py自己不会优化除2，手动写右移
        if key(mid):  # is_right则右边界向里移动，目标区间剩余(lo,mid)
            hi = mid
        else:  # is_left则左边界向里移动，剩余(mid,hi)
            lo = mid
    return hi


#       ms
def solve():
    n, m = RI()
    ab = []
    for _ in range(n):
        ab.append(RILST())

    def is_right(x):
        s = 0
        for a, b in ab:
            if a >= x:
                s += (a - x) // b + 1
        return s < m

    p = lower_bound(0, 10 ** 6 + 1, key=is_right) - 1
    ans = 0
    cnt = 0
    for a, b in ab:
        if a >= p:
            c = (a - p) // b + 1
            ans += c * (a + a - b * (c - 1)) // 2
            cnt += c
    ans -= (cnt - m) * p
    print(ans)


if __name__ == '__main__':
    solve()
