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

line = sorted(dict.keys())
ans = 0
sum_prefix = 0
flag = False

for t in line:
    sum_prefix += dict[t]
    if sum_prefix > ans:
        ans = sum_prefix
        flag = True
    elif sum_prefix < ans and flag:
        flag = False

print(ans)