import sys
input = sys.stdin.readline

change = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

cnt = 0
for coin in coins:
    if change == 0:
        break
    while change >= coin:
        change = change - coin
        cnt += 1

print(cnt)
