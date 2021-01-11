# 절단기 높이 h
# 손님이 요청한 떡 길이가 m일 때 적어도 m만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값
 
n, m = map(int, input().split())
dducks = list(map(int, input().split()))

dducks.sort()
start = 0
end = dducks[len(dducks)-1]
h = (start + end) // 2

temp = 0

while True:
    sum = 0
    for dduck in dducks: # 떡 자르고 합치기 
        if dduck - h > 0:
            sum += dduck - h
    if sum == m:
        break
    if temp != 0 and sum < m: 
        h = temp
        break
    if sum > m: # 자르고 합친 떡의 길이가 손님이 요청한 떡보다 큰 경우, 절단기 높이를 1씩 늘려서 최대값으로 찾아감
        temp = h
        h += 1
    else: # 자르고 합친 떡의 길이가 손님이 요청한 떡보다 작은 경우, 더 크게 잘라야함
        temp = 0
        h = h // 2
    
print(h)
