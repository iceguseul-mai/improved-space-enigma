import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*(m+1)]+[[0]+list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp[1][1] = arr[0][0]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = arr[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n][m])