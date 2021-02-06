from itertools import combinations

n = int(input())
ability = [list(map(int, input().split())) for _ in range(n)]
members = [i for i in range(n)]
all_team = list(combinations(members, n//2))

min_gap = 1000000
for i in range(len(all_team)//2):
    team = all_team[i]
    stat_A = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_A += ability[member][k]

    team = all_team[-i-1]
    stat_B = 0
    for j in range(n//2):
        member = team[j]
        for k in team:
            stat_B += ability[member][k]
    
    min_gap = min(min_gap, abs(stat_A - stat_B))

print(min_gap)
