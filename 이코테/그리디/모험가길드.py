n = int(input())
adventurers = list(map(int, input().split()))
adventurers.sort()

group = 0 # 총 그룹의 수 카운트 
count = 0 # 그룹에 포함된 모험가의 수
 
for adv in adventurers:
    count += 1
    if count >= adv: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        group += 1
        count = 0

print(group)
