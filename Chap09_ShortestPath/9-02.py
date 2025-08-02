# 전보
# chap9. 262 page

# 도시의 개수 N, 통로의 개수 M, 출발 도시 C
# X -> Y 통로, 시간이 Z 소모
# heapq 다익스트라로 구현해야 한다 (M size)

import heapq

N, M, C = map(int, input().split())

INF = int(1e9)
graph = [[] for i in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split()) 
    # a -> b, 비용 c
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드 최단 경로 비용은 0 (거리가 먼저 들어가도록!)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단거리 짧은 노드 꺼내기 -> 우선순위 큐
        dist, now = heapq.heappop(q)

        # 이미 처리한 노드 pass
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드 확인 
        for i in graph[now]:
            cost = dist + i[1] # 지금까지의 거리 더해서 계산하니까

            # 지금 노드 거쳐가는게 더 짧을 때 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# graph update
dijkstra(C) 

count = 0
total_time = 0

print(distance)

for i in distance:
    if i <= INF and i != 0:
        count += 1
        total_time = max(total_time, i)

print(count, total_time)