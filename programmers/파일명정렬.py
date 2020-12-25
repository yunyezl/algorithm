import re
        
def solution(files):
    answer = []
    
    output = []
    for i in files:
        temp = re.split('(\d+)', i)
        output.append(temp)
    
    output.sort(key=lambda x:(x[0].lower(), int(x[1])))
        
    for i in output:
        answer.append(''.join(i))
    
    return answer
