import sys
input = sys.stdin.readline

m = int(input())
s = set()

for i in range(m):
    c = list(input().split())
    
    if c[0] == 'add':
        s.add(c[1])
    elif c[0] == 'remove':
        s.discard(c[1])
    elif c[0] == 'check':
        if c[1] in s:
            print(1)
        else:
            print(0)
    elif c[0] == 'toggle':
        if c[1] in s:
            s.discard(c[1])
        else:
            s.add(c[1])
    elif c[0] == 'all':
        s = set(str(i) for i in range(1, 21))
    elif c[0] == 'empty':
        s = set()