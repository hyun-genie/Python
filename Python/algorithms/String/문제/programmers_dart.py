# 다트 케임
# 문제 : 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성

# 3번 기회 -> 점수 : 0~10점
# 보너스 : 점수와 함께 S, D, T -> ^1, ^2, ^3으로 계산
# 옵션 : *, # 상 존재
# *는 해당 점수와 바로 전에 얻은 점수 각 2배 (첫 번째 기회에서도 O, 이 경우 첫 번째 점수만 2배) (다른 *과 효과 중첩 가능, 이 경우 점수 4배)
# #는 해당 점수는 마이너스
# #과 *은 효과 중첩 가능 -> #의 점수는 -2배
# *, #은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도! 옵선은 *이나 # 중 하나이며, 없을 수도 있다.

# 입력 : 점수|보너스|[옵션] -> 예) 1S2D*3T

def solution(dartResult):
    string_list = []
    # 점수 -> 10인 2자리 예외 처리 -> 10 : A
    dartResult = dartResult.replace('10', 'A')
    bonus = {'S': 1, 'D': 2, 'T': 3}

    for i in dartResult:
        # i가 숫자라면 그대로 스택에 넣는다. (A는 10으로 바꿔서 스택에 넣는다)
        #  이때 정수로 변환해서 스택에 넣어준다.
        if i.isdigit() or i == 'A':
            string_list.append(10 if i == 'A' else int(i))
        elif i in ('S', 'D', 'T'):
            # i가 S, D, T중 하나라면
            # 스택에서 마지막 들어간 아이템을 하나 꺼내서 bonus[i] 만큼 제곱해서 다시 스택에 넣는다.
            num = string_list.pop()
            string_list.append(num**bonus[i])
        elif i == '#':
            # i가 #이라면 스택의 마지막 요소에 -1를 곱한다.
            string_list[-1] *= -1
        elif i == '*':
            # 우선 스택에서 마지막 요소를 하나 꺼낸다.
            # 만약 요소를 꺼낸 뒤 스택에 요소가 더 남아있다면 그 마지막 요소에 2를 곱하고,
            # 꺼냈던 요소에도 2를 곱해서 다시 넣어준다.
            num = string_list.pop()
            # *과 효과 중첩 가능
            if len(string_list):
                string_list[-1] *= 2
            string_list.append(2 * num)

    return sum(string_list)
