import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))
a = [0]*(n)
for i in range(1, n):
    a[i] = abs(arr[i] - arr[i-1])

prefix = [0]*n
for i in range(1, n):
    prefix[i] = prefix[i-1]+a[i]

for _ in range(q):
    start, end = map(int, input().split())
    print(prefix[end-1] - prefix[start-1])