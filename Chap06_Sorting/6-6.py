# 실패율
# chap6. 361 page
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

# 전체 스테이지의 개수 N개 (!= 사람 명수랑은 다름) 
# stage: 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
# 실패율 = 스테이지에 도달 + 아직 클리어 X 플레이어의 수 / 스테이지에 도달한 플레이어의 수

def solution(N, stages):
    clear = []
    players = len(stages)
    
    for i in range(1, N + 1):
        if players <= 0: # 분모 0인 경우 추가 구현
            cur_fail = 0
        else:
            cur_fail = stages.count(i) / players
        
        clear.append((i, cur_fail))
        players -= stages.count(i)
        
    # cur_fail 내림차순, 스테이지는 오름차순 
    clear.sort(key=lambda x: (-x[1], x[0])) # 실패율 먼저 고려하려고 [1] 우선 처리   
    
    answer = []
    for stage, failure in clear:
        answer.append(stage)
        
    return answer