def union_str(compress, cnt, standard):
    if cnt > 1:
        compress += str(cnt) + standard
    else:
        compress += standard
    return compress

def solution(s):
    answer = 0
        
    allLength = []    
    for i in range(1, len(s)//2+1):
        case = [ s[j:j+i] for j in range(0, len(s), i) ]
        cnt = 1
        standard = case[0]
        compress = ''
        for i in range(1, len(case)):
            if standard == case[i]:
                cnt += 1
            else:
                compress = union_str(compress, cnt, standard)
                standard = case[i]
                cnt = 1
        else:
            compress = union_str(compress, cnt, standard)
        allLength.append(len(compress))
    
    return min(allLength) if len(s) > 1 else 1
