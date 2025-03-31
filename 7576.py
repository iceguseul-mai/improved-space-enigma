import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

q = deque()
vis = [[0] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] == 1:
            q.append((i, j))
            vis[i][j] = 1
        elif lst[i][j] == 0:
            cnt += 1

ci, cj = 0, 0, 
while q:
    ci, cj = q.popleft()
    for di, dj in dir:
        nj, ni = cj+dj, ci+di
        if 0 <= nj < m and 0 <= ni < n and vis[ni][nj] == 0 and lst[ni][nj] == 0:
            q.append((ni, nj))
            vis[ni][nj] = vis[ci][cj]+1
            cnt -= 1

if cnt == 0:
    print(vis[ci][cj] - 1)
else:
    print(-1)