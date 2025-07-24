# 공유기 설치
# chap7. 369 page
# https://www.acmicpc.net/problem/2110

# 집 N개, 공유기 C개 
# 가장 인접한 공유기 사이의 거리를 최대
# 최적화 -> 파라메트릭 서치 (202 page)

N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()

max_gap = houses[-1] - houses[0]

# 평균처럼 
# def bs(nums, routers, start, end):
#     mid = (start + end) // 2
#     while(start <= end):
#         if nums[mid] 
#     return 