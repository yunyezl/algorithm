def solution(m, musicinfos):
    answer = ''
    mi = {}
    
    for i in musicinfos:
        temp = i.split(",")
        start = temp[0]
        end = temp[1]
        title = temp[2]
        code = temp[3]
        playTime = int(end[-2:]) - int(start[-2:])
        if playTime > len(code):
            gap = playTime - len(code)
            playLine = code + code*(gap//len(code)) + code[:gap%len(code)]
        elif playTime < len(code):
            playLine = code[:playTime]
        else:
            playLine = len(code)
        mi[title] = [playLine, playTime]
        
    print(mi)
    return answer
