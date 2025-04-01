a = int(input())
b = int(input())

if a < 2 or (a == 2 and b < 18):
    print("Before")
elif a == 2 and b > 18:
    print("After")
elif a >= 3:
    print("After")
elif a == 2 and b == 18:
    print("Special")