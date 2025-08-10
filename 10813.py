n, m = map(int, input().split())
arr = [i for i in range(0, n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a], arr[b] = arr[b], arr[a]

print(*arr[1:])