from collections import deque
from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = list([0] + list(map(int, input().split())))
    graph = [[] for _ in range(n+1)]
    idg = [0 for _ in range(n+1)]
    dp = [0 for _ in range(n+1)] # dp[i] = 건물 i를 짓는데 필요한 최소의 시간
    q = deque()
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        idg[b] += 1
    for i in range(1, n+1):
        if idg[i] == 0:
            q.append(i)
            dp[i] = time[i]
    x = int(input())
    
    while q:
        temp = q.popleft()
        for i in graph[temp]:
            idg[i] -= 1
            dp[i] = max(dp[i], dp[temp]+time[i])
            if idg[i]==0: 
                q.append(i)
    print(dp[x])
