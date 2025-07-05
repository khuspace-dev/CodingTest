# 게임 개발 
# chap4. 118 page

# N M = map size
# x y = init position 
# dir = init direction 
# 0 = 육지, 1 = 바다 

N, M = map(int, input().split())
cur_x, cur_y, dir = map(int, input().split())

maps = []
for _ in range(N): maps.append(list(map(int, input().split())))

visit = [[0] * M for _ in range(N)]
visit[cur_x][cur_y] = 1 

count = 0 
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

temp_x = 0
temp_y = 0

for i in range(N * M):
    for i in range(4):
        temp_x += dx[i]
        temp_y += dy[i]
        
        if maps[cur_x][cur_y] == 0:
            cur_x = temp_x
            cur_y = temp_y

print(count + 1)