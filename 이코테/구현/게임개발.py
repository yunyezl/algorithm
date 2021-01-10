# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽

count = 0

n, m = map(int, input().split())
x, y, direction = map(int, input().split())
gameMap = [ [int(x) for x in input().split()] for y in range(n) ]
visitedMap = [[0]*m for y in range(n)]


# 북, 동, 남, 서로 회전하기 위한 값
tx = [-1, 0, 1, 0]
ty = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


turn_time = 0
while True:
    turn_left()
    nx = x + tx[direction]
    ny = y + tx[direction]
    if gameMap[nx][ny] != 1 and visitedMap[nx][ny] != 0:
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - tx[direction]
        ny = y - ty[direction]
        if visitedMap[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

