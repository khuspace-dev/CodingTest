# 특정 거리의 도시 찾기
# chap5. 339 page 

# N = 도시의 개수
# M = 도로의 개수
# K = 거리 정보
# X = 출발 도시 번호

N, M, K, X = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(M)]
graph = [[] for _ in range(N + 1)] # 편의상 +1 하는거 

for start_node, end_node in [list(map(int, input().split())) for _ in range(M)]:
    graph[start_node].append(end_node)

cities = []
visited = [False] * (N + 1)

def dfs(node, depth):
    visited[node] = True # 방문 처리 

    if depth == K:
        cities.append(node)
        return 
    else:
        # depth += 1 # next 깊이 update 

        for next_node in graph[node]:
            if visited[next_node] == False:
                dfs(next_node, depth + 1)       # 다른 경로에서도 이 노드에 접근 가능하도록, 
                visited[next_node] = False      # 현재 경로 탐색 이후, False로 되돌리기

dfs(X, 0) # 출발 도시 X, 초기 depth = 0 
cities.sort()

if len(cities) == 0:
    print(-1)
else:
    for city in cities:
        print(city)