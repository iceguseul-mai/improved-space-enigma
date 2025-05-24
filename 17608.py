import sys
input = sys.stdin.readline

n = int(input())
arr = []
l_max = 0
for i in range(n):
    arr.append(int(input()))
cnt = 0
for i in range(n-1, -1, -1):
    if l_max < arr[i]:
        cnt += 1
        l_max = arr[i]
print(cnt)