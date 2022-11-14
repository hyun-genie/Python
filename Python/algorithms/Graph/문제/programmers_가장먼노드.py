# 가장 먼 노드

# 입력
# 노드의 개수 : n (2 이상 20,000 이하)
# 간선에 대한 정보가 담긴 2차원 배열 : vertex (간선은 양방향, 1개 이상 50,000개 이하, vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미)

# 출력
# 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return

# IDEA : BFS
# 인접 리스트 이용 -> 노드가 각각 누구와 연결되어 있는지
# visited를 통해 방문을 확인함과 동시에 1부터 해당 노드까지의 거리 파악
from collections import deque


def solution(n, edge):

    # 인접 리스트 이용 -> 노드가 각각 누구와 연결되어 있는지
    adj = [[] for _ in range(n + 1)]

    # 양방향 그래프
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)

    # 몇 개의 간선을 통해 연결된 것인지 표현
    visited_dfs = [0] * (n + 1)  # 노드 1부터 각 노드까지의 거리
    # 이후, 노드들은 2부터 시작될 것
    visited_dfs[1] = 1

    # 1번 노드가 기준 -> queue에 1을 가장 먼저 삽입
    queue = deque()
    queue.append(1)  # queue = deque([1])

    # queue가 빌 때까지 반복
    while queue:
        # queue의 맨 앞 원소 popleft
        x = queue.popleft()
        # 해당 원소와 연결되어 있는 모든 노드 접근
        for i in adj[x]:
            # 해당 노드를 방문한 적이 없다면, 방문하여 현재 원소에 + 1
            if not visited_dfs[i]:
                visited_dfs[i] = visited_dfs[x] + 1
                queue.append(i)

    # 1번 노드로부터 가장 멀리 떨어진 노드 개수 count
    max_edge = max(visited_dfs)
    cnt = visited_dfs.count(max_edge)

    return cnt
