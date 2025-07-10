# 외벽 점검
# chap4. 335 page
# https://school.programmers.co.kr/learn/courses/30/lessons/60062

# 외벽의 총 둘레 n 미터
# 정북 지점 0, 시계방향으로 거리 
# weak = 취약 지점 배열 
# dist = 1시간 동안 친구들이 이동 가능한 거리 (시계 or 반시계)

def solution(n, weak, dist):
    answer = 0
    
    diff = []
    weak.append(weak[1] + n) # 맨 끝에 12 더한 값 추가 
    
    for i in range(len(weak) - 1):
        diff.append(abs(weak[i] - weak[i + 1]))
    
    if max(diff) > max(dist):
        return -1
    
    # now what?
    # 친구들 붙이기 (최소 친구 구하기)
        
    return answer
