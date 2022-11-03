# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 1) 첫 번째 줄에는 총 단지수를 출력하시오.
# 2) 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
from collections import deque

N = int(input())

# 2차원 리스트 맵 정보 입력받기
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))
# graph = [graph.append(list(map(int, input()))) for _ in range(N)]

# 이동할 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    graph[x][y] = 0  # ! 탐색중인 위치 0으로 바꿔 다시 방문하지 않도록 함 !
    cnt = 1

    # 큐가 빌 때까지
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 벽일 경우
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0  # ! 탐색중인 위치 0으로 바꿔 다시 방문하지 않도록 함 !
                queue.append((nx, ny))
                cnt += 1
    return cnt


count = [bfs(i, j) for i in range(N) for j in range(N) if graph[i][j] == 1]
count.sort()

print(len(count))  # 총 단지 수

for i in range(len(count)):
    print(count[i])  # 단지 내, 집의 수
'''
def dfs(x,y):
    if x<0 or x>=N or y<0 or y >=N:
        return False
    
    if graph[x][y] == 1:
        global count # 전역변수
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            dfs(nx,ny)
        return True
    return False
    

count = 0
result = 0

for i in range(N):
    for j in range(N): 
        if dfs(i,j) == True: # dfs(i,j)
            num.append(count)
            result += 1
            count = 0
        
num.sort()
print(result)
for i in range(len(num)):
	print(num[i])
'''
