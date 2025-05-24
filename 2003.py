import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [arr[0]]
for i in range(1, n):
    prefix.append(prefix[i-1]+arr[i])
ans = 0
for i in range(n):
    if prefix[i] == m:
        ans += 1
    elif prefix[i] - m in prefix[:i]:
        ans += 1

print(ans)