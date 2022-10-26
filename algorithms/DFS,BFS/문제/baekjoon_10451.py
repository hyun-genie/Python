import sys

sys.setrecursionlimit(2000)  # 최대 재귀를 늘려줘야 런타임 에러를 피할 수 있다

T = int(input())


def dfs(v):
    # 현재 노드 방문 처리
    visited[v] = 1
    next = nexts[v]

    if visited[next] == 0:  # 아직 방문하지 않은 곳인 경우 #  if not visited[i]: #방문하지 않았다면
        dfs(next)  # 재귀


for i in range(T):
    N = int(input())
    result = 0

    nexts = [0] + list(map(int, input().split()))
    visited = [0] * (N + 1)  # # 방문여부확인용

    for i in range(1, N + 1):
        if visited[i] == 0:  #  if not visited[i]: #방문하지 않았다면
            dfs(i)
            result += 1
    print(result)
