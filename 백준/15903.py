import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()

for i in range(m):
    total = array[0] + array[1]
    array[0] = total
    array[1] = total
    array.sort()

print(sum(array))
