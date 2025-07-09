# 뱀
# chap4. 327 page

# N = 보드의 크기 N * N
# K = 사과의 개수 
# L = 뱀의 방항 변환 횟수
# 정수 X 초 이후, L or D

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input())
moves = [input().split() for _ in range(L)]
moves = [(int(sec), direct) for sec, direct in moves]

seconds = 0
maps = [[0]*N for _ in range(N)]

# apples를 maps에 표기
# maps가 1이라면, 사과가 존재함 
for i in range(K):
    apple_x, apple_y = map(int, input().split())
    maps[apple_x - 1][apple_y - 1] = 1  

head = [1, 1]
tail = [1, 1]

cur_d = 0 # 초기 방향은 오른쪽 
direction = [0, 1, 2, 3] # 동, 남, 서, 북 

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while(True):
    if head[0] >= N or head[1] >= N or tail[0] >= N or tail[1] >= N:
        break

    head[0] += dx[cur_d] 
    head[1] += dy[cur_d]

    if maps[head[0]][head[1]] == 1: 
        seconds += 1 
    else:
        tail[0] += dx[cur_d] 
        tail[1] += dy[cur_d]
        seconds += 1 

    # 특정 seconds에서 회전하기 추가 



print(seconds)