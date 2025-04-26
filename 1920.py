import sys
input= sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr.sort()

for i in arr2:
    l = 0
    r = n-1
    flag = False
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == i:
            print(1)
            flag = True
            break
        elif arr[mid] > i:
            r = mid-1  
        elif arr[mid] < i:
            l = mid+1
    if not flag:
        print(0)