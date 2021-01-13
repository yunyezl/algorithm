# n => 총 노드의 개수, x => 최종 도착지, k => 중간 도착지, m => 총 경로의 개수(간선의 개수)

INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    # a에서 b로 가는 비용은 1이고 연결 정보 입력받음, 연결된 값은 양방향 이동이 가능함    
    a, b = map(int, input().split())
    graph[a][b] = 1 
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
if graph[1][k] + graph[k][x] <= INF:
    print(graph[1][k] + graph[k][x])
else:
    print(-1)
