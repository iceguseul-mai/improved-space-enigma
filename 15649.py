import sys
input = sys.stdin.readline
s = []
def dfs():
    if len(s) == m:
        print(*s)
    
    for i in arr:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
dfs()