# 1이 될 때까지
# chap3. 99 page 

# N = 대상이 될 숫자
# K = 나누기

import math

N, K = map(int, input().split())
count = 0

mok = math.log(N, K)
left = N % K

count = mok + left
print(int(count))