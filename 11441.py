import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp_prefix = [a[0]]
for i in range(1, n):
    dp_prefix.append(dp_prefix[i-1]+a[i])

for i in range(int(input())):
    s, e = map(int, input().split())
    s-=1
    e-=1
    if s == 0:
        print(dp_prefix[e])
    else:
        print(dp_prefix[e]-dp_prefix[s-1])