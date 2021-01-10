n, m = map(int, input().split())

iceFrame = []
for i in range(n):
    iceFrame.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if iceFrame[x][y] == 0:
        iceFrame[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y-1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)    

# 0인 노드를 방문하지 않은 노드라고 생각, 방문한 다음에는 1로 변경
# 근처 노드에 방문하여 1로 바꿔줌. 그러면 메인에서 반복문 돌릴 때 걸러짐.


