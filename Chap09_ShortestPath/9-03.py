# 플로이드
# chap9. 385 page
# https://www.acmicpc.net/problem/11404

# 도시의 개수 n, 버스의 개수 m 
# 시작 도시 a -> 도착 도시 b, 비용 c // 노선은 하나가 아닐 수 있음 
# 모든 도시 쌍에 대해, 최소 비용 출력 (행렬 형태로 출력)

INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기자신 초기화
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

# 버스 정보 채우기 
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) # 중복 경로 가능해서, min 추가함    
    # a -> b 비용 c

# 플로이드 
for k in range(1, N + 1):          
    for a in range(1, N + 1):
        for b in range(1, N + 1):  
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# output 
for a in range(1, N + 1):
    for b in range(1, N + 1): 
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

# 채점 오래 걸림
'''