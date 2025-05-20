import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
dp[0] = 0
min_value = a[0]
for i in range(1, n):
    min_value = min(min_value, a[i])
    dp[i] = max(dp[i-1], a[i] - min_value)

print(*dp)