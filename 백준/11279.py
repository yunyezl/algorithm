import heapq
import sys
input = sys.stdin.readline

n = int(input())
array = []

for _ in range(n):
    number = int(input())
    if len(array) == 0 and number == 0:
        print(0)
    elif number != 0:
        heapq.heappush(array, (-number, number))
    else:
        print(heapq.heappop(array)[1])
