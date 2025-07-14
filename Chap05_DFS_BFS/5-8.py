# 감시 피하기 
# chap5. 351 page 

# N * N = 복도 크기
# 학생 S, 선생님 T, 공백은 X
# 3개의 장애물 설치, 상하좌우 4칸 감시

from itertools import combinations # 3칸 조합 쓰려고 

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

# 동 남 서 북 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, maps):

    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]

        if not (0 <= temp_x < N and 0 <= temp_y < N):
            if map[temp_y][temp_x] == 'S' :
                return True
            if map[temp_y][temp_x] == 'O' :
                break
            
    return False


print(dfs(0, 0, maps))