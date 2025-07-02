# 곱하기 혹은 더하기 
# chap3. 312 page 

# S = 주어진 문자열 

S = list(map(int, input()))

output = 0
temp = 1                        # 곱셈 초기화 == 1 

for i in S:
    if i == 0:
        if temp != 1:           # 0에서 1이 더해진 값이 나옴 (조건문 추가)
            output += temp      # 지금까지 곱해진 결과를 output에 더하고
            temp = 1            # temp는 비운다
    else: 
        temp = temp * i         # temp에 곱해주기 

output += temp                  # 마지막에도 더해줘야 한다. 
print(output)

# 다른 풀이 찾아보기 