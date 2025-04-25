import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(50000)

def solve(y, x, color):
    global visit
    visit[y][x] = 1
    for i, j in (0, 1), (0, -1), (1, 0), (-1, 0):
        ny, nx = y+i, x+j
        if 0<=ny<n and 0<=nx<n:
            if visit[ny][nx] == 0 and arr[ny][nx] == color:
                solve(ny, nx, color)
    return

def solve_blind(y, x, color):
    global visit_blind
    visit_blind[y][x] = 1
    for i, j in (0, 1), (0, -1), (1, 0), (-1, 0):
        ny, nx = y+i, x+j
        if 0<=ny<n and 0<=nx<n:
            if visit_blind[ny][nx] == 0 and arr[ny][nx] == color:
                solve_blind(ny, nx, color)    

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
visit = [[0 for _ in range(n)] for _ in range(n)]
visit_blind = [[0 for _ in range(n)] for _ in range(n)]

ans = 0
ans_blind = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            solve(i, j, arr[i][j])
            ans += 1
 
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visit_blind[i][j] == 0:
            solve_blind(i, j, arr[i][j])
            ans_blind += 1

print(ans, ans_blind)