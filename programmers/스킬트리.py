def solution(skill, skill_trees):
    answer = 0
    
    for st in skill_trees:
        for i in st:
            if i not in skill:
                st = st.replace(i, '')
        if len(st) == 0:
            answer += 1
        else:
            if skill[0] in st and st in skill:
                answer += 1

    return answer
