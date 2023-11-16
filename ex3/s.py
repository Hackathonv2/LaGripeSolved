


import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

def convert(s):
    h, m = map(int, s.split(':'))
    return 60 * h + m

n = lines[0]
prev = []
res = 0
for line in lines[1:]:
    t1, t2 = map(convert, line.split(' - '))
    timeset = set(range(t1, t2))
    for other in prev:
        if len(timeset & other) >= 15:
            res += 1
    prev.append(timeset)

print(res)

