# 백준 1976

import sys

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

link = []
for i in range(n):
    temp = list(map(int, input().split()))
    link.append(temp)

for i in range(n):
    for j in range(n):
        if link[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

tripPlan = list(map(int, sys.stdin.readline().split()))
for i in range(len(tripPlan)-1):
    if find_parent(parent, tripPlan[i]) != find_parent(parent, tripPlan[i+1]):
        print("NO")
        break
else:
    print("YES")
