# 문제
# 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들기
# 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수 작성

# 입력 : 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수

# 제한조건
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.

answer = 0


def solution(numbers, target):
    DFS(0, numbers, target, 0)
    return answer


def DFS(idx, numbers, target, value):
    global answer
    n = len(numbers)

    if (idx == n) and (target == value):
        answer += 1
        return False
    if idx == n:
        return False
    else:
        DFS(idx + 1, numbers, target, value + numbers[idx])
        DFS(idx + 1, numbers, target, value - numbers[idx])
