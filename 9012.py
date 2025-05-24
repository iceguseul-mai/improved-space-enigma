import sys
input = sys.stdin.readline

for i in range(int(input())):
    s = list(input())
    cnt = 0
    arr = []
    for j in range(len(s)):
        if s[j] == '(':
            cnt += 1
            arr.append('(')
        elif s[j] == ')':
            if len(arr) == 0:
                arr.append(')')
            elif cnt == 0:
                arr.append(')')
            else:
                cnt -= 1
                arr.pop()
    if len(arr) != 0:
        print("NO")
    else:
        print("YES")