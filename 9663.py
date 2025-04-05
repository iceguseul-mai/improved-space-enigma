def recu(i):
    global ans
    if n == i:
        ans += 1
        return
    for j in range(n):
        if yq[j] == zq[i+j] == xq[i-j] == 0:
            yq[j] = 1
            zq[i + j] = 1
            xq[i - j] = 1
            recu(i+1)
            yq[j] = 0
            zq[i + j] = 0
            xq[i - j] = 0

n = int(input())
ans = 0

yq = [0]*n
zq = [0]*(n*2)
xq = [0]*(n*2)

recu(0)
print(ans)