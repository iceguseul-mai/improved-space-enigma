import sys
input = sys.stdin.readline

di = [(0,1), (0,-1), (-1,0), (1,0)]

def solve(y, x, cnt):
    global ans
    ans = max(ans, cnt)
    for cy, cx in di:
        ny, nx = cy+y, cx+x
        if 0<=ny<r and 0<=nx<c and v[ord(arr[ny][nx])] == 0:
            v[ord(arr[ny][nx])] = 1
            solve(ny, nx, cnt+1)
            v[ord(arr[ny][nx])] = 0

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
ans = 1
v = [0]*100

v[ord(arr[0][0])] = 1
solve(0, 0, 1)
print(ans)