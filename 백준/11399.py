import sys
input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))

array.sort()
result = 0
for i in range(n):
    result += sum(array[0:i+1])

print(result)
