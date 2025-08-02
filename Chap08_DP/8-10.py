# 편집 거리 
# chap8. 382 page

# 편집 거리 = 문자열 A 편집 -> 문자열 B 로 만들기 위한 연산의 수 (최소 편집 거리 출력)
# 가능한 연산 = insert, remove, replace 

A = input()
B = input()

dp = [] 

for i in range(len(A) + 1):
    dp.append([0] * (len(B) + 1))

# 처음 세로줄 채우기 -> Ø s u n d a y 
for i in range(len(A) + 1):
    dp[i][0] = i 

# 처음 가로줄 채우기 -> Ø s a t u r d a y 
for j in range(len(B) + 1):
    dp[0][j] = j 

# 여기서부터 DP 2차원 테이블 채우기 
for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):

        # 문자가 동일한 경우의 점화식 
        if A[i - 1] == B[j - 1]:  
            dp[i][j] = dp[i - 1][j - 1]
        
        # 문자가 다를 경우 -> 편집 연산
        else:
            dp[i][j] = min(
                dp[i - 1][j] + 1,       # 삭제
                dp[i][j - 1] + 1,       # 삽입
                dp[i - 1][j - 1] + 1    # 교체
            )

print(dp[len(A)][len(B)]) 