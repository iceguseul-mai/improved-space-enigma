n = int(input())
x = list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    a = []
    for j in range(n*2):
        if x[j] == i:
            a.append(j)
    ans = max(ans, a[1]-a[0]-1)

print(ans)