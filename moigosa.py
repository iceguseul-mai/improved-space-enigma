import sys
input = sys.stdin.readline

n = int(input())
print('*'*n + (n*2-3)*' ' + '*'*n)
for i in range(n-2):
    print(' '*(i+1) + '*' + (n-2)*' ' + '*' + ((n-2-i)*2-1)*' ' +  '*' + (n-2)*' ' + '*')
print((n-1)*' ' + '*' + (n-2)*' ' + '*' + (n-2)*' ' + '*')
for i in range(n-3, -1, -1):
    print(' '*(i+1) + '*' + (n-2)*' ' + '*' + ((n-2-i)*2-1)*' ' +  '*' + (n-2)*' ' + '*')
print('*'*n + (n*2-3)*' ' + '*'*n)