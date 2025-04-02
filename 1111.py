n = int(input())
arr = list(map(int, input().split()))

def solve():
    if arr[0] == arr[1]:
        for i in arr:
            if i != arr[0]:
                return "B"
        return arr[0]
    
    a = (arr[2] - arr[1]) // (arr[1] - arr[0])
    b = arr[2] - arr[1] * a

    for i in range(1, n):
        if (arr[i-1] * a + b) != arr[i]:
            return "B"
    
    return arr[n-1] * a + b
        
if n == 1:
    print("A")
elif n == 2:
    if arr[0] != arr[1]:
        print("A")
    else:
        print(arr[0])
else:
    print(solve())