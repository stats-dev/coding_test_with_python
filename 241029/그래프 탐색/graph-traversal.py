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