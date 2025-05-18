import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
print(sum(arr[:len(arr)-1]))