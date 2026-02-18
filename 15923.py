n = int(input())
ans = 0
x1, y1 = map(int,input().split())
a, b = x1, y1
for _ in range(n-1):
    x2, y2 = map(int,input().split())
    ans += abs(x2-x1)+abs(y2-y1)
    x1, y1 = x2, y2

print(ans + abs(x2-a)+ abs(y2-b))