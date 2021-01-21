n = int(input())
array = []
for i in range(n):
    name, a, b, c = input().split()
    array.append((name, int(a), int(b), int(c)))

array.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in array:
    print(i[0])
