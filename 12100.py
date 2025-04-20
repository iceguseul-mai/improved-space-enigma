def tilt(arr):
    for i in range(len(arr)):
        standard = 0
        lst = []
        for num in arr[i]:
            if num == 0:
                continue
            if num == standard:
                lst.append(standard*2)
                standard = 0
            else:
                if standard == 0:
                    standard = num
                else:
                    lst.append(standard)
                    standard = num
        if standard != 0:
            lst.append(standard)
        arr[i] = lst+[0]*(n-len(lst))

n = int(input())
ans = 0
arr = [list(map(int, input().split())) for _ in range(n)]

def solve(cnt, arr):
    global ans
    if cnt == 5:
        ans = max(ans, max(map(max, arr)))
        return

    tmp = [lst[::] for lst in arr]
    tilt(tmp)
    solve(cnt+1, tmp)

    tmp = [lst[::-1] for lst in arr]
    tilt(tmp)
    solve(cnt+1, tmp)

    tmp_r = list(map(list, zip(*arr)))
    tmp = [lst[::] for lst in tmp_r]
    tilt(tmp)
    solve(cnt+1, tmp)

    tmp = [lst[::-1] for lst in tmp_r]
    tilt(tmp)
    solve(cnt+1, tmp)

import sys
input = sys.stdin.readline

solve(1, arr)

print(ans)