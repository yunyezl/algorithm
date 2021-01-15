from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))
all = []

for i in range(1, len(coins)+1):
    all += list(map(sum, combinations(coins, i)))

all.sort()
for i in range(len(all) - 1):
    if all[i] + 1 in all:
        continue
    else:
        answer = all[i] + 1
        break
else:
    answer = max(all) + 1

print(answer)
 
