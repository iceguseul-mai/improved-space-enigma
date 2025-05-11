import sys, heapq
input = sys.stdin.readline
INF = 1e8

n, m = map(int, input().split())
root = int(input())
node = [[] for _ in range(n+1)]

distance = [INF] * (n+1)
distance[root] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    node[u].append((v, w))

q = [(0, root)]
while q:
    cur_dist, cur_node = heapq.heappop(q)

    if cur_dist > distance[cur_node]:
        continue

    for neighbor, weight in node[cur_node]:
        dist = cur_dist + weight
        if dist < distance[neighbor]:
            distance[neighbor] = dist
            heapq.heappush(q, (dist, neighbor))

for i in range(1, n+1):
    if distance[i] > 99999999:
        print('INF')
    else:
        print(distance[i])