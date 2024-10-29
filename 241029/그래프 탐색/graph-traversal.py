## dfs 기본 개념

# 인접 행렬
# def dfs(v):
#     for curr_v in range(1, ver_num + 1):
#         if graph[vertex][curr_v] and not visited[curr_v]:
#             print(curr_v)
#             visited[curr_v] = True
#             dfs(curr_v)

# 인접리스트: 연결된 정점이 graph[vertex] 리스트

# def dfs(v):
#     for curr_v in graph[v]:
#         if not visited[curr_v]:
#             print(curr_v)
#             visited[curr_v] = True
#             dfs(curr_v)

'''
from collections import defaultdict

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

# 입력 받기
n, m = map(int, input().split())
graph = defaultdict(list)

# 그래프 구성
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)  # 양방향 그래프이므로

# DFS 실행 및 결과 출력
reachable = dfs(graph, 1)
print(len(reachable) - 1)  # 1번 정점 제외
'''
'''
## 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

# index 1번부터 사용하고자 n+1 만큼 할당
graph = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

visited = [False for _ in range(n + 1)]
cnt = 0

def dfs(vertex):
    global cnt

    # 해당 정점에서 이어진 모든 정점 탐색
    for curr_v in range(1, n+1):
        # 아직 간선이 존재하고 방문한 적 없는 정점에 대해서만 탐색
        if graph[vertex][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            cnt += 1
            dfs(curr_v)

for i in range(m):
    v1, v2 = tuple(map(int, input().split()))

    # 각 정점에 대한 간선을 각각 저장(양방향그래프)
    graph[v1][v2] = 1
    graph[v2][v1] = 1
    
    ## 다른 코드에서는, 인접리스트 활용
    # graph[v1].append(v2)
    # graph[v2].append(v1)
    

visited[1] = True
dfs(1)

print(cnt)
'''
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

#index를 1번 부터 사용하기 위해 n+1만큼 할당합니다.
graph = [[] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]
vertex_cnt = 0

def dfs(v):
    global vertex_cnt
    ## 정점에서 이어진 모든 정점 탐색
    for cv in graph[v]:
        ## 간선은 존재, 방문 없는 정점만 탐색하고, 
        if not visited[cv]:
            visited[cv] = True
            vertex_cnt += 1
            dfs(cv)

for i in range(m):
    v1, v2 = tuple(map(int, input().split()))

    ## 양방향, 각 간선에 저장
    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)

print(vertex_cnt)