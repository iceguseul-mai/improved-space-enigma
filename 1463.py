import sys
input = sys.stdin.readline

def dfs(depth, cur):
    global ans
    if depth >= ans:
        return
    if cur == 1:
        ans = min(ans, depth)
        return

    if cur % 3 == 0:
        dfs(depth+1, cur//3)
    if cur % 2 == 0:
        dfs(depth+1, cur//2) 
    dfs(depth+1, cur-1)

n = int(input())
ans = 10**6
dfs(0, n)
print(ans)