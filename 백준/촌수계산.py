from sys import stdin


n = int(stdin.readline().rstrip())
man1, man2 = map(int, stdin.readline().rstrip().split())
m = int(stdin.readline().rstrip())
family_tree = [[] for _ in range(n+1)]    # 가족 관계
visited = [0]*(n+1)    # 방문 처리

# 가족 관계 정보 입력
for _ in range(m):
    x, y = map(int, stdin.readline().rstrip().split())
    family_tree[x].append(y)
    family_tree[y].append(x)


# DFS 수행
def dfs(before):
    global family_tree, visited, man1
    for man in family_tree[before]:
        if man != man1 and visited[man] == 0:
            visited[man] = visited[before] + 1
            dfs(man)


dfs(man1)
    
# 탐색 후에도 여전히 0이라면 친척 관계가 전혀 없다는 것(연결되어있지 않음)
if visited[man2] == 0:
    print(-1)
else:
    print(visited[man2])
