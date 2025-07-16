# 두 배열의 원소 교체
# chap6. 182 page

# 두 배열 A, B는 N개의 원소 
# 최대 K 번의 바꾸기 
# A 배열의 sum이 max, 최댓값 출력 

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] <= B[i]:
        A[i], B[i] = B[i], A[i]

print(sum(A))

