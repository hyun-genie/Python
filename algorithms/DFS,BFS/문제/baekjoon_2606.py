# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# 출력
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

# c = 정점 개수, computers = 간선 개수
c = int(input())
computers = int(input())

# 인접 영행렬
graph = [[0] * (c + 1) for i in range(c + 1)]

# 방문 기록 체크
visited_dfs = [0] * (c + 1)

# 입력받는 값에 대해 영형렬에 1삽입(인접리스트생성)
for i in range(computers):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def dfs(v):
    count = 0
    # 현재 노드 방문 처리
    visited_dfs[v] = 1
    # print(v, end=' ')

    # 재귀
    for i in range(1, c + 1):
        if (visited_dfs[i] == 0) and (graph[v][i] == 1):
            dfs(i)
            count += 1


dfs(1)
print(sum(visited_dfs) - 1)
'''
from collections import deque
# c = 정점 개수, computers = 간선 개수
c = int(input())
computers = int(input())

# 인접 영행렬
graph = [[0] * (c + 1) for i in range(c + 1)]

# 방문 기록 체크
visited_bfs = [0] * (c + 1)

# 입력받는 값에 대해 영형렬에 1삽입(인접리스트생성)
for i in range(computers):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def bfs(v):
    # 방문 해야 할 곳을 순서대로 넣을 큐
    queue = deque([v])
    visited_bfs[v] = 1

    # 큐 안에 데이터가 없을때까지
    while queue:
        v = queue.popleft()
        # print(v, end=' ')
        for i in range(1, c + 1):
            if (visited_bfs[i] == 0) and (graph[v][i] == 1):
                queue.append(i)
                visited_bfs[i] = 1


bfs(1)
print(sum(visited_bfs) - 1)
'''
