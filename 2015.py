import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
dict = {0: 1}
cnt = 0
sum_prefix = 0

for i in arr:
    sum_prefix += i
    if sum_prefix - k in dict.keys():
        cnt += dict[sum_prefix - k]
    
    if sum_prefix in dict.keys():
        dict[sum_prefix] += 1
    else:
        dict[sum_prefix] = 1

print(cnt)