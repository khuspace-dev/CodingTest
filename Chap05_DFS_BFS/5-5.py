# 경쟁적 전염 
# chap5. 344 page 

# N X N
# K : 바이러스 개수
# S초 -> (X, Y)칸 바이러스 (마지막 줄 S X Y)

from collections import deque

N, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

# 동 남 서 북 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]




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