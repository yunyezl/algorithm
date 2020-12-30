def solution(n, lost, reserve):
    set_reserve = list(set(reserve)-set(lost))
    set_lost = list(set(lost)-set(reserve))
    noClothes = len(set_lost)

    for lost_num in set_lost:
        if lost_num-1 in set_reserve:
            noClothes -= 1
            del set_reserve[set_reserve.index(lost_num-1)]
        elif lost_num+1 in set_reserve:
            noClothes -= 1
            del set_reserve[set_reserve.index(lost_num+1)]
    return n - noClothes
