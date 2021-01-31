import sys
input = sys.stdin.readline
dp = []

n = int(input())

for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = dp[i][j] + min(dp[i-1][j+1], dp[i-1][j+2])
        elif j == 1:
            dp[i][j] = dp[i][j] + min(dp[i-1][j-1], dp[i-1][j+1])
        elif j == 2:
            dp[i][j] = dp[i][j] + min(dp[i-1][j-2], dp[i-1][j-1])

print(min(dp[n-1]))

