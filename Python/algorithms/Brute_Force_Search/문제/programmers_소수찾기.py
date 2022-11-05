# 문제
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 입력
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers

# 출력
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return

# 조건
# numbers는 길이 1 이상 7 이하인 문자열
# numbers는 0~9까지 숫자

# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미

# IDEA : 조합, 소수 찾기, str -> int

from itertools import permutations
import math


def solution(numbers):
    answer = []
    nums = [n for n in numbers]  # numbers 잘라서 list에 넣기

    per = []
    for i in range(1, len(numbers) + 1):
        # i개씩 순열조합
        # append X (str 고려)
        per += list(permutations(nums, i))
    # 각 순열조합을 하나의 int형 숫자로 변환
    new_nums = [int(''.join(p)) for p in per]

    for n in new_nums:
        check = True
        # 2보다 작은 1,0의 경우 소수 아님
        if n < 2:
            continue
        # n의 제곱근 보다 작은 숫자까지만 나눗셈
        for i in range(2, int(math.sqrt(n)) + 1):
            # 하나라도 나눠떨어진다면 소수 X
            if n % i == 0:
                check = False
                break

        if check:
            answer.append(n)

    # print(len(set(answer)))
    return len(set(answer))  # set을 통해 중복 제거 후 반환
