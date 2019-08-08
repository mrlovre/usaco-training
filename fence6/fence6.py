"""
ID: mrlovre1
LANG: PYTHON3
PROB: fence6
"""

with open("fence6.in", "r") as fin, open("fence6.out", "w") as fout:
    lines = iter(fin.readlines())
    n = int(next(lines))
    fs = [None for _ in range(n)]
    ps = [None for _ in range(n)]
    ns = [None for _ in range(n)]
    for i in range(n):
        line = next(lines).split()
        k = int(line[0]) - 1
        fs[k] = [int(k) for k in line]
        ps[k] = [int(k) - 1 for k in next(lines).split()]
        ns[k] = [int(k) - 1 for k in next(lines).split()]

    b = [False for _ in range(n)]

    def go(curr, start, come):
        # print(f"go({curr}, {start}, {come})")

        b[curr] = True
        l_n = 10000
        nexts = ns[curr] if come is None or come not in ns[curr] else ps[curr]
        for p in nexts:
            if p == start:
                b[curr] = False
                return fs[curr][1]

            if b[p]:
                continue

            l_n = min(l_n, go(p, start, curr))

        b[curr] = False

        return fs[curr][1] + l_n

    sol = min([go(i, i, None) for i in range(n)])
    # print([go(i, i, None) for i in range(n)])
    print(sol, file=fout)
