import sys
from collections import deque
input = sys.stdin.readline

def bfs(tlst):
    q = deque()
    v = [[0]*(m+2) for _ in range(n+2)] # bfs arr
    flower_cnt = 0

    for i in range(limit): # v's fundamental setting
        if tlst[i]==0: continue
        ty, tx = lst[i]
        q.append((ty, tx))
        v[ty][tx] = tlst[i]
    while q:
        cy, cx = q.popleft()
        if v[cy][cx] == 99999: continue
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ny, nx = dy+cy, dx+cx
            if arr[ny][nx] == 0 or v[ny][nx] == 99999:
                continue
            if v[ny][nx] == 0:
                if v[cy][cx] < 0:
                    v[ny][nx] = v[cy][cx]-1
                    q.append((ny, nx))
                else:
                    v[ny][nx] = v[cy][cx]+1
                    q.append((ny, nx))
            else:
                if v[cy][cx] < 0: #flower
                    if v[ny][nx]+v[cy][cx]-1==0:
                        flower_cnt += 1
                        v[ny][nx] = 99999
                else:
                    if v[ny][nx] + v[cy][cx] + 1 == 0:
                        flower_cnt += 1
                        v[ny][nx] = 99999
    return flower_cnt

def solve(n, rcnt, gcnt, tlst):
    global ans
    if n == limit:
        if rcnt == r and gcnt == g:
            ans = max(ans, bfs(tlst))
        return
    solve(n+1, rcnt+1, gcnt, tlst+[-1]) #red seed
    solve(n+1, rcnt, gcnt+1, tlst+[1]) #green seed
    solve(n+1, rcnt, gcnt, tlst+[0]) #none

n, m, r, g = map(int, input().split())
arr = [[0]*(m+2)] + [[0] + list(map(int, input().split()))+[0] for _ in range(n)]+[[0]*(m+2)]
lst = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j] == 2:
            lst.append((i, j))

limit = len(lst)
ans = 0
solve(0, 0, 0, [])
print(ans)