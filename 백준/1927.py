import sys
import heapq
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    num = int(input())
    if num == 0 and len(array) == 0:
        print(0)
    elif num == 0:
        print(heapq.heappop(array))
    else:
        heapq.heappush(array, num)
