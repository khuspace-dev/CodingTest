# 음료수 얼려 먹기
# chap5. 149 page 

# N = 세로
# M = 가로
# 0 = 얼음, 1 = 칸막이

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

def dfs(x, y):
    if not ((0 <= x < M) and (0 <= y < N)):
        return False        # 범위 넘으면 끝
    
    if maps[y][x] == 0 :
        maps[y][x] = 1      # 내가 얼음 하나 먹은 것 (방문함을 의미)

        # 상하좌우로 재귀 호출   # 이어진 얼음들을 찾아가려고 
        dfs(x-1, y)         # 즉, 연결된 0을 찾으려고 -> 또 0이면? Ture -> 다시 상하좌우 ... 
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)         # 싹 다 return -> 너랑 연결된 0들을 모조리 1로 바꾼 것 
        return True         # 이제 이게 새로운 덩어리라는 의미
    
    return False            # 벽 or 다른 덩어리 (이미 0->1)

ices = 0

for y in range(N):
    for x in range(M):
        if dfs(x, y) == True:
            ices += 1       # 해당 point가 새로운 얼음의 시작점

print(ices)