# 문제
# 두 개의 단어 begin, target과 단어의 집합 words
# 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정

# 입력
# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수

# 출력
# 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return

# 조건
# 각 단어는 알파벳 소문자
# 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
# words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
# begin과 target은 같지 않습니다.
# 변환할 수 없는 경우에는 0를 return
from collections import deque


def solution(begin, target, words):
    answer = 0
    word_len = len(words)
    # visited = [0 for _ in range(word_len)]
    visited = [0] * word_len  # 방문 노드 여부 확인 리스트

    q = deque()
    q.append([begin, 0])  # [단어, 깊이]

    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break

        for i in range(word_len):
            temp_cnt = 0

            # 아직 방문 X
            if not visited[i]:  # 만약 확인 안 한 단어라면
                # 그 단어가 words 속 단어와 다를 때 한 자씩 비교해서 더하기
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1

                # 단어 비교 시, 한 알파벳이 다른 경우
                if temp_cnt == 1:  # 만약 다른 글자 개수가 1개라면
                    q.append([words[i], cnt + 1])
                    visited[i] = 1

    return answer
