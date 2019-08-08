"""
ID: mrlovre1
LANG: PYTHON3
PROB: skidesign
"""

from math import floor, ceil

with open("skidesign.in", "r") as fin, open("skidesign.out", "w") as fout:
    lines = iter(fin.readlines())
    n = int(next(lines))
    hs = [int(next(lines)) for _ in range(n)]
    min_h, max_h = min(hs), max(hs)
    sol = None

    for low in range(min_h, max_h - 17 + 1):
        high = low + 17
        s = sum([d ** 2 for d in [h - high for h in hs] if d > 0] + [d ** 2 for d in [low - h for h in hs] if d > 0])
        if sol is None or sol > s:
            sol = s

    print(sol, file=fout)
