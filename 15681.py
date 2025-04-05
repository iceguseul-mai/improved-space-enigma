import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dp(cur):
    global memo
    memo[cur] = 1
    for i in arr[cur]:
        if memo[i] == 0:
            memo[cur] += dp(i)
    return memo[cur]


n, r, q = map(int, input().split())

arr = [[] for _ in range(n+1)]
memo = [0] * (n+1)

for i in range(n-1):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

dp(r)

for i in range(q):
    query = int(input())
    print(memo[query])