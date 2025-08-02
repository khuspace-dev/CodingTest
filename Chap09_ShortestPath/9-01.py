# 미래 도시
# chap9. 259 page

# 전체 회사 N개, 경로 M개 
# A는 1에서 출발 -> K에서 소개팅 -> X에서 방문 판매 (dp 점화식)
# 각 이동은 1 -> 최소 이동 시간 구하기 

N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신(대각선) -> 0으로 채우기
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

# input -> 연결된 관계에 1 넣어주기 
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 반대인 경우도 1 추가해줘야 함! 

X, K = map(int, input().split())

for k in range(1, N + 1):          
    for a in range(1, N + 1):
        for b in range(1, N + 1):   
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

if (graph[1][K] + graph[K][X] >= INF):
    print(-1)
else:
    print(graph[1][K] + graph[K][X])

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''