# 만들 수 없는 금액
# chap3. 314 page 

# N = 주어진 동전의 개수
# coins = N개 각 동전들의 화폐 단위 (중복 가능)

N = int(input())
coins = list(map(int, input().split()))
coins.sort()

if coins[0] != 1:
    print(1)                # 처음이 1이 아니라면, 정답이 1로 끝
    exit

else: 
    sum = 1
    for i in coins:         # coins에서 차례로 더하다가, sum보다 더 큰 수가 나오면 거기서 blank
        if sum >= i:        # 1로 시작, print(sum+1)이 아니라 (하나 더 큰 수), 그냥 sum 반환
            sum += i
    print(sum)