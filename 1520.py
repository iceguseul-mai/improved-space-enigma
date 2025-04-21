import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def solve(y, x):
    if dp[y][x] == -1:
        dp[y][x] = 0
        for i, j in (0, 1), (0, -1), (-1, 0), (1, 0):
            cy, cx = y + i, x + j
            if arr[y][x] < arr[cy][cx]:
                dp[y][x] += solve(cy, cx)
    return dp[y][x]

m, n = map(int, input().split())
arr = [[0] * (n+2)] + [[0] + list(map(int, input().split()))+[0] for _ in range(m)]+[[0] * (n+2)]
dp = [[-1] * (n+2) for _ in range(m+2)]
dp[1][1] = 1

print(solve(m, n))