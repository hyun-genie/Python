# 1 : O, 0 : X
# (1,1)에서 출발
# (N,M)의 위치로 이동할 때 지나야 하는 최소의 칸 수 구하기
# 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동 가능
# 입력 : 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다.
#       다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
#       각각의 수들은 붙어서 입력으로 주어진다.
# 출력 : 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다.
#       항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]


print(bfs(0, 0))
