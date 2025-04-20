def dfs(i, sm, cnt):
    global ans
    if i == n:
        if sm == s and cnt > 0:
            ans += 1
        return
    dfs(i+1, sm+arr[i], cnt+1)
    dfs(i+1, sm, cnt)

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

dfs(0, 0, 0)

print(ans)