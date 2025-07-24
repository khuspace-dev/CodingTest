# 개미 전사
# chap8. 220 page

# 식량 창고 N개 일직선 상 -> 인접 창고 털면 X
# 각 창고에 저장된 식량 개수 K (foods)

N = int(input())
foods = list(map(int, input().split()))

dp = [0] * (N + 1)

# 초기화 주의 
dp[0] = foods[0]
dp[1] = max(foods[0], foods[1]) # 둘 중 하나를 털면 됨 

# 이후 an 점화식 
for i in range(2, N):
    dp[i] = max(dp[i-2] + foods[i], dp[i-1])

# dp[i]는 i번째 창고까지의 최대 식량
# index 처리로 -1 하는 것 (칸은 4칸 -> 0 ~ 3 매핑)
print(dp[N - 1])