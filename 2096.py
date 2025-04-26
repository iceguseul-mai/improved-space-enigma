import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp_m = [0 for _ in range(3)] # max dp
dp_l = [0 for _ in range(3)] # least dp
dp_m = arr[0].copy() # set default
dp_l = arr[0].copy() # default setting

for i in range(1, n):
    dp_m = [max(dp_m[0], dp_m[1])+arr[i][0], max(dp_m)+arr[i][1], max(dp_m[2], dp_m[1])+arr[i][2]] #recurrence relation for dp_max (+sliding window)
    dp_l = [min(dp_l[0], dp_l[1])+arr[i][0], min(dp_l)+arr[i][1], min(dp_l[2], dp_l[1])+arr[i][2]] #recurrence relation for dp_min (+sliding window)

print(max(dp_m), min(dp_l)) #print ans