# 1이 될 때까지
# chap3. 99 page 

# N = 대상이 될 숫자
# K = 나누기

import math

N, K = map(int, input().split())
count = 0

mok = math.log(N, K)    # 나머지 연산이 아니라, 로그로 해야함 (연달아 나누기)
left = N % K            # 찌꺼기는 계속 1 빼기 때문에, 그냥 더한다 

count = mok + left      # 빼는 횟수 + 로그한 값 

print(int(count))