import sys
input = sys.stdin.readline

n = int(input())
dict = {}

for i in range(n):
    enter, leave = map(int, input().split())
    if enter in dict:
        dict[enter] += 1
    else:
        dict[enter] = 1
    if leave in dict:
        dict[leave] -= 1
    else:
        dict[leave] = -1

mos = sorted(dict.keys())
ans = 0
sum_prefix = 0
start, end = 0, 0
flag = False

for t in mos:
    sum_prefix += dict[t]
    if sum_prefix > ans:
        ans = sum_prefix
        start = t
        flag = True
    elif sum_prefix < ans and flag:
        flag = False
        end = t

print(ans)
print(start, end)