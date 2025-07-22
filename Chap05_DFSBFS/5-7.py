# 연산자 끼워 넣기
# chap5. 349 page 

# N = 수의 개수
# 2nd: 수열
# 3rd: 합이 N ― 1, + = * / 개수

import sys

N = int(input())
num_list = list(map(int, input().split()))
n_add, n_sub, n_mul, n_div = map(int, input().split())

# system min, max 값
min_value = sys.maxsize
max_value = -1 * sys.maxsize - 1

def dfs(step, cur_value):
    global min_value, max_value, n_add, n_sub, n_mul, n_div

    if step >= N :
        min_value = min(min_value, cur_value)
        max_value = max(max_value, cur_value)

    else:
        if n_add > 0:
            n_add -= 1
            dfs(step + 1, cur_value + num_list[step])
        
        if n_sub > 0:
            n_sub -= 1
            dfs(step + 1, cur_value - num_list[step])

        if n_mul > 0:
            n_mul -= 1
            dfs(step + 1, cur_value * num_list[step])

        if n_div > 0:
            n_div -= 1
            dfs(step + 1, cur_value / num_list[step])

# init 값은 첫번째 요소 값으로 지정해야 한다. 
dfs(1, num_list[0])

print(max_value)
print(min_value)

# 2nd TC 틀렸다. 