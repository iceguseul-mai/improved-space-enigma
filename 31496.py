import sys
input = sys.stdin.readline

n, birch = input().split()
birch = birch.strip()
n = int(n)
ans = 0

for _ in range(n):
    item, cnt = input().split()
    cnt = int(cnt)
    item = item.split(sep='_')
    
    if birch in item:
        ans += cnt
    
print(ans)