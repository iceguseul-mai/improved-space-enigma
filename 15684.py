import sys
from collections import deque
input = sys.stdin.readline

def bfs(lst):
    for y, x in lst:
        arr[y][x] = 1
    viruses = cnt-3
    q = deque()
    v2 = [[0]*m for _ in range(n)]
    for cy,cx in virus:
        q.append((cy, cx))
        v2[cy][cx] = 1
    
    while q:
        cy, cx = q.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny, nx = dy+cy, dx+cx
            if 0<=ny<n and 0<=nx<m and v2[ny][nx] == 0 and arr[ny][nx] == 0:
                v2[ny][nx] = 1
                q.append((ny, nx))
                viruses -= 1

    for y, x in lst:
        arr[y][x] = 0
    return viruses

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

void = []
virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            void.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

cnt=len(void)
v = [0]*(cnt)
ans = 0

for i in range(cnt-1):
    for j in range(i+1, cnt-1):
        for k in range(j+1, cnt):
            ans = max(ans, bfs([void[i], void[j], void[k]]))

print(ans)