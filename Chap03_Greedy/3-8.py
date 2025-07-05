# 볼링공 고르기
# chap3. 315 page 

# N = 볼링공 개수 
# M 공의 최대 무게
# balls = 볼링공 무게 

from collections import Counter     

N, M = map(int, input().split())
balls = list(map(int, input().split()))

nums = int(N * (N - 1) / 2)                      # 우선 nC2로 초기화

dup = Counter(balls)                             # 중복인 애들 지우려고 counter
# print(dup)

for weight, count in dup.items():
    if count > 1:                                # 즉, 2번 이상 count 된 무게라면? 
        nums -= int(count * (count - 1) / 2)     # 걔네들끼리의 조합을 nums에서 빼준다.

print(nums)