import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

visit = [[[0]*2 for _ in range(m)] for _ in range(n)]
queue = deque()
visit[0][0][0] = 1
queue.append((0, 0, 0))
i = 0

while queue:
    y, x, didBreak = queue.popleft()
    for cy, cx in (1, 0), (0, 1), (-1, 0), (0, -1):
        ny, nx = cy+y, cx+x
        if 0 <= ny < n and 0 <= nx < m:
            if arr[ny][nx] == 1 and didBreak == 0 and visit[ny][nx][1] == 0:
                visit[ny][nx][1] = visit[y][x][0] + 1
                queue.append((ny, nx, 1))
            elif arr[ny][nx] == 0 and visit[ny][nx][didBreak] == 0:
                visit[ny][nx][didBreak] = visit[y][x][didBreak] + 1
                queue.append((ny, nx, didBreak))

if visit[n-1][m-1][0] == 0 and visit[n-1][m-1][1] == 0:
    print(-1)
elif visit[n-1][m-1][0] == 0:
    print(visit[n-1][m-1][1])
elif visit[n-1][m-1][1] == 0:
    print(visit[n-1][m-1][0])
else:
    print(min(visit[n-1][m-1]))