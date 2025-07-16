# 감시 피하기 
# chap5. 351 page 

# N * N = 복도 크기
# 학생 S, 선생님 T, 공백은 X
# O: 3개의 장애물 설치, T: 상하좌우 4칸 감시

from itertools import combinations # 3칸 조합 쓰려고 
from copy import deepcopy

N = int(input())
maps = [input().split() for _ in range(N)]

# 동 남 서 북 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def teacher(x, y, maps):
    for i in range(4):
        temp_x = x
        temp_y = y

        while True:
            temp_x += dx[i]
            temp_y += dy[i] # dy, dx 만큼 계속 이동

            if not (0 <= temp_x < N and 0 <= temp_y < N):
                break 
            
            if maps[temp_y][temp_x] == 'S' : # 학생 만남
                return True
            if maps[temp_y][temp_x] == 'O' : # 벽
                break
    return False

# 벽을 세울 수 있는 좌표들 
empty_area = [(i, j) for i in range(N) for j in range(N) if maps[i][j] == 'X']
teachers = [(i, j) for i in range(N) for j in range(N) if maps[i][j] == 'T']

for trial in combinations(empty_area, 3):
    temp = deepcopy(maps)

    for y, x in trial:
        temp[y][x] = 'O' # 벽 세운 것 

    outcome = "YES"                     # 매 combi마다 초기화 이루어짐 

    for cur_teacher in teachers:
        y, x = cur_teacher
        if teacher(x, y, temp) == True: # 선생님이 학생을 만난 것
            outcome = "NO"              # 기본으로 대부분 NO가 찍힐 것
            break
    
    if outcome == "YES":                # 해당 combi에서 하나라도 가능한 조합이 나오면 YES 가 뜸
        print("YES")                    # YES 출력하고, 바로 종료 -> 아니라면 NO 출력 
        exit()

print("NO")