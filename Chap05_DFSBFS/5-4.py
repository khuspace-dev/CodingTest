# 연구소
# chap5. 341 page 

# N X M = 연구소 크기 
# 0 = 빈 칸, 1 = 벽, 2 = 바이러스 
# 벽은 꼭 3개를 세워야 한다. 
# output = 안전 영역의 최댓값 출력 = dfs?

from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

'''
2들을 기준으로 dfs 상하좌우 확장
1을 만나면 막힘 / 0을 만나면 확장
2의 최소 = 0의 최대
2의 덩어리를 최소로 만드는 추가 1의 배치 
-> N * M - (2의 공간 최소) - ( 1들의 영역 + 3: 추가벽 )= 최대 0의 영역 
'''

area_ZER = [(i, j) for i in range(N) for j in range(M) if maps[i][j] == 0]
area_ONE = [(i, j) for i in range(N) for j in range(M) if maps[i][j] == 1]
area_TWO = [(i, j) for i in range(N) for j in range(M) if maps[i][j] == 2]

# 동 남 서 북 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# count = len(area_TWO)

def dfs(x, y, maps):
    global count
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        if (0 <= temp_x < M) and (0 <= temp_y < N):   # 범위 내에서
            if maps[temp_y][temp_x] == 0:
                maps[temp_y][temp_x] = 2    # 전염시키기
                count += 1                  # 2의 칸이 하나 증가 
                dfs(temp_x, temp_y, maps)   # 그 칸에서 다시 전염              
   
max_safe = 0 

for trial in combinations(area_ZER, 3):
    temp = deepcopy(maps)
    count = len(area_TWO)

    for y, x in trial:
        temp[y][x] = 1 # 임의의 벽을 세운 것 

    for y, x in area_TWO:
        dfs(x, y, temp)

    temp_safe = N * M - (len(area_ONE) + 3) - count
    max_safe = max(max_safe, temp_safe)

print(max_safe)

