# 1부터 n까지 합을 구하는 알고리즘
print("1부터 n까지 합을 구하하기 위하여 n을 입력하시오.")
n = int(input())
def sum(n):
  s = 0
  for i in range(1,n+1):
    s+=i
  return s 
print(sum(n))

# 알고리즘에는 입력이 필요한데 입력 크기는 알고리즘 수행 성능에 영향을 미치는 경우가 존재한다. 
# 즉, 입력의 크기가 커진다면 당연히 알고리즘의 계산도도 복잡해진다. 

# 가우스의 합 공식 이용 알고리즘 n(n+1)/2
def sum2(n):
  return n*(n+1)//2
print(sum2(n))

# 가우스의 합 공식을 이용한 경우, 입력 크기 n이 아무리 커진다고 하더라도, 덧셈 1번, 곱셈 1번, 나눗셈 1번만 하면 된다. (총 3번)
# 1번 알고리즘의 경우, 덧셈 n번
