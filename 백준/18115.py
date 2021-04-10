import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
array = deque(map(int, input().split()))

after = deque(range(1, n+1))
before = deque()

while array:
    i = array.pop()
    a = after.popleft()
    if i == 1:
        before.appendleft(a)
    elif i == 2:
        before.insert(1, a)
    elif i == 3:
        before.append(a)

print(*before)
