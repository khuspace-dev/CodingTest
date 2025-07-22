# 카드 정렬하기
# chap6. 363 page

# 두 묶음을 합쳐서 하나로 -> A + B 번 비교
# N = 숫자 카드 뭉치 개수
# output = 최소 비교 count 

N = int(input())
cards = [int(input()) for _ in range(N)]
# count = 0

# cards = []
# for i in range(N):
#     cards.append(int(input()))

cards.sort()
for i in range(N-1):
    first_min = min(cards)
    cards.remove(first_min)
    second_min = min(cards)
    cards.remove(second_min)

    merged_card = first_min + second_min
    cards.append(merged_card)

print(cards[0])