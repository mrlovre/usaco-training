"""
ID: mrlovre1
LANG: PYTHON3
PROB: wormhole
"""

import operator as op
from itertools import groupby
from functools import reduce

def ncr(n, r):
    if r > n:
        return 0
    r = min(r, n - r)
    num = reduce(op.mul, range(n, n - r, -1), 1)
    den = reduce(op.mul, range(1, r + 1), 1)
    return num // den

with open("wormhole.in", "r") as fin, open("wormhole.out", "w") as fout:
    lines = iter(fin.readlines())
    n = int(next(lines))
    ws = [[int(i) for i in next(lines).split()] for _ in range(n)]
    ws.sort(key=op.itemgetter(1))
    g = groupby(ws, key=op.itemgetter(1))
    s = sum([ncr(len(list(a)), 2) for _, a in g])
    print(s, file=fout)
