from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
array = deque()

for i in range(n):
    command = input().split()
    if command[0] == 'push_front':
        array.appendleft(int(command[1]))
    elif command[0] == 'push_back':
        array.append(int(command[1]))
    elif command[0] == 'pop_front':
        if len(array) > 0:
            print(array.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(array) > 0:
            print(array.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(array))
    elif command[0] == 'empty':
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(array) > 0:
            print(array[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(array) > 0:
            print(array[len(array)-1])
        else:
            print(-1)
