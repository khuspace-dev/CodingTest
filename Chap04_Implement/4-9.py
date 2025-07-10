# 치킨 배달 
# chap4. 332 page

# N = 도시의 크기 N * N
# 0 = 빈 칸 / 1 = 집 / 2 = 치킨집
# 최대 M개의 치킨집 

from itertools import combinations

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []

for y in range(5):
    for x in range(5):
        if maps[y][x] == 1:
            houses.append([x, y])
        if maps[y][x] == 2:
            chickens.append([x, y])

def chicken_dist(houses, chickens):
    distnace = 0

    for cur_house in houses:
        cur_dist = 51                # 현재 이집에서 최단거리 치킨집까지의 거리 (초기값 50 넘도록 설정)

        for cur_chicken in chickens:
            temp_dist = abs(cur_house[0] - cur_chicken[0]) + abs(cur_house[1] - cur_chicken[1])
            cur_dist = min(cur_dist, temp_dist)
        distnace += cur_dist
    return distnace

# 최대 M개, 치킨 거리 반환
answer = 51 # 초기값 50 넘도록 설정

for reduced_chickens in combinations(chickens, M):
    cur_dist = chicken_dist(houses, reduced_chickens)
    answer = min(answer, cur_dist)

print(answer)