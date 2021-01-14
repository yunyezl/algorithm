def check_team(parent, a, b):
    if parent[a] == parent[b]:
        return "YES"
    else:
        return "NO"

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def team_union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)
outputList = []

for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    i, a, b = map(int, input().split())
    if i == 0:
        team_union(parent, a, b)
    else:
        outputList.append(check_team(parent, a, b))

for output in outputList:
    print(output)

