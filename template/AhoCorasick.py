"""ac自动机，多模式匹配
用sum(len(ts)) 时间创建trie以及build初始化
用O(len(s)+匹配次数) 时间搜索主串

本模板：
    - ac = AhoCorasickss)创建ac自动机并建树， 会把words也保存进去
    - ac.put() 手动传word
    - ac.build_fail() 建立失败指针
    - ac.find()->[int, int]  返回匹配的[主串下标(末尾)，模式串在words位置] 注意是yield的
        - 比如返回s=abcd t = [33,a,bcd] 则会返回[(0,1),(3,2)]

直接调模板慢0.9倍左右：https://leetcode.cn/problems/construct-string-with-minimum-cost/solutions/2833949/hou-zhui-shu-zu-by-endlesscheng-32h9/
例题：
    - 3213. 最小代价构造字符串 https://leetcode.cn/problems/construct-string-with-minimum-cost/
"""


class Node:
    __slots__ = 'son', 'fail', 'last', 'idx'

    def __init__(self):
        self.son = [None] * 26
        self.fail = None  # 当 o.son[i] 不能匹配 target 中的某个字符时，o.fail.son[i] 即为下一个待匹配节点（等于 root 则表示没有匹配）
        self.last = None  # 后缀链接（suffix link），用来快速跳到一定是某个 words[k] 的最后一个字母的节点（等于 root 则表示没有）
        self.idx = -2


class AhoCorasick:
    def __init__(self, words=None):
        self.root = Node()
        if words:
            for i, w in enumerate(words):
                self.put(w, i)
        self.words = words if words else []

    def put(self, s: str, i: int = -1) -> None:
        cur = self.root
        for b in s:
            b = ord(b) - ord('a')
            if cur.son[b] is None:
                cur.son[b] = Node()
            cur = cur.son[b]
        if i == -1:
            i = len(self.words)
            self.words.append(s)
        cur.idx = i

    def build_fail(self) -> None:
        self.root.fail = self.root.last = self.root
        q = deque()
        for i, son in enumerate(self.root.son):
            if son is None:
                self.root.son[i] = self.root
            else:
                son.fail = son.last = self.root  # 第一层的失配指针，都指向根节点 ∅
                q.append(son)
        # BFS
        while q:
            cur = q.popleft()
            for i, son in enumerate(cur.son):
                if son is None:
                    # 虚拟子节点 o.son[i]，和 o.fail.son[i] 是同一个
                    # 方便失配时直接跳到下一个可能匹配的位置（但不一定是某个 words[k] 的最后一个字母）
                    cur.son[i] = cur.fail.son[i]
                    continue
                son.fail = cur.fail.son[i]  # 计算失配位置
                # 沿着 last 往上走，可以直接跳到一定是某个 words[k] 的最后一个字母的节点（如果跳到 root 表示没有匹配）
                son.last = son.fail if son.fail.idx != -2 else son.fail.last
                q.append(son)

    def find(self, s: str) -> (int, int):
        cur = root = self.root
        for i, c in enumerate(s):
            cur = cur.son[ord(c) - ord('a')]
            if cur.idx != -2:
                yield i, cur.idx  # 主串末尾位置，对应的模式串数组下标
            fail = cur.last
            while fail != root:
                # 手写 min，避免超时
                yield i, fail.idx  # 主串末尾位置，对应的模式串数组下标
                fail = fail.last


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        p = {}
        for w, c in zip(words, costs):
            p[w] = min(p.get(w, inf), c)
        ss, cc = [], []
        for k, v in p.items():
            ss.append(k)
            cc.append(v)
        ac = AhoCorasick(ss)
        ac.build_fail()

        n = len(target)
        f = [0] + [inf] * n

        for i, idx in ac.find(target):
            # print(i,idx)
            t = f[i + 1 - len(ss[idx])] + cc[idx]
            if t < f[i + 1]: f[i + 1] = t
            # f[i+1] = min(f[i+1], )
        # for i in range(1, n + 1):
        #     cur = cur.son[ord(target[i - 1]) - ord('a')]  # 如果没有匹配相当于移动到 fail 的 son[target[i-1]-'a']
        #     if cur.idx != -2:  # 匹配到了一个尽可能长的 words[k]
        #         f[i] = min(f[i], f[i - len(ss[cur.idx])] + cc[cur.idx])
        #         print(i,cur.idx)
        #     # 还可能匹配其余更短的 words[k]，要在 last 链上找
        #     fail = cur.last
        #     while fail != root:
        #         print(i,fail.idx)
        #         # 手写 min，避免超时
        #         tmp = f[i - len(ss[fail.idx])] + cc[fail.idx]
        #         if tmp < f[i]:
        #             f[i] = tmp
        #         fail = fail.last
        return -1 if f[n] == inf else f[n]
