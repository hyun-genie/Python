print("두 수를 입력하시오")
a, b = map(int, input().split())

# 최대공약수(GCD)
def gcd(a,b):
  while a != 0 and b != 0:
    if a > b:
      a -= b
    else:
      b -= a
  return a + b
print(gcd(a,b))

def gcd2(a,b):
  i = min(a,b)
  while True:
    if a%i == 0 and b%i == 0:
      return i
    i -= 1
print(gcd2(a,b))

# 유클리드 알고리즘 
# a와 b의 최대공약수는 b와 a를 b로 나눈 나머지의 최대공약수와 같다. 
# 어떤 수와 0의 최대공약수는 자기 자신이다. 즉, gcd(n,0)=n이다. 
def gcd_u(a,b):
    if b == 0:
      return a 
    return gcd_u(b, a%b)
print(gcd_u(a,b))
      
# 최소공배수(LCM) 
# 유클리드 이용 : 최소공배수는 a,b의 곱을 a,b의 최대공약수로 나누면 된다. 
def lcm_u(a,b):
  return (a*b)//gcd_u(a,b)
print(lcm_u(a,b))