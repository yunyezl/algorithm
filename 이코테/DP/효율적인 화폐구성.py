# n가지 종류위 화폐 존재
# 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 함
# 각 화폐는 몇 개라도 이용할 수 있고, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분함.

n, m = map(int, input().split())
moneyConf = [ int(input()) for _ in range(n) ]

d = [10001] * (m + 1)
d[0] = 0

print(moneyConf)
for money in moneyConf:
    for i in range(1, m+1):
        if i - money >= 0:
            d[i] = min(d[i], d[i-money]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
