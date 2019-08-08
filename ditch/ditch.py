"""
ID: mrlovre1
LANG: PYTHON3
PROB: ditch
"""

MAX = int(1e8)

def dijkstra_step():
    visited = [False for _ in range(m)]
    comes = [None for _ in range(m)]
    max_flow = [0 for _ in range(m)]
    max_flow[inode] = MAX

    while True:
        cand_flow = 0
        cand_node = None
        for i in range(m):
            if not visited[i] and max_flow[i] > cand_flow:
                cand_flow = max_flow[i]
                cand_node = i

        if cand_node in [None, onode]:
            break

        visited[cand_node] = True

        for i, dist in enumerate(adj[cand_node]):
            if dist == 0: continue
            flow = min(cand_flow, adj[cand_node][i])
            if max_flow[i] < flow:
                max_flow[i] = flow
                comes[i] = cand_node

    flow = max_flow[onode]
    curr = onode

    while True:
        prev = comes[curr]
        if prev is None: break
        adj[prev][curr] -= flow
        adj[curr][prev] += flow
        curr = prev

    return flow

with open("ditch.in", "r") as fin, open("ditch.out", "w") as fout:
    n, m = [int(x) for x in fin.readline().split()]
    adj = [[0 for _ in range(m)] for _ in range(m)]
    for _ in range(n):
        a, b, flow = [int(x) for x in fin.readline().split()]
        adj[a - 1][b - 1] = flow

    inode = 0
    onode = m - 1

    max_flow = 0
    while True:
        flow = dijkstra_step()
        if flow == 0:
            break
        max_flow += flow

    print(max_flow, file=fout)
