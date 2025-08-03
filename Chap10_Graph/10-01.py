# 팀 결성
# chap10. 298 page

# 서로소 연산 
# 총 N + 1 명의 학생, M번의 연산 
# union = 0, a, b
# find = 1, a, b
# find 연산 -> YES or NO 출력 

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

for i in range(M):
    flag, a, b = map(int, input().split())

    if flag == 1:
        if find(parent, a) == find(parent, b):
            print("YES")
        else:
            print("NO")

    # flag 0 => union(a, b)
    else:
        union(parent, a, b)

'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
'''