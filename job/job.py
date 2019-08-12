"""
ID: mrlovre1
LANG: PYTHON3
PROB: job
"""

with open("job.in", "r") as fin, open("job.out", "w") as fout:
    n, m1, m2 = [int(i) for i in fin.readline().split()]
    times = [int(i) for i in str.join(" ", fin.readlines()).split()]
    m1_times = times[:m1]
    m2_times = times[m1:]
    m1_schedule = [0 for _ in range(m1)]
    m2_schedule = [0 for _ in range(m2)]
    m1_complete = [None for _ in range(n)]
    m2_complete = [None for _ in range(n)]

    for i in range(n):
        min_m1 = min(range(m1), key=lambda k: m1_schedule[k] + m1_times[k])
        m1_schedule[min_m1] += m1_times[min_m1]
        m1_complete[i] = m1_schedule[min_m1]

    for i in reversed(range(n)):
        min_m2 = min(range(m2), key=lambda k: m2_schedule[k] + m2_times[k])
        m2_schedule[min_m2] += m2_times[min_m2]
        m2_complete[i] = m2_schedule[min_m2]

    total_complete = [m1_complete[i] + m2_complete[i] for i in range(n)]

    print(max(m1_complete), max(total_complete), file=fout)
