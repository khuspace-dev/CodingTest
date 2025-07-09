# 자물쇠와 열쇠
# chap4. 325 page
# https://school.programmers.co.kr/learn/courses/30/lessons/60059

# key = M * M
# lock = N * N
# M <= N
# 0은 홈, 1은 돌기 
# lock은 고정, key를 움직여, lock's 0을 채우는지 check 

import numpy as np

# 이동 방향 (동, 남, 서, 북)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

M = len(key)
N = len(lock)

def rotate(key):
    return [list(row) for row in zip(*key[::-1])]

def solution(key, lock):
    answer = False
    
    while(True):
        for i in range(4):
            key = rotate(key)

            # move 하는 로직 추가해야됨

            if key + lock == np.ones((N, N)):
                answer = True
                break
            else:
                continue
    return answer