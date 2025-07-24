# 1로 만들기 
# chap8. 217 page

# 주어진 정수 N
# 할 수 있는 연산 -> 5로 나누기, 3으로 나누기, 2로 나누기, 1 빼기
# 연산 횟수의 최솟값 반환 

N = int(input())
count = 0

# # Greedy 구현 -> 정답 X 
# while N > 1:
#     if N % 5 == 0:
#         count += 1
#         N //= 5
#         continue
#     elif N % 3 == 0:
#         count += 1
#         N //= 3
#         continue
#     elif N % 2 == 0:
#         count += 1
#         N //= 2
#         continue
#     else:
#         count += 1
#         N -= 1
#         continue

# Dynamic Programming 구현
# 이 변형될 N들에 대한 정보를 담는 dp table
dp_list = [0] * (N + 1)

for i in range(2, N+1):
    # 왜 마이너스 1 연산이 제일 위에 -> 기본 연산이기 때문
    # 나머지도 가능하다면? -> 덮어쓰는 구조 
    # for문 연산이 왜 2부터 시작되는지 잘 이해 X -> 피보나치 list 구현처럼 생각하기
    
    dp_list[i] = dp_list[i-1] + 1

    if i % 5 == 0:
        # count + 1이 이런 식으로 테이블에 저장되는 것 
        dp_list[i] = min(dp_list[i], dp_list[i//5] + 1) # 기존 값 재활용 하는 것 !
    if i % 3 == 0:                                      # 그때까지의(작은 수) 연산 결과를 가져오는 것
        dp_list[i] = min(dp_list[i], dp_list[i//3] + 1) # update를 안해도 됨!
    if i % 2 == 0:
        dp_list[i] = min(dp_list[i], dp_list[i//2] + 1)

print(dp_list[N])
