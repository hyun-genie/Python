# 문제
# 철수와 동생은 롤케이크를 공평하게 나눠먹으려 하는데, 그들은 롤케이크의 크기보다 롤케이크 위에 올려진 토핑들의 종류에 더 관심
# 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 롤케이크가 나누어진 것으로 생각

# 입력
# 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열 topping이 매개변수
# 1 ≤ topping의 길이 ≤ 1,000,000
# 1 ≤ topping의 원소 ≤ 10,000

# 출력
# 롤케이크를 공평하게 자르는 방법의 수를 return 하도록 solution 함수를 완성

from collections import Counter


def solution(topping):
    top_count = Counter(topping)
    check = set()
    answer = 0
    for i in topping:
        top_count[i] -= 1
        check.add(i)
        if top_count[i] == 0:  # 토핑의 개수가 0이면 pop
            top_count.pop(i)
        if len(top_count) == len(check):  # 토핑의 개수가 같다면 +1
            answer += 1

    return answer
