# 큰 수의 법칙 
# chap3. 92 page 

# N = 주어질 배열의 크기 
# M = 숫자가 더해질 총 횟수 
# K = 연속해서 더하기 가능한 횟수

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
outcome = 0 

first_max = max(nums)
nums.remove(first_max)
second_max = max(nums)

sets = M // (K+1)       # 몇 세트인지 의미 (만약 3회가 max라면, f f f s 이걸 1세트로 본다, 따라서 K+1)
leftover = M % (K+1)    # 나머지는 f로 채우기 

outcome += sets * (K * first_max + second_max)      # 한 세트씩 더해주고 
outcome += leftover * first_max                     # 나머지 칸은 first_max로 채우기 

print(outcome)