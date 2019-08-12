"""
ID: mrlovre1
LANG: PYTHON3
PROB: stall4
"""

MAX = int(1e8)

def dijkstra_step():
    not_visited = set(range(n + m + 2))
    comes = [None for _ in range(n + m + 2)]
    max_flow = [0 for _ in range(n + m + 2)]
    max_flow[inode] = MAX

    while True:
        cand_node = max(not_visited, key=max_flow.__getitem__)
        cand_flow = max_flow[cand_node]

        if cand_flow == 0 or cand_node == onode:
            break

        not_visited.remove(cand_node)

        for i in adj_nodes[cand_node]:
            dist = adj[cand_node][i]
            flow = min(cand_flow, dist)
            if max_flow[i] < flow:
                max_flow[i] = flow
                comes[i] = cand_node

    flow = max_flow[onode]
    curr = onode

    while True:
        prev = comes[curr]
        if prev is None: break

        adj[prev][curr] -= flow

        if adj[prev][curr] <= 0:
            adj_nodes[prev].remove(curr)

        if adj[curr][prev] <= 0:
            adj_nodes[curr].add(prev)

        adj[curr][prev] += flow

        curr = prev

    return flow

with open("stall4.in", "r") as fin, open("stall4.out", "w") as fout:
    n, m = [int(x) for x in fin.readline().split()]
    adj = [[0 for _ in range(n + m + 2)] for _ in range(n + m + 2)]
    adj_nodes = [set() for _ in range(n + m + 2)]

    for i in range(1, n + 1):
        for j in [int(x) for x in fin.readline().split()[1:]]:
            adj[i][n + j] = 1
            adj_nodes[i].add(n + j)

    inode = 0
    onode = n + m + 1

    for i in range(1, n + 1):
        adj[inode][i] = 1
        adj_nodes[inode].add(i)

    for j in range(1, m + 1):
        adj[n + j][onode] = 1
        adj_nodes[n + j].add(onode)

    max_flow = 0
    while True:
        flow = dijkstra_step()
        if flow == 0:
            break
        max_flow += flow

    print(max_flow, file=fout)
