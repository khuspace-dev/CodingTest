# 위에서 아래로 
# chap6. 178 page

# N개의 수
# 이후로 수 -> 범위는 1 이상 100,000 이하의 자연수

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

nums.sort(reverse=True)

# print(nums)

for i in nums:
    print(i, end=' ')