import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
ans = [[-1 for _ in range(m)] for _ in range(n)]
startx, starty = 0, 0
for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            starty, startx = i, j
            ans[starty][startx] = 0
        elif lst[i][j] == 0:
            ans[i][j] = 0
q = deque()
q.append((starty, startx))
while q:
    y, x = q.popleft()
    for cy, cx in (0, 1), (0, -1), (1, 0), (-1, 0):
        ny, nx = cy+y, cx+x
        if 0<=ny<n and 0<=nx<m and lst[ny][nx] == 1 and ans[ny][nx] == -1:
            q.append((ny, nx))
            ans[ny][nx] = ans[y][x] + 1

for i in range(n):
    print(*ans[i])