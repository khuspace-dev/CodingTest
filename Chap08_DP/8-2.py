# 개미 전사
# chap8. 220 page

# 식량 창고 N개 일직선 상 -> 인접 창고 털면 X
# 각 창고에 저장된 식량 개수 K (foods)

N = int(input())
foods = list(map(int, input().split()))

dp = [0] * (N)

