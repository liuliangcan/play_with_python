"""粘贴了一个找割边的板子

例题：https://ac.nowcoder.com/acm/contest/76681/L ，需要枚举割边，看子树的和
"""



def dfs_bridges(graph, node):
    n = len(graph)

    time = 0
    discover_time = [0] * n
    low = [0] * n

    pi = [None] * n
    color = [1] * n

    ecc = [-1] * n
    ecc_number = 0
    bridges = []

    stack = [node]
    discover_stack = []
    while stack:
        current_node = stack[-1]

        if color[current_node] != 1:
            stack.pop()
            if color[current_node] == 3:
                if pi[current_node] is not None:
                    low[pi[current_node]] = min(low[pi[current_node]], low[current_node])

                    if low[current_node] == discover_time[current_node]:
                        bridges.append((pi[current_node], current_node))

                        while discover_stack:
                            top = discover_stack.pop()
                            ecc[top] = ecc_number
                            if top == current_node:
                                break

                        ecc_number += 1
                color[current_node] = 2
            continue

        time += 1
        color[current_node] = 3
        low[current_node] = discover_time[current_node] = time
        discover_stack.append(current_node)
        for adj in graph[current_node]:
            if color[adj] == 1:
                pi[adj] = current_node
                stack.append(adj)
            elif pi[current_node] != adj:
                low[current_node] = min(low[current_node], discover_time[adj])
    else:
        while discover_stack:
            top = discover_stack.pop()
            ecc[top] = ecc_number
        ecc_number += 1

    return ecc_number, ecc, bridges