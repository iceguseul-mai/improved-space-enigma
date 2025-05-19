import sys
input = sys.stdin.readline

s = list(input().strip())
q = int(input())
prefix = {}
for i in 'abcdefghijklmnopqrstuvwxyz':
    cnt = 0
    tmp = [0]*len(s)
    for j in range(len(s)):
        if i == s[j]:
            cnt += 1
        tmp[j] = cnt
    prefix[i] = tmp

for _ in range(q):
    alpha, start, end = sys.stdin.readline().split()
    start, end = int(start), int(end)
    if start > 0: 
        print(prefix[alpha][end] - prefix[alpha][start-1])
    else:
        print(prefix[alpha][end])