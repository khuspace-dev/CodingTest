# 럭키 스트레이트
# chap4. 321 page

# N = 점수 
# 항상 짝수 길이

N = input()
length = len(N)

left_sum = 0
right_sum = 0 

for i in range(length // 2):
    left_sum += int(N[i])

for i in range(length // 2):
    right_sum += int(N[i + length // 2])

if right_sum == left_sum:
    print("LUCKY")
else: 
    print("READY")