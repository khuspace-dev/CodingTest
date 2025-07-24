# 바닥 공사
# chap8. 223 page

# 가로 길이 N, 높이는 2
# 채우는 방법 3가지 -> 모든 경우의 수 구하기

N = int(input())

# dynamic programming

dp = [0] * (N + 1)
dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    # 한 칸 추가 -> 세로 하나 붙이기
    # 두 칸 추가 -> 경우의 수 2개 (가로 둘, 한덩어리)
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[N] % 796796)
