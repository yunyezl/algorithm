def isRight(u):
    left_count = 0
    right_count = 0
    for i in u:
        if i == '(':
            left_count += 1
        else:
            right_count += 1
        if right_count > left_count:
            return False
    return True

def divide(p):

    left = 0
    right = 0
    u = ''
    v = ''

    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break

    return u, v

def solution(p):
    
    answer = ''
    
    # step 1
    if p == '':
        return ''
    
    # step 2
    u, v = divide(p)
        
    if isRight(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = u[1: -1]
        u = u.replace('(', '.')
        u = u.replace(')', '(')
        u = u.replace('.', ')')
        answer += u    
        return answer




