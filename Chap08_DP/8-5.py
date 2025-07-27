# 금광
# chap8. 375 page

# N * M 금광 -> 오른쪽 대각선 아래 · 위, 오른쪽 이동 가능 
# 가장 많이 얻을 수 있는 금 출력하기
# 첫번째 열의 아무 행에서나 시작 가능 

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    input_list = list(map(int, input().split()))

    maps = [] 
    for i in range(N):
        # M 단위로 끊어서 2차원 배열로 저장
        maps.append(input_list[i * M : (i + 1)* M])

    # dp 배열도 2차원으로 선언 
    dp = [[0] * M for _ in range(N)]

    for i in range(N):
        dp[i][0] = maps[i][0]   # 첫번째 열은 무작위로 시작 가능 (초기 조건 채우기)

    for j in range(1, M):
        for i in range(N):
            if i > 0:           # 내가 지금 첫 행이면 이전의 Up이 X
                up = dp[i-1][j-1]
            else:
                up = 0
            
            mid = dp[i][j-1]

            if i < N - 1:           # 내가 지금 마지막 행이면, 이전의 down이 X
                down = dp[i+1][j-1]
            else:
                down = 0

            # 현재칸 = 이전 칸들 중 최대값 + 현재의 금
            dp[i][j] = max(up, mid, down) + maps[i][j]
    
    max_value = max(dp[i][M - 1] for i in range(N))
    print(max_value)

# 이걸 왜 DP로 풀어야한다고 떠올릴 수 O?