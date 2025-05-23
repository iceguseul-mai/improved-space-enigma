import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    tmp = ' '*(n-i)+'*'*i
    print(tmp)
for i in range(n-1, 0, -1):
    tmp = ' '*(n-i)+'*'*i
    print(tmp)