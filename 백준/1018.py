n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(input()))

change = []

for x in range(n - 7):
    for y in range(m - 7):
        W = 0 # W로 시작할 때 바꿔야하는 인덱스의 수
        B = 0 # B로 시작할 때 바꿔야하는 인덱스의 수
        for i in range(x, x + 8):
            for j  in range(y, y + 8):
                if (i + j) % 2 == 0:
                    # 첫 시작이 B일때 홀수항은 B로 구성되어야 함
                    if array[i][j] == 'W': B += 1  
                    # 첫 시작이 W일때 홀수항들은 W로 구성되어야 함
                    elif array[i][j] == 'B': W += 1
                else : 
                    # 첫 시작이 B일때 짝수항들은 W로 구성되어야 함
                    if array[i][j] == 'B': B += 1 
                    # 첫 시작이 W일때 짝수항들은 B로 구성되어야 함
                    elif array[i][j] == 'W': W += 1
        change.append(W)                          
        change.append(B)                          

print(change)
print(min(change))        

# BBBBBBB -> WBWBWBWB or BWBWBWBW
# WBWBWBWB로 바꾸기 위해서는 홀수번째일 때 W여야 됨
# 홀수번째 일때 B인 것이 4이므로, 
# WBWBWBWB로 바꾸기 위해서 (W로 시작하는 체스로 바꾸기 위해서) 4번 변경되어야 함 => W = 4
