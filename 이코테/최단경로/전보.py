import heapq

INF = int(1e9)

# 도시의 개수 n, 통로의 개수 m, 메세지를 보내고자 하는 도시 start
n, m, start = map(int, input().split())
graph = [ [] for _ in range(n + 1) ]
distance = [INF] * (n + 1)

# 모든 통로 정보 입력 받기
# 특정 도시 x에서 다른 특정 도시 y로 이어지는 통로가 있으며, 메세지가 전달되는 시간이 z
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    print(q)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]: 
            cost = dist + i[1] 
            if cost < distance[i[0]]: 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
distance.sort(reverse=True)

for i in range(len(distance)-1):
    if distance[i] == INF:
        continue
    else:
        impossible = i # 자기 자신에 대한 방문 정보도 제외해야 하므로 인덱스 그대로 넣어줌.
        max_distance = distance[i]
        break

print(n - impossible, max_distance)
