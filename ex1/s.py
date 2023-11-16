
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

n = int(lines[0])
res = 0
for line in lines[1:]:
    x, y = map(int, line.split())
    if x*x + y*y < 100*100:
        res += 1
print(res)


