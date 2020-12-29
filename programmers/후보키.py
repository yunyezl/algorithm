from itertools import combinations

def solution(relation):
    
    answer = 0
    reldic = {}
    
    for i in range(len(relation[0])):
        reldic[i] = []
    for i in range(len(relation)):
        for j in range(len(relation[i])):
            reldic[j].append(relation[i][j])
            
    noUniqueKey = []
    for i in reldic:
        if len(reldic[i]) == len(set(reldic[i])):
            answer += 1
        else:
            noUniqueKey.append(tuple(reldic[i]))

    print(list(zip(*relation)))
    for i in range(len(noUniqueKey)-1):
        for j in range(i+1,len(noUniqueKey)):
            temp = list(zip(noUniqueKey[i], noUniqueKey[j]))
            if len(temp) == len(set(temp)):
                answer += 1

    return answer
