import sys
input = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append((i+1, x, y))
array.sort(key = lambda x: (x[1], x[2]))

ranking = []
for i in range(n):
    count = 0
    for j in range(i, n):
        if array[j][2] > array[i][2] and array[j][1] > array[i][1]:
            count += 1
    ranking.append((array[i][0], count))

ranking.sort()
for i in range(len(ranking)):
    print(ranking[i][1] + 1, end = ' ')
print()
