def divide(str):
    split = []
    for i in range(0, len(str)-1):
        if (ord(str[i:i+2][0]) in range(65, 91)) and (ord(str[i:i+2][1]) in range(65, 91)):
            split.append(str[i:i+2])
    return split
    

def solution(str1, str2):

    nt = divide(str1.upper())
    deno = divide(str2.upper())
    
    # 교집합(분자)
    a = 0    
    for i in range(len(nt)):
        if nt[i] in deno:
            a += 1
            del deno[deno.index(nt[i])]
            
    # 합집합(분모)
    b = len(nt + deno)
    
    if a == 0 and b == 0:
        return 65536
    
    import math
    return math.trunc(a/b*65536)
    
    
# isalpha() 함수를 알았다면 더 간단히 해결할 수 있음, divide 함수  11, 12번째를 다음과 같이 바꾸면 더 간단하고 빨라짐
# nt = [ str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha() ]
# deno = [ str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha() ]
