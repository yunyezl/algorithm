from itertools import combinations
import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    for j in combinations(array, i):
        if sum(j) == s:
            cnt += 1

print(cnt)
