import sys
input = sys.stdin.readline

arr = [[0 for _ in range(105)] for _ in range(105)]
cnt = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    x = 100 - x
    y = 100 - y
    for i in range(x-10, x):
        for j in range(y-10, y):
            if arr[j][i] != 1:
                cnt += 1
            arr[j][i] = 1

print(cnt)