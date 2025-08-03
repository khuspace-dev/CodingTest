# Chap10. 그래프 이론
'''
- 다익스트라 heapq -> 인접 리스트
- 노드의 개수만큼 리스트를 만들어, 각 노드와 연결된 간선 정보 저장 
- ex) graph[a].append(b, cost)

- 플로이드 워셜 -> 인접 행렬
- 모든 노드 to 다른 노드 (노드^2) 비용을 행렬에 저장 
- 노드의 개수가 적은 경우에만 사용 가능 O(N^3)

* 서로소 집합 - 공통 원소가 없는 두 집합
- union : 합집합 연산
- find : 특정 원소가 속한 집합 반환 

- 번호가 작은 원소 : 부모가 됨
- 자식 -> 부모 가리킴 (부모로 설정함)
- root를 확인하기 위해, 재귀적으로 부모를 찾아나감

'''

'''
def find_parent(parent, x):
    if parent[x] != x:
        # 루트가 아니라면 -> 루트 도달까지 재귀 호출
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        # 더 작다 -> a가 부모가 됨 (b가 a를 가리킴)
        parent[b] = a
    else:
        parent[a] = b

# v = 노드, e = 간선
v, e = map(int, input().split())
parent = [0] * (v + 1) 

# 0은 버리고 시작
for i in range(1, v + 1):
    parent[i] = i

# 간선의 수 만큼 union
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()
print('부모 테이블: ', end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')

# 1부터 시작하도록 범위가 (1, v+1)

''' 

'''
* find 함수 최적화 -> 경로 압축
- find가 모든 노드를 탐색 -> 최악의 경우 O(V)
- 경로 압축: 재귀로 find 호출 후, 부모 테이블 값을 갱신시킴

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

'''

'''
* 서로소 집합을 활용한 사이클 판별 
- 간선으로 연결된 두 노드 -> 둘의 루트 노드가 같다면? -> cycle 발생 


cycle = False

for i in range(e):
    a, b = map(int, input().split())

    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

'''

'''
* 신장 트리 = Spanning Tree
- 모든 노드를 포함하며, 사이클이 존재 X 

* 크루스칼 알고리즘 : Greedy
- 최소한의 비용으로 신장 트리를 찾자: 최소 신장 트리 알고리즘 
- 간선 정렬 -> 가장 짧은 간선부터 집합에 포함 (사이클 발생 시 pass)

- 사이클 판별 : 둘의 루트가 같은지 check 
- 최종 간선 개수 = 노드의 개수 - 1 (E = V - 1)
- 시간 복잡도 : ElogE 


'''

'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(v+ 1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용으로 정렬하기 위해 cost 먼저
    edges.append((cost, a, b))

# 최소 신장 비용 트리 -> edge로 정렬 
edges.sort()

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        result += cost

print(result)

'''

'''
* 위상 정렬 : Topology Sort
- 방향 그래프의 모든 노드 -> 방향성 거스르지 않도록 순서대로 나열
- ex) 선수 과목을 고려한 학습 순서 설정 

- 진입 차수 : 해당 노드로 들어오는 간선의 개수
- start: 진입 차수 0인 노드를 큐에 넣고 
-> pop, 해당 노드에서 출발하는 간선을 그래프에서 제거  
-> 새롭게 진입 차수가 0이 된 노드를 큐에 넣는다 

- 큐에서 원소가 V번 추출되기 전, 큐가 비면? -> Cycle 발생 
- 간선들을 끊으며, next 0노드를 만들어 가는 과정에서
- 큐에서 빠져나간 순서 = 위상정렬  / 답이 여러개 가능함
- 시간 복잡도 : O(V + E)

'''

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v + 1) # 진입 차수 0으로 초기화

# 연결 리스트 : 각 노드와 연결된 e 정보 저장하려고 
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # a -> b
    indegree[b] += 1    # b의 진입차수 ++

def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 큐에서 나온 순서대로 위상 정렬 결과니깐
        result.append(now)

        # now 노드랑 연결된 노드(i)와의 간선 끊기
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()