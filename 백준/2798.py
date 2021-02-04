from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = list(map(int, input().split()))

allcase = list(map(sum, combinations(array, 3)))

result = 0
for i in allcase:
    if i <= m and i > result:
        result = i

print(result)
