# 경쟁적 전염 
# chap5. 344 page 

# N X N
# K : 바이러스 개수
# S초 -> (X, Y)칸 바이러스 (마지막 줄 S X Y)

from collections import deque # 덱 (bfs)

N, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 동 남 서 북 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

temp = []
# 초기 상태를 큐에 입력
for y in range(N):
    for x in range(N):
        if maps[y][x] != 0:
            temp.append(((maps[y][x], 0, y, x))) # 번호, 0초, 좌표

temp.sort()
queue = deque(temp)

while queue:
    virus_type, second, y, x = queue.popleft()

    if second == S: # 주어진 시간에 도달하면 끝
        break

    for i in range(4):
        temp_x = x + dx[i] 
        temp_y = y + dy[i]

        if (0 <= temp_x < N) and (0 <= temp_y < N): # 범위 내
            if maps[temp_y][temp_x] == 0:
                maps[temp_y][temp_x] = virus_type
                queue.append((virus_type, second + 1, temp_y, temp_x))

# 여기 인덱스 주의
print(maps[X - 1][Y - 1])

# first trial
#
# maps 칸에 담긴게 바이러스 종류가 됨 
# def dfs(x, y, maps):
#     if maps[Y][X] != 0:
#         cur_virus = maps[Y][X]
        
#         for i in range(4):
#             temp_x = x + dx[i] 
#             temp_y = y + dy[i]

#             if (0 <= temp_x < N) and (0 <= temp_y < N): # 범위 내
#                 maps[temp_y][temp_x] = cur_virus
            
#             # 순차적으로 (초, 작은숫자대로) 진행 -> BFS

# print(maps[Y][X])