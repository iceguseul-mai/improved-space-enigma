import sys
input = sys.stdin.readline

x = int(input())
cnt = 0
while len(str(x)) > 1:
    cnt += 1
    add = list(str(x))
    new_x = 0
    for i in add:
        new_x += int(i)
    x = new_x

print(cnt)
if x % 3 == 0:
    print("YES")
else:
    print("NO")