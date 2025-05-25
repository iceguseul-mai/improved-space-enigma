import sys
input = sys.stdin.readline

n, m = map(int, input().split())
target = [list(input().rstrip()) for _ in range(n)]
path = []
ans = []
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            path.append((i, j))
    else:
        for j in range(m-1, -1, -1):
            path.append((i, j))
y, x = 0, -1

for i, (ny, nx) in enumerate(path):
    dy, dx = ny-y, nx-x
    if dy == 1: ans.append('D')
    elif dy == -1: ans.append('U')
    elif dx == 1: ans.append('R')
    elif dx == -1: ans.append('L')
    w = 1 if target[ny][nx] == '#' else 0
    if 1 != w:
        if i+1 < len(path):
            ny2, nx2 = path[i+1]
        else:
            ny2, nx2 = path[i-1]
        dy2, dx2 = ny2 - ny, nx2 - nx
        if dy2 == 1: d1, d2 = 'D', 'U'
        elif dy2 == -1: d1, d2 = 'U', 'D'
        elif dx2 == 1: d1, d2 = 'R', 'L'
        elif dx2 == -1: d1, d2 = 'L', 'R'
        ans.append(d1)
        ans.append(d2)
        ans.append(d1)
    y, x = ny, nx

if len(ans) > 3 * n * m:
    print(-1)
else:
    print(''.join(ans))