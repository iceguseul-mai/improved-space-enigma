import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l, r = 0, 1000000000
arr = list(map(int, input().split()))
ans = 0

while l <= r:
    mid = (l+r)//2
    s = 0
    for i in arr:
        s += max(i-mid, 0)
    if s >= m:
        l = mid+1
        ans = max(ans, mid)
    else:
        r = mid-1

print(ans)