# 문제
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수

# 입력
# array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수

# 조건
# i ~ j 번째까지 잘라서 리스트에 담기
# 정렬
# k번째 숫자 추출

# 출력
# 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return


def solution(array, commands):
    answer = []

    for i in commands:
        # 주어진 array에서 자를 부분 인덱싱
        arr = array[i[0] - 1:i[1]]

        # 정렬
        arr.sort()

        # k 번째 수 넣기
        answer.append(arr[i[2] - 1])

    return answer


'''
다른 한 줄 풀이 
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
'''
