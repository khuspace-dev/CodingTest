# 못생긴 수 
# chap8. 381 page

# 못생긴 수 : 2, 3, 5 만 소인수로 갖는 수 
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ... 
# 입력 N -> nth 못생긴 수 출력 (N <= 1000)

N = int(input())

# N까지 못생긴 수의 개수 
dp = [0] * 1000

for i in range(1000):
    if i % 2 == 0: 
        dp[i] = dp[i//2] + 1
    elif i % 3 == 0:
        dp[i] = dp[i//3] + 1
    elif i % 5 == 0:
        dp[i] = dp[i//5] + 1
    else:
        continue

count = 0 

for i in dp:
    if count == N:
        print(i)
        break
    else:
        if i == 0:
            pass
        else:
            count += 1