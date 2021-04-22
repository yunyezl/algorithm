from itertools import combinations
import sys
input = sys.stdin.readline

array = []
for _ in range(9):
    array.append(int(input().strip()))

for com in combinations(array, 7):
    if sum(com) == 100:
        for i in sorted(com):
            print(i)
        break
