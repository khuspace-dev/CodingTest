# 숫자 카드 게임 
# chap3. 96 page 

# N = rows, 가로줄 선택
# M = cols, 새로로 카드 선택 

rows, cols = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(rows)]

output = 0

for i in range (rows):
    if output <= min(cards[i]):
        output = min(cards[i])       # 더 큰 min으로 output을 update 

print(output)

