# 문제
#  체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성

# 입력
# 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수

# 제한사항
# 전체 학생의 수는 2명 이상 30명 이하입니다.
# 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.


def solution(n, lost, reserve):
    answer = 0

    # 1. student 배열 생성
    student = [0] * (n + 2)

    # 2. reserve / lost 정보 반영
    for r in reserve:
        student[r] += 1
    for l in lost:
        student[l] -= 1

    # 3. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for i in range(1, n + 1):
        if student[i] > 0:
            if student[i - 1] < 0:
                student[i] -= 1
                student[i - 1] += 1
            elif student[i + 1] < 0:
                student[i] -= 1
                student[i + 1] += 1

    # 4. 체육복을 갖고 있는 학생 수를 계산한다.
    for i in range(1, n + 1):
        if student[i] > -1:
            answer += 1

    return answer
