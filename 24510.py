import sys
input = sys.stdin.readline
ans = -67
for _ in range(int(input())):
    s = input()
    ans = max(ans, s.count("for")+s.count("while"))

print(ans)