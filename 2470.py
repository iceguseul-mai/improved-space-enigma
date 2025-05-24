import sys
input = sys.stdin.readline

# -99, -2, -1, 4, 98
n = int(input())
lst = sorted(list(map(int, input().split())))
ans = 2000000001
start, end = 0, n-1
minstart, minend = 0, 0
flag = True
while start < end:
    s = lst[start]+lst[end]
    if abs(ans) > abs(s):
        ans = s
        minstart, minend = lst[start], lst[end]
    if s > 0:
        end -= 1
    elif s < 0:
        start += 1
    else:
        print(lst[start], lst[end])
        flag = False
        break

if flag:
    print(minstart, minend)