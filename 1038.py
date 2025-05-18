import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())-1
res = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        tmp = ''.join(list(map(str, reversed(list(j)))))
        res.append(int(tmp))
res.sort()
print(res[n] if n < 1023 else -1)