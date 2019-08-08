"""
ID: mrlovre1
LANG: PYTHON3
TASK: test
"""

with open("test.in", "r") as fin, open("test.out", "w") as fout:
    x, y = [int(i) for i in fin.readline().split()]
    S = x + y
    print(S, file=fout)
