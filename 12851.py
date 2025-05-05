from collections import deque

n, k = map(int, input().split())
check = [0] * (100001)
back = [0] * (100001)
q = deque([n])
cnt = 0
res = 0

while q:
    cur = q.popleft()
    if cur == k:
        res = check[cur]
        cnt += 1
        break
    if (cur - 1 >= 0 and check[cur - 1] == 0) or (check[cur - 1] == check[cur]+1):
        q.append(cur - 1)
        check[cur - 1] = check[cur] + 1
        back[cur-1] = cur
    if (cur + 1 <= 100000 and check[cur + 1] == 0) or (check[cur + 1] == check[cur]+1):
        q.append(cur + 1)
        check[cur + 1] = check[cur] + 1
        back[cur+1] = cur
    if (cur * 2 <= 100000 and check[cur * 2] == 0) or (check[cur * 2] == check[cur]+1):
        q.append(cur * 2)
        check[cur * 2] = check[cur] + 1
        back[cur*2] = cur

print(res)
print(cnt)