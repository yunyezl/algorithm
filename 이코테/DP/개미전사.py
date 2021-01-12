# n개의 식량 창고에 저장된 식량을 털 수 있는 최댓값 구하기
# 식량은 인덱스가 1개 이상 차이날 경우에만 털 수 있음(인접한 인덱스의 창고 불가)
n  = int(input())
array = list(map(int, input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-2] + array[i], d[i-1])
