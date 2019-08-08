"""
ID: mrlovre1
LANG: PYTHON3
PROB: wormhole
"""

from itertools import groupby

with open("wormhole.in", "r") as fin, open("wormhole.out", "w") as fout:
    lines = iter(fin.readlines())
    n = int(next(lines))

    # ws: x, y, adjacent, linked
    ws = [[int(i) for i in next(lines).split()] + [None, None] for _ in range(n)]
    ws.sort(key=lambda x: (x[1], x[0]))
    for i, (w, w_n) in enumerate(zip(ws, ws[1:])):
        if w[1] == w_n[1]:
            w[2] = i + 1

    def go(r, p_i):
        tot = 0

        for i in range(p_i + 1, n):
            if ws[i][3] is not None: continue
            for j in range(i + 1, n):
                if ws[j][3] is not None: continue
                ws[i][3], ws[j][3] = j, i
                tot += go(r + 1, i)
                ws[i][3], ws[j][3] = None, None

        if r == n // 2:
            for i in range(n):
                p = ws[i]
                for _ in range(n):
                    try:
                        p = ws[p[3]]
                        p = ws[p[2]]
                    except TypeError:
                        break
                else:
                    tot += 1
                    # print(*[w[3] for w in ws], sep=" ")
                    break

        return tot

    print(go(0, -1), file=fout)
