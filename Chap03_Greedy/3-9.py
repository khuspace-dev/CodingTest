# 무지의 먹방 라이브 
# chap3. 316 page 
# https://school.programmers.co.kr/learn/courses/30/lessons/42891

# N = 음식의 개수

'''
# first

def solution(food_times, k):
    length = len(food_times)
    answer = k % length - 1         # index니까 1 뺀 것, 원래 있어야 할 point
    cycle = k // length             # 몇 바퀴를 도냐
    
    for i in range(length):
        if food_times[i] < cycle:   # 바퀴수보다 값이 작으면, 한 칸 밀기
            answer += 1
    
    answer %= length                # length보다 길어진다면, 다시 나눗셈으로 죽이기 
    
    # 다 먹은 경우 -1 반환
    if sum(food_times) <= k:
        return -1 
    
    return answer
'''

'''
# second

def solution(food_times, k):
        
    # 다 먹은 경우 -1 반환
    if sum(food_times) <= k:
        return -1 
    
    length = len(food_times)
    
    for i in range(k):
        if food_times[i%length] != 0:
            food_times[i%length] -= 1
        else:
            continue
            
    return i%length
'''

# 3rd 

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    length = len(food_times)
    time = 0
    eaten = 0

    while eaten < k:                            # k번 먹는거랑, 현재 포인터(time) 구분하기
        if food_times[time % length] != 0:      
            food_times[time % length] -= 1      # 음식을 먹었다!
            eaten += 1                          
        time += 1                               # 시간 흐르기

    # k초 후 남아 있는 음식 중 다음 위치
    while food_times[time % length] == 0:
        time += 1

    return (time % length) + 1
