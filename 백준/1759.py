import sys
from itertools import combinations
input = sys.stdin.readline

L, C = map(int, input().split())
alphaList = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
alphaList.sort()

results = list(combinations(alphaList, L))
answer = []

for result in results:
    cnt = 0 # 모음 갯수 카운트
    for vowel in vowels:
        cnt += result.count(vowel)
    if cnt >= 1 and (len(result) - cnt) >= 2:
        print(''.join(result))
