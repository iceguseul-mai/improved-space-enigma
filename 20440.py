import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for i in range(n):
    start, end = map(int, input().split())
    if start in dict.keys():
        dict[start] += 1
    else:
        dict[start] = 1
    if end in dict.keys():
        dict[end] -= 1
    else:
        dict[end] = -1

flag = False
mos = sorted(dict.keys())
ans = -1
start, end = 0, 0
prefix_sum = 0

for t in mos:
    prefix_sum += dict[t]
    if prefix_sum > ans:
        ans = prefix_sum
        start = t
        flag = True
    elif prefix_sum < ans and flag:
        flag = False
        end = t
    
print(ans)
print(start, end)