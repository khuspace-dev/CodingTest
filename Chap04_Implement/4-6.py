# 자물쇠와 열쇠
# chap4. 325 page
# https://school.programmers.co.kr/learn/courses/30/lessons/60059

# key = M * M
# lock = N * N
# M <= N
# 0은 홈, 1은 돌기 
# lock은 고정, key를 움직여, lock's 0을 채우는지 check 

def rotate(key):
    return [list(row) for row in zip(*key[::-1])]

def solution(key, lock):
    answer = False

    M = len(key)
    N = len(lock)

    new_map = [[1] * (2 * N + M) for _ in range(2 * N + M)]
    
    for y in range(N):
        for x in range(N):
            new_map[y + M][x + M] = lock[y][x]

    for _ in range(4):
        key = rotate(key) # 회전된 키 

        # 키를 움직이는 것
        for i in range(1, N + M):
            for j in range(1, N + M):

                # 특정 위치의 키를 더해주는 것 
                for y in range(M):
                    for x in range(M):                
                        new_map[i + y][j + x] = new_map[i + y][j + x] + key[y][x]
                
                flag = True

                for y in range(N):
                    for x in range(N):
                        if new_map[M+y][M+x] != 1:
                            flag = False
                
                if flag == True:
                    answer = True 
                
                # 더해진 key를 다시 빼주어야 한다. 
                for y in range(M):
                    for x in range(M):                
                        new_map[i + y][j + x] = new_map[i + y][j + x] - key[y][x]

    return answer