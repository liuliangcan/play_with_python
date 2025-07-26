"""后缀数组SA：
https://oi-wiki.org/string/sa/
https://www.cnblogs.com/milliele/p/11019099.html
rk[i]是每个后缀s[i:]的排名
sa[i]排名为i的后缀的起始下标

例题：
直接用sa的rk作比较：https://ac.nowcoder.com/acm/contest/76681/I （这题也可以用字符串哈希，二分两个子串最长相同前缀，然后比较下一个位置
"""


class SuffixArray:
    def __init__(self, s):
        self.s = s
        self.doubling()

    def doubling(self):
        # sa[i]:排名为i的后缀的起始位置
        # rk[i]:起始位置为i的后缀的排名
        s = self.s
        n = len(s)
        sa = []
        rk = []
        for i in range(n):
            rk.append(ord(s[i]) - ord('a'))  # 刚开始时，每个后缀的排名按照它们首字母的排序
            sa.append(i)  # 而排名第i的后缀就是从i开始的后缀

        l = 0  # l是已经排好序的长度，现在要按2l长度排序
        sig = 26  # sig是unique的排名的个数，初始是字符集的大小
        while True:
            p = []
            # 对于长度小于l的后缀来说，它们的第二关键字排名肯定是最小的，因为都是空的
            for i in range(n - l, n):
                p.append(i)
            # 对于其它长度的后缀来说，起始位置在`sa[i]`的后缀排名第i，而它的前l个字符恰好是起始位置为`sa[i]-l`的后缀的第二关键字
            for i in range(n):
                if sa[i] >= l:
                    p.append(sa[i] - l)
            # 然后开始基数排序，先对第一关键字进行统计
            # 先统计每个值都有多少
            cnt = [0] * sig
            for i in range(n):
                cnt[rk[i]] += 1
            # 做个前缀和，方便基数排序
            for i in range(1, sig):
                cnt[i] += cnt[i - 1]
            # 然后利用基数排序计算新sa
            for i in range(n - 1, -1, -1):
                cnt[rk[p[i]]] -= 1
                sa[cnt[rk[p[i]]]] = p[i]

            # 然后利用新sa计算新rk
            def equal(i, j, l):
                if rk[i] != rk[j]: return False
                if i + l >= n and j + l >= n:
                    return True
                if i + l < n and j + l < n:
                    return rk[i + l] == rk[j + l]
                return False

            sig = -1
            tmp = [None] * n
            for i in range(n):
                # 直接通过判断第一关键字的排名和第二关键字的排名来确定它们的前2l个字符是否相同
                if i == 0 or not equal(sa[i], sa[i - 1], l):
                    sig += 1
                tmp[sa[i]] = sig
            rk = tmp
            sig += 1
            if sig == n:
                break
            # 更新有效长度
            l = l << 1 if l > 0 else 1
        # 计算height数组
        k = 0
        height = [0] * n
        for i in range(n):
            if rk[i] > 0:
                j = sa[rk[i] - 1]
                while i + k < n and j + k < n and s[i + k] == s[j + k]:
                    k += 1
                height[rk[i]] = k
                k = max(0, k - 1)  # 下一个height的值至少从max(0,k-1)开始
        self.sa = sa
        self.rk = rk
        self.height = height
        return sa, rk, height

    def build_lcp_array(self):
        s = self.s
        sa = self.sa
        n = len(s)
        # 计算排名数组：rank[i]表示后缀i在后缀数组中的排名
        rank = self.rk
        # for i in range(n):
        #     rank[sa[i]] = i

        lcp = [0] * n  # 初始化LCP数组,lcp[i]代表排名为sa[i]和sa[i-1]的公共前缀长度
        h = 0  # 当前公共前缀长度

        for i in range(n):
            # 只处理排名>0的后缀（排名0的后缀没有前驱）
            if rank[i] > 0:
                # 找到后缀数组中前一个后缀的起始位置
                j = sa[rank[i] - 1]

                # 从位置h开始比较两个后缀
                while i + h < n and j + h < n and s[i + h] == s[j + h]:
                    h += 1  # 增加公共前缀长度

                # 设置LCP值
                lcp[rank[i]] = h

                # 为下一个后缀准备：公共前缀长度至少为h-1
                if h > 0:
                    h -= 1

        return lcp
    def get_pos_range(self, w):  # 获取所有s中所有w所在位置的起始点，例如s='abaac',w='a',则返回(0,2,3)，但是yield返回
        sa, s, n = self.sa, self.s, len(self.s)

        def bigger_or_startswith_w(x):
            i = sa[x]
            for c in w:
                if i == n or s[i] < c:
                    return False
                if s[i] > c:
                    return True
                if s[i] == c:
                    i += 1
            return True

        def bigger_not_startswith_w(x):
            i = sa[x]
            for c in w:
                if i == n:
                    return False
                if s[i] > c:
                    return True
                if s[i] == c:
                    i += 1
            return False

        l, r = -1, n
        while l + 1 < r:
            mid = (l + r) // 2
            if bigger_or_startswith_w(mid):
                # if s[sa[mid]:]>=w:
                r = mid
            else:
                l = mid
        left = r
        l, r = left-1, n
        while l + 1 < r:
            mid = (l + r) // 2
            if bigger_not_startswith_w(mid):
                r = mid
            else:
                l = mid
        right = r
        # print(left,right)
        for i in range(left, right):
            yield sa[i]


if __name__ == '__main__':
    s = 'jzeaeee'
    sa = SuffixArray(s)
    # print(sa.sa)
    # print(sa.rk)
    w = 'abc'
    words = ["ee","ae","e","eaeee","jz"]
    for w in words:
        for v in sa.get_pos_range(w):
            print(w,v, v + len(w))
