import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
vis = [[0 for _ in range(m)] for _ in range(n)]

def dfs(y, x):
    global vis
    global size_drawing
    vis[y][x] = 1
    area = 1
    for cy, cx in (0, 1), (0, -1), (1, 0), (-1, 0):
        ny, nx = y+cy, x+cx
        if 0<=ny<n and 0<=nx<m and vis[ny][nx] == 0 and arr[ny][nx] == 1:
            area += dfs(ny, nx)
    return area

cnt = 0
size_drawing = 0

for i in range(n):
    for j in range(m):
        if vis[i][j] == 0 and arr[i][j] == 1:
            size_drawing = max(dfs(i, j), size_drawing)
            cnt += 1

print(cnt)
print(size_drawing)