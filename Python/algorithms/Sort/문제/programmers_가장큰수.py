# 문제
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수

# 입력
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수

# 출력
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return

# 조건
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.

# int형 리스트 map 이용하여 string으로 치환 -> list로 변환
# num을 sort하여 key 조건에 맞게 정렬
# lambda x:x*3은 num 인자 각각의 문자열을 3번 반복 (num의 인수값이 1000이하이므로(원소가 1000이하이므로), 3자리 수로 맞춘 뒤 비교)

# 문자열 비교
# ASCII 값으로 치환되어 정렬
# 문자열 비교연산의 경우에 문자열 첫번째 인덱스를 아스키숫자로 바꿔서 비교하고, 같으면 그 다음 인덱스를 비교하기때문에 숫자비교와는 다름

# Sort()
# default : 오름차순
# reverse = True : 내림차순

# 문자열에서의 대소비교와 일반숫자의 대소비교가 다르기때문에 가능한 코드

# 마지막에 문자열을 -> 정수 -> 문자열로 반환
# '00'을 '0'으로 반환하기 위함


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))
