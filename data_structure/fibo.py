# 1부터 n까지 합을 구하는 알고리즘
print("1부터 n까지 합을 구하하기 위하여 n을 입력하시오.")
n = int(input())

# 피보나치 수열 : 0과 1부터 시작해서 바로 앞의 두 수를 더한 값을 다음 값으로 추가하는 방식으로 만든 수열을 피보나치 수열이라고 한다. 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

# 재귀 호출을 이용하여 알고리즘을 구현하시오. 

def fibo(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else: 
    return fibo(n-1)+fibo(n-2)

print(fibo(n))