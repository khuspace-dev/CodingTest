# Chap09. 최단 경로 
# 1. 다익스트라 -> Greedy 
# 무한 = int(1e9) 

# 1-1) O(V^2) 구현 
# 노드 수 < 5,000 가능
# 10,000 이상 node -> O(ElogV), heap 활용

'''
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split()) # a->b 비용이 c
    graph[a].append((b, c))

def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i

    return index

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드 제외한 노드들에 대해 반복 
    for i in range(n - 1):
        temp = get_smallest_node()
        visited[temp] = True
        
        for j in graph[temp]:
            cost = distance[temp] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])

'''


# 1-2) O(ElogV) 구현
# heapq 우선순위 큐 -> 우선순위 가장 높은 데이터 먼저 삭제
# 내부 = 최소 힙 / 첫번째 원소를 기준으로 우선순위 설정됨
# 최대 힙 (값이 큰 데이터 먼저 삭제) -> (-) 붙여서 구현하면 됨 

# 첫 구현과 비교 -> get_smallest_node() 함수 필요 X 
# 최단거리가 가장 짧은 노드 선택 -> 우선순위 큐로 대체 가능 

'''
import heapq
import sys 

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

# 간선 정보 채우기
for _ in range(m):
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드 최단 경로 비용은 0 (거리가 먼저 들어가도록!)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단거리 짧은 노드 꺼내기 -> 우선순위 큐
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드 -> 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드 확인 
        for i in graph[now]:
            cost = dist + i[1] # 지금까지의 거리 더해서 계산하니까

            # 지금 노드 거쳐가는게 더 짧을 때 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])

'''

# E개의 원소를 우선순위 큐에 넣었다가, 모두 빼는 연산과 유사
# 항상 작은 값이 먼저 나온다 -> 데이터 삽입/삭제 logN 연산

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

# 2) 플로이드 워셜 알고리즘 
# 다익스트라 = 한 지점 -> 다른 특정 지점
# 플로이드 = 모든 지점 -> 다른 모든 지점 / O(N^3)

# 2차원 리스트에 최단 거리 정보 저장 -> 모든 노드에 대해 다른 모든 노드로의 최단거리 저장
# DP -> N개의 노드에 대해, 점화식에 맞게 N번 2차원 리스트 업데이트

# Dab = min(Dab, Dak + Dkb) // K 거치는 경로와 min 치면 됨 
# Dab = a에서 b로 가는 최단 거리 


INF = int(1e9)

n = int(input())
m = int(input())

# 2차원 그래프를 모두 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 비용 (대각선) = 0 초기화 
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 간선 정보 받아서 채워 넣기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c     # a -> b 비용은 c

# 플로이드 워셜 알고리즘 ***
for k in range(1, n + 1):           # 중간 노드가 될 K
    for a in range(1, n + 1):
        for b in range(1, n + 1):   # DP 점화식 (구현이 매우 간단)
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력하기 위한 코드 
for a in range(1, n + 1):
    for b in range(1, n + 1): 
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''
