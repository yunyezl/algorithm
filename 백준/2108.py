import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
    
print(round(sum(array) / len(array)))
print(sorted(array)[len(array)//2])

cnt = Counter(array)
cnt = cnt.most_common()
cnt.sort(key = lambda x: (-x[1], x[0]))

if len(array) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(array)-min(array))
