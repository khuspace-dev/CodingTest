# 문자열 뒤집기
# chap3. 313 page 

# S = 주어진 문자열 

S = list(map(int, input()))
count = 0

diff = 0                    # 변동하는 point 찾기

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        diff +=1 

count = (diff+1) // 2       # 변동점 1개 -> 1, 2개 -> 1, 3개 -> 2, 4개 -> 2, 5개 -> 3 ... 
print(count)                # 따라서 1을 더해준 상태에서, 2로 나눈 몫이 답 (Cycle처럼 그림 그리기)