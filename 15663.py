import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
ans = []
v = [0]*n

def dfs(i, lst):
    if i == m:
        ans.append(lst)
        return
    prev = 0
    for j in range(n):
        if v[j] == 0 and prev != arr[j]:
            prev=arr[j]
            v[j] = 1
            dfs(i+1, lst+[arr[j]])
            v[j] = 0

dfs(0, [])

for lst in ans:
    print(*lst)