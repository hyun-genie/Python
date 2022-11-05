# 전화번호 목록
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 조건
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

# 입력
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때

# 출력
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성


# 풀이 1
def solution(phone_book):
    answer = True
    hash_map = {}
    # 모든 전화번호 Hashing 하기 (Hash Map에 추가하기)
    for phone_number in phone_book:
        # Key는 phone_number / Value는 1로 설정
        # Value == 1의 의미는 숫자가 1개 존재
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number

            # String이라는 Key가 현재 hash_map에 존재하는지 확인
            if temp in hash_map and temp != phone_number:
                answer = False

    return answer


# 실패 풀이 2 : 시간 초과
def solution(phoneBook):
    # 1. 비교할 A선택
    for i in range(len(phoneBook)):
        # 2. 비교할 B선택
        for j in range(i + 1, len(phoneBook)):
            # 3. 서로가 서로의 접두어인지 확인한다.
            # String1.startswith(String2)
            # String1이 String2로 시작되는지 (String2가 String1의 접두어인지)를 찾아주는 기본 함수
            if phoneBook[i].startswith(phoneBook[j]):
                return False
            if phoneBook[j].startswith(phoneBook[i]):
                return False
    return True
