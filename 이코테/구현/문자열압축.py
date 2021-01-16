def solution(s):
    answer = 0
    
    if len(s) == 1:
        return 1;
    
    allCase = []
    for i in range(1, len(s)//2+1):
        slicelist = [ s[j:j+i] for j in range(0, len(s), i) ]
        allCase.append(slicelist)
        
    allLength = []    
    for case in allCase:
        cnt = 1
        standard = case[0]
        compress = ''
        minLength = 1001
        for i in range(1, len(case)):
            if standard == case[i]:
                cnt += 1
            else:
                if cnt > 1:
                    compress += str(cnt) + standard
                else:
                    compress += standard
                standard = case[i]
                cnt = 1
        else:
            if cnt > 1:
                compress += str(cnt) + standard
            else:
                compress += standard
        allLength.append(len(compress))
    
    return min(allLength)
