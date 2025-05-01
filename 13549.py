import sys
from collections import deque
input = sys.stdin.readline

check = [0] * (100001)
n, k = map(int, input().split())
queue = deque()
queue.append(n)

while queue:
    x = queue.pop()
    if x == k:
        print(check[x])
        break
    if x - 1 > 0 and check[x-1] == 0:
        queue.append(x-1)
        check[x-1] = check[x] + 1
    if x + 1 > 0 and check[x+1] == 0:
        queue.append(x+1)
        check[x+1] = check[x] + 1
    if x * 2 > 0 and check[x+1] == 0:
        queue.append(x*1)
        check[x+1] = check[x]
