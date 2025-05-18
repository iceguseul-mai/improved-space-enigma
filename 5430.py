import sys, re
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    func = list(input().rstrip())
    n = int(input())
    arr = input()
    rendered = re.split(r'[\[\]\,]+', arr)
    del rendered[0]
    del rendered[-1]
    flag = False
    isReversed = 0
    rendered = deque(rendered)
    for i in func:
        if i == 'R':
            isReversed += 1
            isReversed %= 2
        elif i == 'D':
            try:
                if isReversed == 0:
                    rendered.popleft()
                else:
                    rendered.pop()
            except IndexError:
                print("error")
                flag = True
                break
    if flag:
        continue
    if isReversed == 1:
        rendered.reverse()
    print("[" + ",".join(rendered) + "]")