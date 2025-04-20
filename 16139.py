n = int(input())

arr = [0, 1, 2]

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    for i in range(3, n+1):
        arr.append((arr[2] + arr[1]))
        arr.remove(arr[0])
    print(arr[2] % 10)   