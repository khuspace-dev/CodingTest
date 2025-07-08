# 게임 개발 
# chap4. 118 page

# N M = map size
# x y = init position 
# direction = init direction 
# 0 = 육지, 1 = 바다 
# 0 1 2 3 = 북 동 남 서 

N, M = map(int, input().split())
cur_x, cur_y, cur_d = map(int, input().split())

maps = []
for _ in range(N): maps.append(list(map(int, input().split())))

visit = [[0] * M for _ in range(N)]
visit[cur_x][cur_y] = 1 

count = 1
turns = 0 # 회전 count

# 북 동 남 서 (의왼쪽) -> 서 북 동 남 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 동서남북 방향 (북 동 남 서)
directions = [0, 1, 2, 3]
 
temp_x = 0
temp_y = 0

while(True):
    # 현재 dir에서 왼쪽으로 회전 (북 서 남 동) -> 0 3 2 1 0 3 2 1 ... 
    cur_d = (cur_d - 1) % 4
    temp_x = cur_x + dx[cur_d]
    temp_y = cur_y + dy[cur_d]
        
    if maps[temp_x][temp_y] == 0 and visit[temp_x][temp_y] == 0:
        visit[temp_x][temp_y] = 1
        cur_x = temp_x
        cur_y = temp_y
        count += 1
        turns = 0 # 초기화
        continue
    else:
        turns += 1 # 회전만 한다

    if turns >= 4:
        # cur_d는 유지, 뒤로 한 칸
        # 북 -> 남, 동 -> 서, 남 -> 북, 서 -> 동
        back_x = cur_x + dx[(cur_d - 1)%4]
        back_y = cur_y + dy[(cur_d - 1)%4]

        if maps[back_x][back_y] == 0:
            cur_x = back_x
            cur_y = back_y
        else:
            break # 끝난 것 
        
print(count)