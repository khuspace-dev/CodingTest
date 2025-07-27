# 정수삼각형
# chap8. 376 page
# https://www.acmicpc.net/problem/1932

# 맨 꼭대기에서 시작 -> 선택한 합이 최대가 되는 경로 (합을 출력하면 됨)
# 아랫층의 수는 현재 층에서 대각선 왼 or 오른쪽만 선택 가능 -> 아까 문제와 유사하다

N = int(input()) # 전체 정수의 개수 = N * (N + 1) // 2
# triangle = [[0] * N for _ in range(N)] # N * N 행렬 선언
triangle = []

# for j in range(N):
#     for i in range(j):
#         triangle[j][i] = int(input())

for _ in range(N):
    triangle.append(list(map(int, input().split())))
        
# dp = [[0] * N for _ in range(N)]

# for j in range(N):
#     for i in range(j):
#         dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])

# i = 세로 줄 (step)
# j = 가로 위치 
for i in range(1, N):
    for j in range(len(triangle[i])):
        if j == 0:                                  # 첫번째는 선택권 X (무조건 오른쪽 위)
            triangle[i][j] += triangle[i-1][j]
        elif j == len(triangle[i]) - 1:             # 마지막도 선택권 X (무조건 왼쪽 위)
            triangle[i][j] += triangle[i-1][j-1]
        else:                                       # 가장 기본 점화식 
            triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])

print(max(triangle[N-1]))