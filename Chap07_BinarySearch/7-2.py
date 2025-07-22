# 떡볶이 떡 만들기
# chap6. 201 page

# 떡의 개수 N 
# 손님 요청한 길이 M
# 적어도 M만큼 떡을 위해 설정할 절단기 높이의 최댓값 출력 

N, M = map(int, input().split())
heights = list(map(int, input().split()))
max_height = 0

# first
# # 긴 길이가 앞에 오도록 우선 정렬 
# heights.sort(reverse=True)

# def cut(input_list, target_height):
#     cutted_rices = [max(0, x - target_height) for x in input_list]
#     total_length = sum(cutted_rices)
#     return total_length

# height = 0
# max_rice = max(heights)

# while(True):
#     height += 1
#     output = cut(heights, max_rice - height)
#     if output >= M:
#         print(max_rice - height)
#         break



# second, 이진 탐색으로 구현할 때 -> 그림보면 이해됨 

def cut(input_list, target_height):
    return sum(max(0, x - target_height) for x in input_list)

start = 0
end = max(heights) 
# 이 범위 안에서만 가능 

max_height = 0  # 절단기 높이의 최댓값 

while start <= end: # 이진 탐색 구조 
    mid = (start + end) // 2
    total = cut(heights, mid)

    if total >= M:
        result = mid         
        start = mid + 1
    else:
        end = mid - 1

print(result)