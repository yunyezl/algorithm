from collections import deque

def bfs(graph, start, distance):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if distance[i] == -1:
                distance[i] = distance[v] + 1
                queue.append(i)

n, m, k, x = list(map(int, input().split()))

graph = [ [] for _ in range(n+1) ]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b) # a 노드는 b 노드와 연결

distance = [-1] * (n + 1)
distance[x] = 0

bfs(graph, x, distance)

check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
