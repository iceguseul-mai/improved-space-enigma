import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))

s = [0]
t = 0
for i in range(len(l)):
    t += l[i]
    s.append(t)

for _ in range(m):
    i, j = map(int, input().split())
    print(s[j] - s[i - 1])