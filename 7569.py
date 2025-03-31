import sys
from collections import deque
input = sys.stdin.readline

m, n, he = map(int, input().split())
lst = [[list(map(int, input().split())) for _ in range(n)] for _ in range(he)]
dir = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

q = deque()
vis = [[[0] * m for _ in range(n)] for _ in range(he)]
cnt = 0

for h in range(he):
    for i in range(n):
        for j in range(m):
            if lst[h][i][j] == 1:
                q.append((h, i, j))
                vis[h][i][j] = 1
            elif lst[h][i][j] == 0:
                cnt += 1

ch, ci, cj = 0, 0, 0
while q:
    ch, ci, cj = q.popleft()
    for dh, di, dj in dir:
        nh, nj, ni = ch+dh, cj+dj, ci+di
        if 0 <= nh < he and 0 <= nj < m and 0 <= ni < n and vis[nh][ni][nj] == 0 and lst[nh][ni][nj] == 0:
            q.append((nh, ni, nj))
            vis[nh][ni][nj] = vis[ch][ci][cj]+1
            cnt -= 1

if cnt == 0:
    print(vis[ch][ci][cj] - 1)
else:
    print(-1)