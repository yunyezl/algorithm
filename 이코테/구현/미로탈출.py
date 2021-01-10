# 괴물이 있는 부분 0, 없는 부분 1
# 시작 위치 (1, 1)
# 출구의 위치 (n, m) 
# 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

이동할 위치, 상/하/좌/우, 하 우 상 좌
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[n - 1][m - 1]

print(bfs(0, 0))
