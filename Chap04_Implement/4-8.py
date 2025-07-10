# 기둥과 보 설치 
# chap4. 329 page
# https://school.programmers.co.kr/learn/courses/30/lessons/60061

# n = 벽면의 크기
# build_frame 구성요소 = [x, y, a, b]
# x, y = 교차점의 좌표
# a = 기둥은 0, 보는 1
# b = 삭제는 0, 설치는 1 
# ruturn 배열 = [x, y, a], 해당 교차점에서 0은 기둥, 1은 보

# first trial
# def solution(n, build_frame):
#     maps = [[]]   

#     for trial in build_frame:
#         x = trial[0]
#         y = trial[1]
#         types = trial[2]
#         built = trial[3]

#         if types == 0 and built == 1:           # 기둥 설치 
#             if (y == 0 
#                 or [x, y-1, 0] in maps 
#                 or [x, y, 1] in maps 
#                 or [x-1, y, 1] in maps):
#                 maps.append([x, y, 0])

#         elif types == 0 and built == 0:         # 기둥 삭제
#             if ([x, y+1, 0] not in maps 
#                 and [x, y+1, 1] not in maps
#                 and [x-1, y+1, 1] not in maps):
#                 maps.remove([x, y, 0])

#         elif types == 1 and built == 1:         # 보 설치
#             if ([x, y-1, 0] in maps
#                 or [x+1, y-1, 0] in maps
#                 or ([x-1, y, 1] in maps and [x+1, y, 1] in maps)):
#                 maps.append([x, y, 1])

#         else:                                   # 보 삭제
#             if ([x, y, 0] not in maps
#                 and [x+1, y, 0] not in maps):
#                 # 끄트머리에 달린 경우도 고려해야한다 -> GG
#                 maps.remove([x, y, 1])

#     return maps

# second trial 

def isValid(maps):
    for x, y, types in maps:
        if types == 0:                      # 기둥 X -> 기둥의 설치 가능 조건을 뒤집음 
            if not (y == 0                  # 전체를 돌면서 유효성 검사를 해야하기 때문에
                or [x, y, 1] in maps        # 끝까지 문제가 없어야 -> True
                or [x-1, y, 1] in maps
                or [x, y-1, 0] in maps):
                return False 
        else:                               # 보 X -> 보의 설치 가능 조건의 역
            if not ([x, y-1, 0] in maps
               or [x+1, y-1, 0] in maps
               or ([x-1, y, 1] in maps and [x+1, y, 1] in maps)):
                return False
            
    return True

def solution(n, build_frame):
    maps = []

    for x, y, types, built in build_frame:
        cur_f = [x, y, types]

        if built == 1: # 설치
            maps.append(cur_f)
            if isValid(maps) == False:
                maps.pop()

        else: # 삭제
            maps.remove(cur_f)
            if isValid(maps) == False:
                maps.append(cur_f)
    
    s_maps = sorted(maps)
    return s_maps