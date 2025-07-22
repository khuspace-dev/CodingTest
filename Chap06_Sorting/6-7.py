# 카드 정렬하기
# chap6. 363 page
# https://www.acmicpc.net/problem/1715

# 두 묶음을 합쳐서 하나로 -> A + B 번 비교
# N = 숫자 카드 뭉치 개수
# output = 최소 비교 count 

# N = int(input())
# cards = [int(input()) for _ in range(N)]
# # count = 0

# # cards = []
# # for i in range(N):
# #     cards.append(int(input()))

# cards.sort()
# for i in range(N-1):
#     first_min = min(cards)
#     cards.remove(first_min)
#     second_min = min(cards)
#     cards.remove(second_min)

#     merged_card = first_min + second_min
#     cards.append(merged_card)

# print(cards[0])



# Second * 그래도 시간 초과 

# N = int(input())
# cards = [int(input()) for _ in range(N)]
# cards.sort()

# for i in range(N-1):
#     first_min = cards[0]
#     cards.remove(first_min)
#     second_min = cards[1]
#     cards.remove(second_min)

#     merged_card = first_min + second_min
#     cards.append(merged_card)
#     cards.sort()

# print(cards[0])


# Third - heap

import heapq

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards) 
count = 0

while len(cards) > 1:
    first_min = heapq.heappop(cards)
    second_min = heapq.heappop(cards)
    merged_card = first_min + second_min

    count += merged_card
    heapq.heappush(cards, merged_card)
    # merged_card 더하면서, 자동 정렬 

print(count)