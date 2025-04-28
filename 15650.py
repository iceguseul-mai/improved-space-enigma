import sys
import itertools
input = sys.stdin.readline
s = []

n, m = map(int, input().split())
ans = itertools.combinations([i for i in range(1, n+1)], m)

for i in ans:
    print(*i)