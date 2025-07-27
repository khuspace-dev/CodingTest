# 효율적인 화폐 구성 
# chap8. 226 page

# N가지 화폐 -> 최소 개수로, 합이 M원
# 만들 수 없다면 -1 출력

N, M = map(int, input().split())
money_list = [int(input()) for _ in range(N)] 

# 주어지는대로 dp list 상수 정하기 -> 무엇을 저장? 
# 작은 문제들로 큰 문제를 해결 -> 점화식
# dp[x] = x원을 만들기 위한 최소 화폐 개수

dp = [10001] * 10001 # max 값으로 초기화
dp[0] = 0

for money in money_list:
    for i in range(money, M+1):
        if dp[i - money] != 10001:                  # dp[i - money]가 불가능한 상황이 아니라면, 즉 money를 늘릴 수 있다면 
            dp[i] = min(dp[i], dp[i - money] + 1)   # 해당 money를 더한 상황 or 지금 현재 중 최소인 것 선택

print(dp[M])