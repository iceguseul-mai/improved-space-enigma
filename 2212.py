import sys
input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())
arr = sorted(list(map(int, input().rstrip().split())), reverse=True)
dist = []
if k == 1:
    print(max(arr) - min(arr))
else:
    for i in range(n-1):
        dist.append(arr[i]-arr[i+1])
    sorted(dist, reverse=True)
    print(dist)
    for i in range(k-1):
        dist[i] = 0
    print(dist)
    print(sum(dist))