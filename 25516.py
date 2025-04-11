import sys
sys.setrecursionlimit(100000)

def dfs(cur, d):
    global cnt
    if isApple[cur] == 1:
        cnt += 1
    if d == k:
        return
    for i in node[cur]:
        dfs(i, d+1)

n, k = map(int, input().split())
node = [[] for _ in range(n+1)]
cnt = 0

for i in range(n-1):
    p, c = map(int, input().split())
    node[p].append(c)

isApple = list(map(int, input().split()))

dfs(0, 0)

print(cnt)