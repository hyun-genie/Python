# 출력
# 가장 큰 양의 정수 a return
# 한 명이 가지고 있는 나눌 수 있는 최대값 return, 만족하는 조건이 없다면 0 return

# 최대 공약수 (GCD)
# 유클리드 알고리즘
# a와 b의 최대공약수는 b와 a를 b로 나눈 나머지의 최대공약수와 같다.
# 어떤 수와 0의 최대공약수는 자기 자신이다. 즉, gcd(n,0)=n이다.


def get_a_b(arr):
    g = arr[0]
    for i in range(1, len(arr)):
        g = gcd_u(g, arr[i])
    return g


def gcd_u(a, b):
    if b == 0:
        return a
    return gcd_u(b, a % b)


def solution(arrayA, arrayB):
    result = 0

    A, B = get_a_b(arrayA), get_a_b(arrayB)

    for i in arrayB:
        if i % A == 0:
            break
    else:
        result = max(A, result)

    for i in arrayA:
        if i % B == 0:
            break
    else:
        result = max(B, result)

    return result
