# 순위

# 입력
# n : 권투선수 (1명 이상 100명 이하)
# 경기 결과를 담은 2차원 배열 result (1개 이상 4,500개 이하) / results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미
# 어떤 선수 A가 B를 이겼으면 B가 이긴 선수들은 A가 이김
# 어떤 선수 A가 C한테 졌으면 C를 이긴 선수들은 A도 이김

# 출력
# 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return

# 조건
# 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다.
# 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다.
# 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.
# 모든 경기 결과에는 모순이 없습니다.

# IDEA : 플로이드 워셜 : 모든 정점사이의 최단 비용를 찾는 알고리즘
# 정점과 정점사이의 최단 비용을 찾는데, k 노드를 경유하였을 때 그 값이 현재 최솟 값보다 작으면 갱신 시키며 행렬을 만드는 알고리즘
# a가 b를 이겼다면 b는 항상 a 아래이고, b가 c를 이겼다면 c도 항상 b 아래
# 결국 c는 항상 a아래 이므로 a->b, b->c이면 a->c 인 것이므로 플로이드 워셜로 접근이 가능
# a와 b 관계에서 a가 c를 이기고 c가 b를 이기는 관계가 있으면 a가 b를 이긴것으로 체크하고 (b,a), (c,a), (b,c)는 모두 진것으로 체크
# 순위가 결정되려면 모든 선수와 다 겨뤄봐야함
# 체크된 값의 개수가 n-1이거나 체크되지 않은 값이 1

# i 번째 사람이 다른 사람과 n-1 번 싸워 이기던가, 이미 순위가 결정된 사람과 싸워 나온 승패를 이용하여 알 수 O ->  바로 갈 수도 있고, 한 다리 (혹은 여러 다리) 건너건너 알 수도 있는 것 ! 한 점에서 다른 점까지의 거리를 (한 다리 거쳐서) 찾을 수 있는 알고리즘

# 플로워드 워셜 > 인접 행렬로 표현
from collections import Counter


def solution(n, results):
    answer = 0
    matrix = [[0] * n for _ in range(n)]  # 연결되지 않은 곳 0으로

    for win, lose in results:
        matrix[win - 1][lose - 1] = 1  # 이김
        matrix[lose - 1][win - 1] = -1  # 짐

    #  Floyd-Warshell 알고리즘의 기본적인 논리는 j 점에서 k점을 갈 때 i 점을 거쳐 j -> i -> k로는 갈 수 있는가
    # 일반적인 경우, 이렇게 가는 것이 비용이 더 작은가? 에 대한 평가, if 문이 들어가지만, 우리는 연결만 되어 있으면 O
    # 플로이드 워셜을 탐색할 때, K 노드를 경유할 때, 현재 탐색하는 A(ROW) 노드가 현재 경유하는 K 노드 한테 이겼으면, [K][B] = 1 인 것들은 [A][B] = 1, [B][A] = -1 을 의미
    for k in range(n):  # 모든 노드를 중간점(경로)로 가정
        for row in range(n):  # 거리 행렬을 순회
            for col in range(n):  # 만약 row가 k에 이겼고, k가 col에 이겼다면
                # row는 col에게도 이김 (지는 것도 동일)
                if row != col and matrix[row][col] == 0 and matrix[col][
                        row] == 0:
                    if matrix[row][k] == 1 and matrix[k][col] == 1:
                        matrix[row][col] = 1
                        matrix[col][row] = -1
                    if matrix[row][k] == -1 and matrix[k][col] == -1:
                        matrix[col][row] = 1
                        matrix[row][col] = -1

    # 각 노드 점수판에 0이 하나(다른 노드들에 대해 승패가 모두 결정됨)인 경우만 셈
    for i in range(n):
        if Counter(matrix[i])[0] == 1:
            answer += 1
    return answer
