# 안테나
# chap6. 360 page
# https://www.acmicpc.net/problem/18310

# 집의 수 N 
# 안테나 ~ 모든 집까지 거리 합 최소 

N = int(input())
dist = list(map(int, input().split()))

dist.sort()
mid = dist[(N - 1) // 2]

print(mid)

# first
# dist.sort()
# summation = sum(dist)
# answer = summation // N 

# print(answer)

# 평균 = 제곱 오차(variance) 최소화
# 중앙값 = 절댓값 거리(L1 norm)의 합 최소화