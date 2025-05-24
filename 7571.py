import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c = [], []
for i in range(m):
    a, b = map(int, input().split())
    r.append(a)
    c.append(b)

r.sort()
c.sort()
mid_r = r[m//2]
mid_c = c[m//2]
ans = 0
for i in range(m):
    ans += abs(mid_r - r[i]) + abs(mid_c - c[i])

print(ans)