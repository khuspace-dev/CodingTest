# 뱀
# chap4. 327 page

# N = 보드의 크기 N * N
# K = 사과의 개수 
# L = 뱀의 방항 변환 횟수
# 정수 X 초 이후, L or D

from collections import deque

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input())
moves = [input().split() for _ in range(L)]
moves = [(int(sec), direct) for sec, direct in moves]
secs = [move[0] for move in moves]

seconds = 0
maps = [[0] * N for _ in range(N)]

# apples를 maps에 표기하기 -> maps가 1이라면, 사과가 존재함 
for i in range(K):
    apple_x, apple_y = apples[i]
    maps[apple_x - 1][apple_y - 1] = 1  

snakes = deque()
snakes.append((0, 0))

cur_d = 0 # 초기 방향은 오른쪽 
# dirs = [0, 1, 2, 3] -> 없어도 됨 
# 동, 남, 서, 북 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while(True):
    seconds += 1 
    temp_x = snakes[0][0] + dx[cur_d]
    temp_y = snakes[0][1] + dy[cur_d]

    if (temp_x, temp_y) in snakes:                  # 이미 뱀이 있는 곳 -> 죽음 
        break

    if not (0 <= temp_x < N and 0 <= temp_y < N):   # 맵 벗어남 -> 죽음
        break

    if maps[temp_x][temp_y] == 1:                   # 사과가 있다면?
        snakes.appendleft((temp_x, temp_y))         # 머리만 새로 더하기, 기존 꼬리는 유지 (사과를 먹어서!)
    else: 
        snakes.appendleft((temp_x, temp_y))         # 머리 더하기
        snakes.pop()                                # 꼬리는 제거하기 (사과 못먹어서, 길이 유지)

    # 방향 전환 처리 
    if seconds in secs:
        index = secs.index(seconds)
        if moves[index][1] == 'D':                  # 오른쪽으로 회전 
            cur_d = (cur_d + 1) % 4                 # 동 -> 남 ... 즉 + 1 
        else: 
            cur_d = (cur_d - 1) % 4                 # 왼쪽은 동 -> 북 ... 즉 - 1
 
print(seconds)



# first trial
# N = int(input())
# K = int(input())
# apples = [list(map(int, input().split())) for _ in range(K)]

# L = int(input())
# moves = [input().split() for _ in range(L)]

# seconds = 0
# maps = [N][N]

# # apples maps에 표기하기 

# head = [1, 1]
# tail = [1, 1]

# cur_d = 0 # 초기 방향은 오른쪽 
# direction = [0, 1, 2, 3] # 동, 남, 서, 북 

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# while(True):
#     if head[0] >= N or head[1] >= N or tail[0] >= N or tail[1] >= N:
#         break

#     head[0] += dx[cur_d] 
#     head[1] += dy[cur_d]

#     if maps[head[0]][head[1]] == 1: 
#         seconds += 1 
#     else:
#         tail[0] += dx[cur_d] 
#         tail[1] += dy[cur_d]
#         seconds += 1 

#     # 특정 seconds에서 회전하기 로직 추가 

# print(seconds)