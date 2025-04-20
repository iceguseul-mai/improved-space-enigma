import sys
input = sys.stdin.readline

def solve(lst, v):
    cnt = 1
    for i in range(1, len(lst)):
        if lst[i-1] == lst[i]:
            cnt += 1
        elif lst[i-1]+1==lst[i] and cnt >= l and v[i-l:i]==[0]*l:
            cnt = 1
            v[i-l:i] = [1]*l
        elif lst[i-1]>lst[i]:
            cnt = 1
        else:
            return False
    return True

n, l = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for _ in range(2):
    for lst in arr:
        v = [0]*(len(lst))
        if solve(lst, v) and solve(lst[::-1], v[::-1]):
            ans += 1
    arr = list(map(list, zip(*arr)))

print(ans)