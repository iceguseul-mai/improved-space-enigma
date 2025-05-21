import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(h)]
visit = [[[-1] * (2) for _ in range(w)] for _ in range(h)]
q = deque([])
visit[0][0][0] = 0
q.append((0, 0, 0)) # y, x, k
flag = True
while q:
    y, x, m = q.popleft()
    if y == h-1 and x == w-1:
        print(visit[y][x][m]+1)
        flag = False
        break
    for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0):
        ny, nx = y+dy, x+dx
        if ny < 0 or nx < 0 or ny >= h or nx >= w:
            continue
        if grid[ny][nx] == 1 and m == 0 and visit[ny][nx][1] == -1:
            visit[ny][nx][1] = visit[y][x][m] + 1
            q.append((ny, nx, 1))
        elif grid[ny][nx] == 0 and visit[ny][nx][m] == -1:
            visit[ny][nx][m] = visit[y][x][m] + 1
            q.append((ny, nx, m))

if flag:
    print(-1)