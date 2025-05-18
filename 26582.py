import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,w = map(int, input().split())
    dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
    arr = [(0, 0)]
    for i in range(n):
        arr.append(list(map(int, input().split())))
    for i in range(1, n+1):
        for j in range(1, w+1):
            if j < arr[i][1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-arr[i][1]]+arr[i][0])
    print(dp[n][w])