n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
visit = [list(map(int, input().split())) for _ in range(n)]

arr[0][0] = visit[0][0]
for y in range(n):
    for x in range(n):
        if y==0 and x==0:
            continue
        elif y==0:
            arr[y][x] = arr[y][x-1]*2+visit[y][x]
        elif x==0:
            arr[y][x] = arr[y-1][x]*2+visit[y][x]
        else:
            arr[y][x] = max(arr[y][x-1]*2+visit[y][x], arr[y-1][x]*2+visit[y][x])
        # for dy, dx in (0,1), (1,0):
        #     ny, nx = dy+y, dx+x
        #     if 0 <= ny < n and 0 <= nx < x:
        #         visit[ny][nx] = max(visit[ny][nx], visit[y][x]+arr[ny][nx]*2)
print(arr[n-1][n-1])