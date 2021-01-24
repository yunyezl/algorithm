# 백준 10775

# 내 풀이, 그리디, 시간초과
g = int(input()) # 탑승구의 수
p = int(input()) # 비행기의 수
docking = [ 0 for _ in range(g+1) ]

array = []

for i in range(p):
    array.append(int(input()))

# 제일 큰 숫자부터 도킹할 수 있으면 도킹하고, 못하면 다음으로 큰 숫자에 도킹
for i in array:
    for j in range(i, 0, -1):
        if docking[j] == 0:
            docking[j] = 1
            break
    else:
        break

print(sum(docking))

# 서로소 집합 자료구조 이용
import sys

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

g = int(sys.stdin.readline()) # 탑승구의 수
p = int(sys.stdin.readline()) # 비행기의 수
parent = [0] * (g + 1)

array = []
for i in range(p):
    array.append(int(sys.stdin.readline()))

for i in range(1, g + 1):
    parent[i] = i

result = 0
for i in array:
    i = find_parent(i)
    if i == 0:
        break
    union_parent(i, i-1)
    result += 1

print(result)
