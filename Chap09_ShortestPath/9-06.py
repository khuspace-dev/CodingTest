# 숨바꼭질
# chap9. 390 page

# N개의 헛간, M개의 통로 
# 1번에서 최단거리가 가장 먼 헛간 = 가장 안전
# 최단거리 = 지나야하는 통로의 최소 개수 
# 거리가 같은 헛간 -> 작은 번호 출력 

import heapq

N, M = map(int, input(). split())

INF = int(1e9)
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # 연결됨 의미 = 1
    graph[b].append((a, 1)) # 서로 연결 -> b->a 도 추가해야 함

def dijkstra(start):
    q = []

    # (거리, 노드) -> 거리에 대한 최소힙
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, temp_node = heapq.heappop(q)

        # 이미 방문한 노드라면 -> pass (이미 update 되었다는 의미)
        if distance[temp_node] < dist:
            continue

        # 인접 노드를 살펴봄 
        # graph[i]에는 인접한 노드와 cost가 저장됨
        for connected_node, cost in graph[temp_node]:
            temp_cost = dist + cost

            # 지금 노드 거쳐가는게 더 짧을 때 
            if temp_cost < distance[connected_node]:
                distance[connected_node] = temp_cost
                heapq.heappush(q, (temp_cost, connected_node))

# 시작 노드 기준 = 1
dijkstra(1)

print(graph)
print(distance)

# 1st - 숨어야 하는 헛간 번호 (가장 작은 번호) 
# 2nd - 해당 헛간까지의 거리 
# 3rd - 같은 거리를 갖는 헛간의 개수

safest_dist = max(distance[1:])
safest_house = distance.index(safest_dist)
duplicate_num = distance.count(safest_dist)

print(safest_house, safest_dist, duplicate_num)

'''
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
'''