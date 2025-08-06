# 여행 계획 
# chap10. 393 page

# 여행지 N개, 여행 계획은 M개 
# N * N 행렬 -> 연결 여부 (1)
# 마지막 줄 -> 여행 계획 
# 가능한지 출력 -> Spanning Tree - Find & Union 

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0] * (N + 1)

# 일단 부모 = 자기 자신 (초기화)
for i in range(1, N + 1):
    parent[i] = i

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x > y:
        parent[x] = y
    else:
        parent[y] = x

for i in range (1, N + 1):
    input_list = list(map(int, input().split()))

    for j in range(1, N + 1):
        # 여기서는 index가 0부터 적용되어야하니까 (index 주의)
        if input_list[j - 1] == 1:
            union(parent, i, j)

# 경로 -> find를 써야 함 
path = list(map(int, input().split()))

origin = find(parent, path[0])

for j in path[1:]:
    if find(parent, j) != origin:
        print("NO")
        break
else:
    print("YES")


'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''