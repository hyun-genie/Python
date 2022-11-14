# 콜라츠 추측
# 모든 자연수 n에 대해 다음 작업을 반복 시, 항상 1로 만들 수 있음
# 입력된 수가 짝수라면 2로 나누고, 입력된 수가 홀수라면 3을 곱하고 1을 더함
# 결과로 나온 수가 1보다 크다면 2로 계속해서 나누는 작업을 반복

# 출력
# 정적분의 결과 목록을 return 하도록 solution을 완성
# 단, 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어질 수 있으며 이때의 정적분 결과는 -1로 정의

# 제한사항
# 정답에 실수형이 포함되는 문제입니다.
# 2 ≤ k ≤ 10,000
# 1 ≤ ranges의 길이 ≤ 10,000
# ranges의 원소는 [a, b] 형식이며 0 ≤ a < 200, -200 < b ≤ 0 입니다.
# 주어진 모든 입력에 대해 정적분의 결과는 2^27 을 넘지 않습니다.
# 입출력 예의 소수 부분 .0이 코드 실행 버튼 클릭 후 나타나는 결괏값, 기댓값 표시와 다를 수 있습니다.


def solution(k, ranges):
    answer = []

    num_list = [k]
    while k != 1:
        if k % 2 == 0:
            k = k // 2
        elif k % 2 != 0:
            k = k * 3 + 1
        num_list.append(k)

    num_sequence = []
    for i in range(len(num_list)):
        num_sequence.append((i, num_list[i]))

    for a, b in ranges:
        c = len(num_list) + b - 1
        if a > c:
            answer.append(-1)
        else:
            temp = 0
            for i in range(a, c):
                temp += (num_sequence[i][1] + num_sequence[i + 1][1]) / 2
            answer.append(float(temp))

    return answer
