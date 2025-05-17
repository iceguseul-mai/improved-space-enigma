import sys
input = sys.stdin.readline

a = list(input().rstrip())
b = list(input().rstrip())
dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] != b[j]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = dp[i-1][j-1]+1

for k in range(len(s)+1)
    lcs = dp[k][k];  
    ans = max(ans, min(k, len(s)-k) - lcs)