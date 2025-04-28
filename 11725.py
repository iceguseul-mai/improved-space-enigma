import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

n = int(input())
tree = [[] for _ in range(n+1)]
node = [0 for _ in range(n+1)]

def dfs(cur):
    for child in tree[cur]:
        if node[child] == 0:
            node[child] = cur
            dfs(child)
    return

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[b].append(a)
    tree[a].append(b)

dfs(1)

for i in range(2, n+1):
    print(node[i])