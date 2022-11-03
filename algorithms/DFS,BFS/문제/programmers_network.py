# 문제 : 연결되어 있는 네트워크의 수 출력
# 입력 : 컴퓨터의 개수 n (1 <= n <= 200) > 정점 개수
#       컴퓨터 연결된 간선 computers list
# 연결 O은 1, 연결 X은 0
# computer[i][i]는 항상 1


def solution(n, computers):
    answer = 0
    visited = [0] * (n + 1)  # [0 for i in range(n)]
    for com in range(n):
        if visited[com] == 0:
            DFS(n, computers, com, visited)
            answer += 1  #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer


def DFS(n, computers, com, visited):
    visited[com] = 1  # 현재 노드 방문 처리
    for connect in range(n):
        if (visited[connect] == 0) and (computers[com][connect] == 1): # connect != com #연결된 컴퓨터
            # if visited[connect] == 0:
            DFS(n, computers, connect, visited)


'''
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for com in range(n):
        if visited[com] == 0:
            BFS(n, computers, com, visited)
            answer += 1
    return answer

def BFS(n, computers, com, visited):
    visited[com] = 1 # 현재 노드 방문 처리
    queue = []
    queue.append(com)
    while queue: # 큐가 빌 때까지
        com = queue.pop(0)
        visited[com] = 1
        for connect in range(n):
            if (visited[connect] == 0) and (computers[com][connect] == 1):
                queue.append(connect)
'''
