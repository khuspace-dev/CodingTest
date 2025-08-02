# 화성 탐사
# chap9. 388 page

# 다익스트라 최소비용 -> heapq 구현

import heapq

T = int(input())

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]

INF = int(1e9)
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
