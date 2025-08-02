# 정확한 순위 
# chap9. 386 page

# 학생 N명, 성적 비교 M회
# A B -> A학생 성적 < B 성적 
# 성적 순위를 정확히 알 수 있는 학생 수 출력 

# 모든 경로와 직/간접 이어진 학생
# -> 성적을 정확하게 추론할 수 있음 -> 플로이드 

N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1 
    # graph[b][a] = 1
    # A < B 상관관계 의미

for k in range(1, N + 1):          
    for a in range(1, N + 1):
        for b in range(1, N + 1):  

            # first
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

            # second 
            # if graph[a][k] == 1 and graph[k][b] == 1:
            #     graph[a][b] = 1

# output 행렬 확인해보기 
# for a in range(1, N + 1):
#     for b in range(1, N + 1): 
#         if graph[a][b] == INF:
#             print("-", end=" ")
#         else:
#             print(graph[a][b], end=" ")
#     print()

# 정답
result = 0
for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
        # 둘 중 한번이라도 연결 되면 -> 가능하다고 보는 것 
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    
    # 모든 학생과 성적 비교 가능한 경우 -> 정확한 성적을 아는 학생!
    if count == N:
        result += 1
print(result)
