import sys
input = sys.stdin.readline
s = []

def backtrack(cur):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(cur, n+1):
        s.append(i)
        backtrack(i)
        s.pop()

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
backtrack(1)