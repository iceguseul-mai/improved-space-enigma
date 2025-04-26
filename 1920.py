import sys
from bisect import bisect_left
from bisect import bisect_right
input= sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr.sort()

for i in arr2:
    if bisect_right(arr, i) - bisect_left(arr, i) > 0:
        print(1)
    else:
        print(0)