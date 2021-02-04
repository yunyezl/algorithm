from collections import deque
import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    inputList = list(map(int, input().split()))
    array = []
    for i in range(len(inputList)):
        array.append((i, inputList[i]))

    array = deque(array)
    order = 0
    while True:
        for i in range(1, len(array)):
            if array[0][1] < array[i][1]:
                array.append(array.popleft())
                break
        else:
            printed = array.popleft()
            order += 1
            if printed[0] == m:
                return order

num = int(input())
for i in range(num):
    print(solution())
