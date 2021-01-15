array = list(map(int, input()))

result = 0
for i in array:
    if result <= 1:
        result += i
    else:
        result *= i

print(result)
