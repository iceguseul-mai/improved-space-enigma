import re

n = int(input())
s = input()
s = re.split(r'[.\|\:\#]+', s)
ans = 0

for i in s:
    ans += int(i)

print(ans)