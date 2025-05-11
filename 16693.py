import sys, math
input = sys.stdin.readline

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

if p1/a1 > p2/(r1**2*math.pi):
    print("Whole pizza")
else:
    print("Slice of pizza")