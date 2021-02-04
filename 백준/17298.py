import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

stack = []
result = [-1 for _ in range(n)]

stack.append(0)
i = 1
while stack and i < n:
    while stack and array[stack[-1]] < array[i]:
        result[stack[-1]] = array[i]
        stack.pop()
    stack.append(i)
    i += 1

print(' '.join(map(str, result)))

# 1. stack = [0]
# 2. array[0] < array[1] true, result[0] = 5, stack -> empty
# 3. stack = [1]
# 4. array[1] < array[2] false
# 5. stack = [1, 2]
# 6. array[2] < array[3] true, result[2] = 7, stack = [1]
# 7. array[1] < array[3] true, result[1] = 7
