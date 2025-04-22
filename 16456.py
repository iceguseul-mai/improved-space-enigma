# 0, 1, 1, 2, 3, 4
n = int(input())

arr = [0, 1, 1, 2]

if n > 3:
    for i in range(4, n+1):
        arr.append((arr[i-1] + arr[i-3]) % 1000000009)

print(arr[n])