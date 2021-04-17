import sys
input = sys.stdin.readline

n = input()
array = list(map(int, input().split()))
answer = []

setArray = list(sorted(set(array)))
dic = {setArray[i]:i for i in range(len(setArray))}
answer = [dic[n] for n in array]
print(*answer)
