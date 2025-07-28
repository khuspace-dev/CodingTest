# 퇴사
# chap8. 377 page
# https://www.acmicpc.net/problem/14501

# 오늘부터 N + 1 일째 퇴사 -> 남은 N 일 최대한 많은 상담
# 상담 기간 T / 상담 금액 P -> 얻을 수 있는 최대 수익  

N = int(input())
time = []
pay = []

for i in range(N):
    temp_time, temp_pay = map(int, input().split())
    time.append(temp_time)
    pay.append(temp_pay)

# dp[N] 의미 = N일까지 최대 이익 
dp = [0] * 20

# first 
# for i in range(N):    
#     for k in range(i):
#         dp[i] = max(dp[i-k] + pay[i-k], dp[i])

# 지금이 i일인 상황에서 
for i in range(N): 
    if i + time[i] <= N:    # 오늘 상담 가능한 경우 -> 미래(i + time[i])에 오늘 선택한 경우와 max 치기 
        dp[i + time[i]] = max(dp[i] + pay[i], dp[i + time[i]])
    
    # 오늘 상담 X -> 내일은 일단 오늘 합산까지 가지고 가기 (init)
    dp[i + 1] = max(dp[i + 1], dp[i])        

print(dp[N])