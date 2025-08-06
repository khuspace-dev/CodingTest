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

for i in range (i, N + 1):
    input_list = list(map(int, input().split()))

    # N 칸의 Parent 관계 연결해주기


