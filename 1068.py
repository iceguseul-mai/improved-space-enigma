import sys
input = sys.stdin.readline

def dfs(cur):
    global leaf
    global tree
    if cur == delete:
        return -1
    if len(tree[cur]) < 1:
        leaf += 1
        return 0
    flag = True
    for i in tree[cur]:
        if i != delete:
            dfs(i)
            flag = False
    if flag == True:
        leaf += 1
    return 0

# 2 -> 0 -> 1 -> 4

n = int(input())
tree = [[] for _ in range(n)]
arr = list(map(int, input().split()))
leaf = 0
root = 0

for i in range(n):
    if arr[i] == -1:
        root = i
    else:
        tree[arr[i]].append(i)

delete = int(input())


if delete == root:
    print(0)
else:
    dfs(root)
    print(leaf)