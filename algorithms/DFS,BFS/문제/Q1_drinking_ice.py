# 문제 한 줄 정의 : 음료수 얼려 먹기
# 입력 : 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M (1, <= N, M <= 1000)
#       두 번째 줄부터 N+1 번째 줄ㄹ까지 얼음 틀의 형태가 주어진다.
#       이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
# 출력 : 한 번에 만들 수 있는 아이스크림의 개수 출력
# 조건 : 상, 하, 좌, 우를 살펴보고 방문하며 연결된 부분 방문
# IDEA : Graph, DFS

print('n, m 입력')
n, m = map(int, input().split())  # N, M 공백으로 구분하여 입력받기
print('행:', n, ', 열:', m)

print('n, m에 따른 그래프 모양 입력')
# 2차원 리스트 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# print(graph)


# DFS로 특정 노드 방문 후, 연결된 모든 노드 방문
def dfs(x, y):
    # 주어진 범위 벗어나는 경우 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 방문 처리
        graph[x][y] = 1

        # 상, 하, 좌, 우 위치 재귀적 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False


# 모든 노드(위치)에 대하여 값 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현 위치 DFS 수행
        if dfs(i, j) == 1:
            result += 1

print(result)
