import sys
input = sys.stdin.readline

ans = set([i for i in range(1, 10001)])
a = 0
i = 1
while(a < 10100):
    num = [int(digit) for digit in str(i)]
    a = i
    for index in num:
        a += index
    ans.discard(a)
    i += 1
ans = sorted([ans])
for i in ans:
    print(i)