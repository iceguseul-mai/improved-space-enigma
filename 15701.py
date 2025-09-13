n = int(input())
ans = 0
b = 0

for i in range(1, n+1):
    if not i*i < n:
        if i*i == n:
            ans += 1
        break
    if n % i == 0:
        ans += 2

print(ans)