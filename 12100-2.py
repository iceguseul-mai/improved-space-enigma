import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def tilt(arr):
    for i in range(len(arr)):
        std = 0
        lst = []
        for num in arr[i]:
            if num == 0:
                continue
            if std == num:
                lst.append(std*2)
                std = 0
            else:
                if std == 0:
                    std = num
                else:
                    lst.append(std)
                    std = num
        if std != 0:
            lst.append(std)
        arr[i] = lst+[0]*(n-len(lst))

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

solve(0, arr)

print(ans)