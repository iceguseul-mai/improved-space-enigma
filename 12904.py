import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())
res = 0
while True:   
    if len(t) == len(s):
        res = int(t==s)
        break
    if t[-1] == 'B':
        t.pop()
        t = t[::-1]
    elif t[-1] == 'A':
        t.pop()

print(res)