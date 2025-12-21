import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    if n == 1:
        print(m//n)
        continue
    dp = [[0 for _ in range(31)] for _ in range(31)]
    for i in range(1, m+1):
        dp[1][i] = i
    for i in range(2, n+1):
        for j in range(i, m+1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    print(dp[n][m])