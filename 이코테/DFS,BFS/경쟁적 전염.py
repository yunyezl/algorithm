from collections import deque

n, k = map(int, input().split())
examiner = [] # 전체 보드 정보
data = [] # 바이러스에 대한 정보

for i in range(n):
    examiner.append(list(map(int, input().split())))
    for j in range(n):
        if examiner[i][j] != 0:
            data.append((examiner[i][j], 0, i, j))
            
data.sort()
q = deque(data)

ts, tx, ty = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus, s, x, y = q.popleft()
    if s == ts:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if examiner[nx][ny] == 0:
                examiner[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(examiner[tx-1][ty-1])
