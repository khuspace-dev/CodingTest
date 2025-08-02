# 못생긴 수 
# chap8. 381 page

# 못생긴 수 : 2, 3, 5 만 소인수로 갖는 수 
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... 
# 입력 N -> nth 못생긴 수 출력 (N <= 1000)

N = int(input())

# first
# # N까지 못생긴 수의 개수 
# dp = [0] * 1000

# for i in range(1000):
#     if i % 2 == 0: 
#         dp[i] = dp[i//2] + 1
#     elif i % 3 == 0:
#         dp[i] = dp[i//3] + 1
#     elif i % 5 == 0:
#         dp[i] = dp[i//5] + 1
#     else:
#         continue

# count = 0 

# for i in dp:
#     if count == N:
#         print(i)
#         break
#     else:
#         if i == 0:
#             pass
#         else:
#             count += 1


# second
dp = [0] * N  
dp[0] = 1     # 첫 번째 못생긴 수 = 1 

i2 = i3 = i5 = 0

# next target
next2, next3, next5 = 2, 3, 5

for i in range(1, N):
    dp[i] = min(next2, next3, next5)

    # 다음 못생긴 수로 2의 배수가 선택되는 상황 
    if dp[i] == next2: 
        i2 += 1
        next2 = dp[i2] * 2 # 다음 * 2의 못생긴 수 후보를 next2로 지정 (update)
    
    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3

    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

# print(dp)
print(dp[N - 1])

# [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
# 0th index -> ith 못생긴 수 (따라서 1 빼서 접근)