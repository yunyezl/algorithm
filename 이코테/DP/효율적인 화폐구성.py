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

    
# 13행을 1부터가 아닌 range(money, m+1) 로 바꾸면 쓸데없는 연산도 줄이고, if i - money >= 0도 안해줘도 됨
# 해당 화폐 가치보다 낮은 가치의 값은 어차피 구성을 못하니까!
