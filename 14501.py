import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def dfs(time, price):
    global n, ans
    if time >= n+1:
        ans = max(ans, price)
        return
    if time+t[time] <= n+1:
        dfs(time+t[time], price+p[time])
    dfs(time+1, price)

n = int(input())
t = list([])
p = list([])

for i in range(1,n+1):
    o, t = map(int, input().split())
    t.append(o)
    p.append(t)
ans = 0
dfs(1, 0)
print(ans)