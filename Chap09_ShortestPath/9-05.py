# 화성 탐사
# chap9. 388 page

import sys
import heapq

input = sys.stdin.readline

# 동 남 서 북 
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

INF = int(1e9)

def dijkstra(graph, distance):
    q = []
    # 비용(이거 기준 최소힙), x, y -> 좌표가 필요함
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0] 

    while q:
        # cost 작은 노드 pop
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            # 다른 인접 노드를 탐색하는 과정
            temp_x = x + dx[i]
            temp_y = y + dy[i]

            if (0 <= temp_x < N and 0 <= temp_y < N): # N-1 까지만 가능 
                cost = dist + graph[temp_x][temp_y]

                if cost < distance[temp_x][temp_y]:
                    distance[temp_x][temp_y] = cost 
                    heapq.heappush(q, (cost, temp_x, temp_y))

    return distance[N - 1][N - 1]


T = int(input()) # test case 

for _ in range(T):
    N = int(input())
    temp_graph = [list(map(int, input().split())) for _ in range(N)]
    temp_distance = [[INF] * N for _ in range(N)] # 2차원 결과를 저장하도록

    output = dijkstra(temp_graph, temp_distance)
    print()
    print(output)

'''
3 
3 
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
