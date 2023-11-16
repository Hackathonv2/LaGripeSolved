import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

REF = 'ALIMENTATION'
def matchLabel(s):
    if len(s) != len(REF):
        return False
    for a, b in zip(s, REF):
        if a != '_' and a != b:
            return False
    return True

n = int(lines[0])
for i in range(n):
    if matchLabel(lines[i+1]):
        print(i + 1)


