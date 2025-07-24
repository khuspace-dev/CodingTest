# 고정점 찾기 
# chap7. 368 page

# 수열의 원소 중 값 == 인덱스
# 수열 원소의 개수 N개
# 고정점은 최대 1개, 없다면 -1 출력 
# O(log N) 이상은 시간 초과 

N = int(input())
nums = list(map(int, input().split()))

# 수열을 절반씩 나누어 검사 
# target이 아니라, 해당 값과 index로 비교해야 할 듯

def binarySearch(nums, start, end): 
    while (start <= end):
        mid = (start + end) // 2
        if nums[mid] == mid:
            return mid
        elif nums[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1

    return -1

print(binarySearch(nums, 0, N))