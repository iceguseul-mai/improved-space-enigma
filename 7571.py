import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c = [], []
for i in range(m):
    a,b = map(int, input().split())
    r.append(a)
    c.append(b)
r.sort()
c.sort()
mr = r[m//2]
mc = c[m//2]
ans = 0
for i in range(m):
    ans += abs(mr-r[i]) + abs(mc-c[i])

print(ans)