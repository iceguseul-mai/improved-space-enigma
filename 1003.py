t = int(input())
c = 2

for i in range(t):
    m = int(input())
    z, o = 1, 0
    for j in range(m):
        z, o = o, z+o
    
    print(z, o)