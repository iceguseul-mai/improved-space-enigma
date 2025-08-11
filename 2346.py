import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = deque(list(map(int, input().split())))
idx = deque(list([i for i in range(1, n+1)]))
ans = []

while arr:
    ans.append(idx.popleft())
    r = arr.popleft()
    if r > 0:
        arr.rotate(1-r)
        idx.rotate(1-r)
    else:
        arr.rotate(-(r))
        idx.rotate(-(r))

print(*ans)