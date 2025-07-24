# 정렬된 배열에서 특정 수의 개수 구하기
# chap7. 367 page

# N개 원소를 포함한 수열, 오름차순으로 정렬
# x 개수 print
# 단, O(log N) 이상은 시간 초과 

N, X = map(int, input().split())
nums = list(map(int, input().split()))

# count method = O(n)
# print(nums.count(X))

# BS 사용해보기
def binarySearch(nums, target, start, end):
    while(start <= end):
        mid = (start + end) // 2 
        if nums[mid] > target:
            end = mid - 1           # 1 처리 주의 
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid              # index를 반환시킬 수 있음
    
    return None

# 1과 3의 index를 안다면? -> 중복이라 어려울 것 같음
# 제일 작은 2랑 제일 큰 2 index need -> 빼면 2들의 길이가 됨

def first_bin(nums, target, start, end):
    while (start < end):
        mid = (start + end) // 2 
        if nums[mid] >= target:             # 같더라도 더 앞으로 밀어붙여야 함
            end = mid
        else:
            start = mid + 1                 

    return start                            # 잘 이해 X

def second_bin(nums, target, start, end):
    while(start < end):
        mid = (start + end) // 2 
        if nums[mid] > target:
            end = mid 
        else:
            start = mid + 1                 # 이 범위가 이해 X 

    return start

print(second_bin(nums, X, 0, N) - first_bin(nums, X, 0, N)) 