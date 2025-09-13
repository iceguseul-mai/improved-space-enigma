n = int(input())
s = set([])
ans = 0
for i in range(n):
    temp = input().rstrip()
    if temp == "ENTER":
        ans += len(s)
        s.clear()
    else:
        s.add(temp)

ans += len(s)
print(ans)