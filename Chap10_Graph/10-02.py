# 도시 분할 계획
# chap10. 300 page
# https://www.acmicpc.net/problem/1647

# N개의 집, M개의 길 (무방향)
# 마을을 2개로 분할 + 길은 최소 비용으로
# 2개의 최소 신장 비용 트리 -> 크루스칼 

# A, B, C(cost)
# 길을 없애고 남은 최소 유지비(cost) 출력 

# 백준 시간초과 -> input sys로 받기 
import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
parent = [0] * (N + 1)

edges = []
result = 0

# 자기 자신으로 테이블 초기화 
for i in range(1, N + 1):
    parent[i] = i

# 서로소 집합 연산 
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

# 간선 cost 정보 (for 정렬)
for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 정렬하기
edges.sort()

# 제일 마지막 cost가 최댓값 -> 얘를 기준으로 끊으면 됨 
max_cost = 0

# 크루스칼 알고리즘 
for edge in edges:
    cost, a, b = edge

    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        max_cost = cost

print(result - max_cost)

'''
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
'''