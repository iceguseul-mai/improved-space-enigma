import sys
input = sys.stdin.readline

n = int(input())
lines = []
for i in range(n):
    lines.append(tuple(map(int, input().split())))

ans = 0
lines.sort()
start, end = lines[0]

for x, y in lines:
    if x <= end:
        end = max(end, y)
    else:
        ans += (end - start)
        start, end = x, y

ans += (end - start)
print(ans)