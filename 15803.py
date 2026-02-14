import sys
input = sys.stdin.readline

a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())
if a1*b2 + b1*c2 + c1*a2 - b1*a2 - c1*b2 - a1*c2 == 0: 
    print("WHERE IS MY CHICKEN?")
else:
    print("WINNER WINNER CHICKEN DINNER!")