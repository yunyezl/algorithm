import sys
input = sys.stdin.readline

n = int(input())

array = [0] * (n)
d = []
for i in range(n):
    t, p = map(int, input().split())
    d.append([t, p])
    array[i] = p

for i in range(n):
    if i + d[i][0] > n:
        d[i][1] = 0
        continue
    for j in range(i+d[i][0], n):
        d[j][1] = max(d[j][1] , d[i][1] + array[j])

d.sort(key = lambda x:x[1])
print(d[len(d)-1][1])
