def solution(name):
    alpa_distance = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    idx, answer = 0, 0
    while True:
        answer += alpa_distance[idx]
        alpa_distance[idx] = 0
        if sum(alpa_distance) == 0:
            break
        left, right = 1, 1
        while alpa_distance[idx - left] == 0:
            left += 1
        while alpa_distance[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer
    
#그리디
#문제가 좀 이상함. 완전탐색이어야 할 것 같다.
