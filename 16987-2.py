import sys
input = sys.stdin.readline

def solve(i, cnt):
    global ans
    if i == n:
        ans = max(ans, cnt)
        return
    if hp[i] <= 0:
        solve(i+1, cnt)
    else:
        flag = False
        for cur in range(n):
            if cur == i or hp[cur] <= 0:
                continue
            flag = True
            hp[cur] -= w[i]
            hp[i] -= w[cur]
            solve(i+1, cnt+int(hp[cur]<1)+int(hp[i]<1))
            hp[cur] += w[i]
            hp[i] += w[cur]
        if flag == False:
            solve(i+1, cnt)
            

n = int(input())
hp, w = [0]*n, [0]*n

for i in range(n):
    hp[i], w[i] = map(int, input().split())

ans = 0
solve(0, 0)
print(ans)