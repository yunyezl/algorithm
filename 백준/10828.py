from collections import deque
import sys
input = sys.stdin.readline

stack = deque()
result = []

n = int(input())
for i in range(n):
    command = input().rstrip()
    if command == 'pop':
        if len(stack) > 0:
            result.append(stack.pop())
        else:
            result.append(-1)
    elif command == 'size':
        result.append(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif command == 'top':
        if len(stack) != 0:
            result.append(stack[len(stack)-1])
        else:
            result.append(-1)
    else:
        stack.append(int(command[5:len(command)]))

for i in result:
    print(i)
        
