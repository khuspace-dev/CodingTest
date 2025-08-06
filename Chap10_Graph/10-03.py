# 커리큘럼 
# chap10. 303 page

# 강의 수 N개 / 동시에 여러 강의 수강 가능 
# 위상 정렬 -> 각 강의 별 시간과, 선수 강의들이 주어짐 (끝은 -1)
# 모든 강의에 대해 -> 수강 완료까지 걸리는 최소 시간 출력 (위상 정렬)

import sys
import copy
from collections import deque

input = sys.stdin.readline 

N = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)                # 진입 차수 초기화 (0으로)
time = [0] * (N + 1)                    # ith 강의의 수강 시간 저장 

# 연결 리스트 : 각 노드와 연결된 e 정보 저장
for i in range(1, N + 1): # 1부터 저장되도록 하려고 index 주의 
    input_line = list(map(int, input().split()))

    # init 강의 시간 => time 
    time[i] = input_line[0]

    for x in input_line[1:-1]:
        graph[x].append(i)              # x 먼저 듣고 -> i 들어야 함 
        indegree[i] += 1                # 선수강 숫자 ++ 

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        # 큐에서 나온 순서대로 위상 정렬 결과니깐
        # result.append(now)

        # now 노드랑 연결된 노드(i)와의 간선 끊기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1

            # 선수강 강의가 있다면? 
            # result[i] = max(result[i], result[선수강] + time[i])
            # result update 과정에서 time 오염 가능 -> 딥카피 

            # 진입 차수가 0인 강의부터 Enqueue
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, N + 1):
        print(result[i])

topology_sort()


'''
5 
10 -1
10 1 -1 
4 1 -1
4 3 1 -1
3 3 -1
'''