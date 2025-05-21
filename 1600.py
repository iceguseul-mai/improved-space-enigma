import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]
visit = [[[-1] * (k+1) for _ in range(w)] for _ in range(h)]
q = deque([])
visit[0][0][0] = 0
q.append((0, 0, 0)) # y, x, k
flag = True
while q:
    y, x, m = q.popleft()
    if y == h-1 and x == w-1:
        print(visit[y][x][m])
        flag = False
        break
    if m < k:
        for dy, dx in (-2, -1), (-2, 1), (-1, -2), (-1, 2), (2, -1), (2, 1), (1, -2), (1, 2):
            ny, nx = y+dy, x+dx
            if ny < 0 or nx < 0 or ny > h-1 or nx > w-1:
                continue
            if grid[ny][nx]:
                continue
            if visit[ny][nx][m+1] != -1:
                continue
            visit[ny][nx][m+1] = visit[y][x][m] + 1
            q.append((ny, nx, m+1))
    for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0):
        ny, nx = y+dy, x+dx
        if ny < 0 or nx < 0 or ny > h-1 or nx > w-1:
            continue
        if grid[ny][nx]:
            continue
        if visit[ny][nx][m] != -1:
            continue
        visit[ny][nx][m] = visit[y][x][m]+1
        q.append((ny, nx, m))

if flag:
    print(-1)