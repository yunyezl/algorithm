def solution(clothes):

    clothesdict = {}
    for cloth in clothes:
        clothesdict[cloth[1]] = []
    for cloth in clothes:
        if cloth[0] not in clothesdict[cloth[1]]:
            clothesdict[cloth[1]].append(cloth[0])

    cnt = 1
    for key in clothesdict.keys():
        cnt *= (len(clothesdict[key])+1)

    return cnt - 1
