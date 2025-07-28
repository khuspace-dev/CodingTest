# 병사 배치하기 
# chap8. 380 page
# https://www.acmicpc.net/problem/18353

# N명의 병사 무작위 나열 -> 높은 전투력부터 내림차순 
# 열외 가능, 남은 병사 수가 최대가 되도록 배치, 열외하는 병사 수 출력

# 1 ≤ N ≤ 2,000
# 전투력 = 10,000,000보다 작거나 같은 자연수

N = int(input())
power = list(map(int, input().split()))

# 현재까지의 병사 수 (max) -> list 길이 저장하기
# dp = [0] * 2000
dp = [1] * 2000

# first
# for i in range(N - 1):
#     # 현재 i 명 -> 열외 여부
#     if power[i] <= power[i+1]: # 나 or 다음 병사 열외 
#         dp[i] = max(dp[i-1], dp[i])
#     else:
#         dp[i + 1] = max(dp[i], dp[i + 1])

for i in range(1, N):
    for j in range(i):
        # 나보다 앞선 애들 중, power가 더 크다면 -> 가능
        # 아니라면 -> 열외 대상 (= 빼야함. 무조건 감소해야함)
        if power[j] > power[i]:
            dp[i] = max(dp[i], dp[j] + 1) # jth 추가 의미

print(N - max(dp))