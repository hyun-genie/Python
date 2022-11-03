# 문제 : 조이스틱으로 알파벳 이름을 완성


# 조건
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.
def solution(name):

    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    # 상, 하 방향 -> A부터 오름차순, Z부터 내림차순
    # A인 경우, 0, Z인 경우, 1
    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 좌, 우 방향
        # A가 나오기 전까지 왼쪽에서 오른쪽으로 이동
        # A를 마주치면 되돌아가기
        # 문자열 끝으로 가서, A가 나오기 전까지 이동
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min(
            [min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer
