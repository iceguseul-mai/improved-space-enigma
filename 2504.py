import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
dp = [0]
for i in range(1, n+1):
    arr.append(int(input()))

dp.append(arr[1])
if n > 1:
    dp.append(arr[1]+arr[2])

for i in range(3, n+1):
    dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1]))

print(max(dp[n], dp[n-1]))