# 효율적인 화폐 구성 
# chap8. 226 page

# N가지 화폐 -> 화폐 최소 개수로, 합이 M원
# 이후 각 화폐의 가치가 주어짐

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)] 

# 주어지는대로 dp list 상수 정하기
dp = [0] * 100

for i in range(M):
    dp[i] = min()

print(dp[N])