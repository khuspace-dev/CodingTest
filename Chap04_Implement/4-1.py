# 왕실의 나이트
# chap4. 115 page

# pos = init 위치 (a1 -> a를 숫자에 매핑해야 함)

pos = input()

col = ord(pos[0]) - ord('a') + 1
row = int(pos[1])

# 나이트 이동 가능한 8가지 경우의 수 (dx, dy)
dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

count = 0 

for i in range(8):
    move_x = row + dx[i]
    move_y = col+ dy[i]

    if 1 <= move_x <= 8 and 1<= move_y <= 8:
        count += 1

print(count)