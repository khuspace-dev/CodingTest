# 미로 탈출
# chap5. 152 page 

# N X M 직사각형 미로
# init 위치 (1, 1), 출구는 (N, M)
# 괴물 0, 없는 곳은 1 
# 1들을 따라서 m, n까지 가야함 
# output: 탈출하기 위해 움직이는 최소 칸 개수 

from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

# 동 남 서 북 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

path = 0

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            # 범위 밖 or 괴물이 있다면 pass 
            if not (0 <= temp_x < M and 0 <= temp_y < N):
                continue

            if maps[temp_y][temp_x] == 0:
                continue

            if maps[temp_y][temp_x] == 1:
                    # 기존까지의 값에, 지금 한 칸을 더한것으로 저장
                    maps[temp_y][temp_x] = maps[y][x] + 1
                    queue.append((temp_x, temp_y))

    # indexing - 1 
    # 가장 끝 칸까지 올 때, 최소거리 반환
    return maps[N - 1][M - 1] 

# 항상 첫 칸에서 시작
path = bfs(0, 0)
print(path)