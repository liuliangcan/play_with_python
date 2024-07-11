trie = {}


def add(word):
    cur = trie
    for c in word:
        if c not in cur:
            cur[c] = {}
        cur = cur[c]
    cur['#'] = word


def find(word):
    cur = trie
    for c in word:
        if c not in cur:
            return False
        cur = cur[c]
    return '#' in cur


# a = ['abc', 'abb', 'aab', 'cc', 'erf', 'b', ]
# b = ['a', 'bc', 'erf', 'ddd']
# for w in a:
#     add(w)
# print([find(w) for w in a])
# print([find(w) for w in b])
