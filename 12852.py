import sys
input = sys.stdin.readline

def dfs(num, cnt, arr):
    global ans
    global method
    if cnt >= ans:
        return 
    if num == 1:
        if ans > cnt:
            method = arr.copy()
        ans = min(ans, cnt)
        return

    if num % 3 == 0:
        dfs(num//3, cnt+1, arr+[num//3])
    if num % 2 == 0:
        dfs(num//2, cnt+1, arr+[num//2])
    dfs(num-1, cnt+1, arr+[num-1])
    

n = int(input())
ans = 10**6
method = []
dfs(n, 0, list([n]))
print(ans)
for i in method:
    print(i, end=' ')