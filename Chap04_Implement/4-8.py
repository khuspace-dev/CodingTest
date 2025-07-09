# 기둥과 보 설치 
# chap4. 329 page
# https://school.programmers.co.kr/learn/courses/30/lessons/60061

# n = 벽면의 크기
# build_frame 구성요소 = [x, y, a, b]
# x, y = 교차점의 좌표
# a = 기둥은 0, 보는 1
# b = 삭제는 0, 설치는 1 
# ruturn 배열 = [x, y, a], 해당 교차점에서 0은 기둥, 1은 보

def solution(n, build_frame):
    maps = [[]]   

    for trial in build_frame:
        x = trial[0]
        y = trial[1]
        types = trial[2]
        built = trial[3]

        if types == 0 and built == 1:           # 기둥 설치 
            if y == 0 :
                maps.append([x, y, 0])

        elif types == 0 and built == 0:         # 기둥 삭제

            maps.remove([x, y, 0])

        elif types == 1 and built == 1:         # 보 설치
            maps.append([x, y, 1])

        else:                                   # 보 삭제
            maps.remove([x, y, 1])

    return maps