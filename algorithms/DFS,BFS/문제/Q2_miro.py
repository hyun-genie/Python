# 미로 탈출
# 백준 알고리즘 2178: 미로 탐색 (Python)
# 문제 한 줄 정의 : 미로 탈출
# 입력 : 첫 번째 줄에 두 정수 세로 길이 N과 가로 길이 M (4, <= N, M <= 200)
#       다음 N개의 줄에는 각각 M개의 정수 (0, 1)로 미로의 정보가 주어짐 -> 괴물이 없는 부분은 1, 괴물이 있는 부분은 0
#       각각의 수들은 공백 없이 붙어서 입력으로 제시
#       마지막 칸은 항상 1
# 출력 : 첫째 줄에 최소 이동 칸의 개수를 출력
# 조건 : 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산
#			  1은 이동할 수 있는 칸이고 0은 이동할 수 없는 칸
# 		  인접한 칸 즉 상, 하, 좌, 우 의 방향으로 이동하기 때문에 행, 열의 리스트를 각각 만들어서 정의
# IDEA : Graph, BFS(Dequeue)
# 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색한다.
# 상, 하, 좌, 우로 연결된 모든 노드로의 거리가 1로 동일하다.
# 따라서 (1,1)지점부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결할 수 있다.

from collections import deque

print('n, m 입력')
n, m = map(int, input().split())  # N, M 공백으로 구분하여 입력받기
print(n, m)

print('n, m에 따른 그래프 모양 입력')
# 2차원 리스트 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
print(graph)

# 이동할 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽일 경우
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


bfs(0, 0)  # 처음 시작이 0,0
print(graph[n - 1][m - 1])

# if 0 <= nx < n and 0 <= ny < m:
#     if graph[nx][ny] == 1:
#         graph[nx][ny] = graph[x][y] + 1
#         queue.append((nx, ny))
