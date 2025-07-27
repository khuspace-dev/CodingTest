# 금광
# chap8. 375 page

# N * M 금광 -> 오른쪽 대각선 아래 · 위, 오른쪽 이동 가능 
# 가장 많이 얻을 수 있는 금 출력하기
# 첫번째 열의 아무 행에서나 시작 가능 

T = int(input())

for _ in T:
    N, M = map(int, input().split())
    maps = [int(input()) for _ in range(N * M)] 

