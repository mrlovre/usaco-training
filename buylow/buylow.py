"""
ID: mrlovre1
LANG: PYTHON3
PROB: buylow
"""

from collections import defaultdict
from bisect import bisect_left

with open("buylow.in", "r") as fin, open("buylow.out", "w") as fout:
    lines = fin.readlines()
    n = int(lines[0])
    prices = [int(x) for x in str.join("\n", lines[1:]).split()]
    max_days = [1 for _ in range(n)]
    max_days_dict = defaultdict(list)

    m = 0
    for i in range(n):
        p = prices[i]
        for q in reversed(range(m + 1)):
            escape = False
            for j in max_days_dict[q]:
                if p < prices[j]:
                    max_days[i] = q + 1
                    escape = True
                    break
            if escape:
                break

        m = max(m, max_days[i])
        max_days_dict[max_days[i]].append(i)

    routes = [1 for _ in range(n)]

    for i in range(n):
        if max_days[i] > 1:
            r = 0
            p = None
            ind = bisect_left(max_days_dict[max_days[i] - 1], i)
            for j in reversed(max_days_dict[max_days[i] - 1][:ind]):
                if prices[j] > prices[i] and (p is None or p != prices[j]):
                    r += routes[j]
                    p = prices[j]
            routes[i] = r

    max_total = 0
    route = 0
    p = None

    for i in reversed(range(n)):
        if max_days[i] > max_total:
            max_total = max_days[i]
            route = routes[i]
            p = prices[i]
        elif max_days[i] == max_total and (p is None or p != prices[i]):
            route += routes[i]
            p = prices[i]

    print(max_total, route, file=fout)
