# [6080 - 6098]

# 6080
# 주사위 2개 던지기 
# 1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위를 2개 던졌을 때, 나올 수 있는 모든 경우의 수를 출력해보자.
# 예시 
# for i in range(1,n+1):
#  for j in range(1, m+1):
#    print(i,j)
# 위 코드는 바깥쪽의 i 값이 1부터 n까지 순서대로 바뀌는 각각의 동안에 안쪽의 j값이 다시 1부터 m까지 변하며 출력되는 코드이다. 반복 실행구조 안에 다른 반복 실행구조를 넣어 처리할 수 있으며, 원하는 형태로 실행 구조를 결합하거나 중첩시킬 수 있다. 

# i = 1,2,...,n
# j = 1,2,...,m
# (1,1) (2,1) ... (n,1)
# (1,2) (2,2) ... (n,2)
# (1,m) (2,m) ... (n,m)

# 6081 
# 16진수 구구단 출력하기 
# 16진수(0,1,2,3,4,5,6,7,8,9,A.B.C.D.E.F0) 중에서 A부터 F까지 하나가 입력된다고 할 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력한다. 
# 참고로 print(‘%X’%n) #n에 저장되어 있는 값을 16진수 형태로 출력한다. 
# 작은 따옴표 2개를 사용해서 print(…, sep=’’)으로 출력하면, 공백없이 모두 붙여 출력된다. 작은 따옴표 2개 ‘’ 또는 큰 따옴표 2개 “”는 아무 문자도 없는 빈문자열을 의미한다. 
n = int(input(), 16) 
for i in range(1, 16): 
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

# 6082
# 3,6,9 게임의 왕이 되자
# 여러 사람이 순서를 정한 후, 순서대로 수를 부르는 게임이다. 3,6,9가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 박수(X)를 쳐야 한다. 33과 같이 3,6,9가 두 번 들어간 수일 때는 짝짝과 같이 박수를 두 번 치는 형태도 존재한다. 
n = int(input())

for i in range(1,n+1):
  if i%10==3 or i%10==6 or i%10==9:
    print("X", end=' ')    #출력 후 공백문자(빈칸, ' ')로 끝냄
  else:
    print(i, end=' ')

# 6083
# 빛 섞어 색 만들기
# 빨강, 초록, 파랑 빛을 섞어 여러 가지 다른 색의 빛을 만들어 내려고 한다. r,g,b 각 빛의 가짓수가 주어질 때, 주어진 rgb 빛들을 섞어 만들 수 있는 모든 경우의 조합과 만들 수 있는 색의 가짓수를 계산해보자. 
r, g, b = map(int, input().split())
count = 0 

for i in range(r): 
  for j in range(g): 
    for k in range(b): 
      print('%d %d %d' %(i, j, k)) 
      
      count = count + 1 

print(count)

# 6084
# 소리 파일 저장용량 계산하기 
h, b, c, s = map(int, input().split()) 
print(round(h*b*c*s/8/1024/1024, 1), "MB")
# 6085
# 그림 파일 저장용량 계산하기 
w, h, b = map(int, input().split()) 
res = (w*h*b)/8/1024/1024
print('%.2f'%res, "MB")

# 6086
# 거기까지! 이제 그만~ 
# 조건문이나 반복문의 코드블록 안에서 break가 실행되면, 반복실행을 중단(break)하고, 가장 가까운 반복 블록의 밖으로 빠져나간다. 
n = int(input())
c = 0
s = 0
while True :
  s += c
  c += 1
  if s>=n :
    break
print(s)

a = int(input()) 
total = 0 
i = 1 
while (total < a): 
  total += i 
  i += 1 
print(total)

# 6087
# 3의 배수는 통과 
# 조건문이나 반복문의 코드블록 안에서 continue가 실행되면, 반복 블록 안에 있는 나머지 부분을 실행하지 않고, 다음 반복 단계로 넘어간다. 즉, 반복 블록의 나머지 부분은 실행되지 않고, 다음 단계의 반복을 계속(continue)하는 것이다. 
n = int(input())

for i in range(1, n+1) :
  if i%3==0:
    continue            #다음 반복 단계로 넘어간다.
print(i, end=' ')

# 6088
# 수 나열하기 1 (등차수열)
# 시작 값(a), 등차의 값(d), 몇 번째 수인지 의미하는 정수(n)
a, d, n = map(int, input().split()) 
print(a+d*(n-1))
# 6089
# 수 나열하기 2 (등비수열)
a, r, n = map(int, input().split()) 
print(a*r**(n-1))

# 6090
# 수 나열하기 3 
# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)
# n번째 수를 출력하는 프로그램을 만들어보자.
a, m, d, n = map(int, input().split()) 
num = 0 

for i in range(1,n):
   a = (m*a)+d
print(a)

# 6091
# 함께 문제 푸는 날 
a, b, c = map(int, input().split()) 
i = 0
 
while True:
    i += 1 
    if i%a == 0 and i%b == 0 and i%c == 0: 
        print(i) 
        break

# day는 날 수, a/b/c는 방문 주기 
a, b, c = map(int, input().split())

d = 1
while d%a != 0 or d%b != 0 or d%c != 0 :
  d += 1
print(d)

# 6092
# 이상한 출석 번호 부르기 1
# 각 1~23번까지 불린 횟수를 각각 출력하기 
# 리스트는 여러 개의 값을 하나로 묶어 목록으로 기록했다가 다시 사용할 필요가 있을 때, 리스트를 만들어 사용할 수 있다. 
# 리스트는 변수들을 모아 놓은 변수라고 생각할 수도 있고, 참조번호를 이용해 간단하고 편리하게 사용할 수 있다. 
n = int(input()) 
a = input().split() 

for i in range(n): 
  a[i] = int(a[i]) 

d = [] # d라는 이름의 빈 리스트 [] 변수를 만듦, 어떤 데이터 목록(list)을 순서대로 저장하기 위해 아무것도 없는 리스트 변수를 만드는 것 
for i in range(24): # [0,0,0,0,,,]과 같이 24개의 정수 값 0을 추가해 넣음 
  d.append(0) # 각 값은 d[0], d[1], d[2] ,,, 으로 값을 읽고 저장할 수 있음, d리스트의 마지막에 원하는 값을 추가해 넣음  
  
for i in range(n): # 번호를 부를 때마다  그 번호에 대한 카운트 1씩 증가 
  d[a[i]] += 1 
    
for i in range(1, 24): # 카운트한 값을 공백을 두고 출력 
  print(d[i], end=' ')

# 6093
# 이상한 출석 번호 부르기 2
# 출석 번호 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력하기 
n = int(input()) 
a = input().split() 

for i in range(n): 
  a[i] = int(a[i]) 

d = [] 
for i in range(24): 
  d.append(0) 

for i in range(n): 
  d[a[i]] += 1 

for i in range(n-1, -1, -1) : # range(시작, 끝, 증감) : 시작수는 포함, 끝수는 포함하지 않음. n-1, n-2, …, 3, 2, 1, 0
  print(a[i], end=' ')

# 6094
# 이상한 출석 번호 부르기 3 
# 출석 번호 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력하기 
# 리스트에 출석 번호를 기록해 뒀다가, 그 중에서 가장 작은 값을 찾아내면 된다. 
n = int(input()) 
a = input().split() 

for i in range(n): 
  a[i] = int(a[i]) 
  min = a[0] 
  
for i in range(0, n): 
  if a[i] < min: 
    min = a[i] 
print(min)

num = int(input()) 
numlist = map(int, input().split()) 
a = min(numlist) 
print(a)

# 6095
# 바둑판에 흰 돌 놓기 
# 바툭판 (19*19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력하는 프로그램 작성하기 
d = [] # 대괄호 [ ] 를 이용해 아무것도 없는 빈 리스트 만들기
for i in range(20):
  d.append([]) # 리스트 안에 다른 리스트 추가해 넣기
  for j in range(20): 
    d[i].append(0) # 리스트 안에 들어있는 리스트 안에 0 추가해 넣기

n = int(input())
for i in range(n):
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20):
  for j in range(1, 20): 
    print(d[i][j], end=' ') # 공백을 두고 한 줄로 출력
print() # 줄 바꿈
# 리스트가 들어있는 리스트를. 만든다면 가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다. 리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있고, 더 확장한 n차원 리스트도 만들 수 있다. 

# d = [[0 for j in range(20)] for i in range(20)]
# 위와 같이 20개의 0이 들어간 [0,0,0,…,0] 리스트를 한 번에 만들 수 있다. 이러한 리스트 생성 방식을 List Comprehensions라고 한다. 

# 6096
# 바둑알 십자 뒤집기 
# 십자 뒤집기는 그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다. 어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다. 
# 바둑판(19*19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때, n개의 좌표를 입력받아 십자 뒤집기한 결과를 출력하는 프로그램을 작성하기 
d = [] 
for i in range(20): 
  d.append([])
  for j in range(20): 
    d[i].append(0) 
for i in range(19): 
  a = input().split() 
  for j in range(19): 
    d[i+1][j+1] = int(a[j]) 
    
n = int(input()) 
for i in range(n): 
  x, y = input().split() 
  x = int(x) 
  y = int(y) 
  for j in range(1, 20):
    if d[j][y] == 0: 
      d[j][y] = 1 
    else: 
      d[j][y] = 0 
      
    if d[x][j] == 0: 
      d[x][j] = 1 
    else: 
      d[x][j] = 0 
      
for i in range(1, 20): 
  for j in range(1, 20): 
    print(d[i][j], end=' ') 
  print()

# 6097
# 설탕과자 뽑기 
# 막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임 
# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,
# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.
h, w = map(int, input().split())

m = [] # 빈 리스트 만들기 
for i in range(h+1): 
  m.append([]) # 리스트 안에 다른 리스트 추가 
  for j in range(w+1): 
    m[i].append(0) # 리스트 안에 들어있는 리스트 안에 0 추가해 넣기 
  
n = int(input()) 
for i in range(n): 
  l, d, x, y = map(int, input().split())
  if d == 0: 
    for j in range(l): 
      m[x][y+j] = 1 
  else: # d == 1
    for j in range(l): 
      m[x+j][y] = 1

for i in range(1, h+1): 
  for j in range(1, w+1): 
    print(m[i][j], end=' ') 
  print()

# 6098
# 성실한 개미 
# 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동한다. 개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다. 오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다. 개미는 움직일 수 없을 때까지 오른쪽 또는 아래쪽으로만 움직였다. 미로 상자 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고, 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상하기
# 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는 더이상 이동하지 않고 그 곳에 머무른다고 가정한다. 
# 개미집은 반드시 (2,2)에 존재하기 때문에 개미는 (2,2)에서 출발한다. 
m = []

for i in range(12):
  m.append([])
  for j in range(12):
    m[i].append(0)

for i in range(10):
  a = input().split()
  for j in range(10):
    m[i+1][j+1] = int(a[j])

x = 2
y = 2

while True:
  if m[x][y] == 0:
    m[x][y] = 9
  elif m[x][y] == 2:
    m[x][y] = 9
    break

  if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9):
    break

  if m[x][y+1] != 1:
    y += 1
  elif m[x+1][y] != 1:
    x += 1

for i in range(1, 11):
  for j in range(1, 11):
    print(m[i][j], end=' ')
  print()

m = []

for i in range(10): 
    m.append(list(map(int, input().split())))

x = 1
y = 1

while True:
  if m[x][y] == 0:
    m[x][y] = 9
  elif m[x][y] == 2:
    m[x][y] = 9
    break

  if (m[x][y+1]==1 and m[x+1][y]==1):
    break

  if m[x][y+1] != 1:
    y += 1
  elif m[x+1][y] != 1:
    x += 1

for i in range(10):
  for j in range(10):
    print(m[i][j], end=' ')
  print()

# list comprehension : 리스트 컴프리헨션 
# 리스트의 값을 할당할 때, 편리하게 리스트를 정의하는 방법이다. 
# 1) 리스트의 값을 각각 타이핑해 정의하는 방법
# 2) 빈 리스트를 만들고, for 반복문을 이용하여 리스트의 append()의 함수를 이용해 정의하는 방법 
# 3) [할당할 값 for 순차적으로 받을 변수 in 이터레이터]
# 예 : list = [i for i in range(1, 10+1)]
# 4) 조건 추가 : [할당할 값 for 순차적으로 받을 변수 in 이터리에터 if 조건]
# 조건에 참인 경우 값만 할당된다.
# 5) 중첩된 리스트 컴프리헨션
list = []
for i in range(5):
    for j in range(5):
      list.append(i*j)

# 다음과 같이 쓸 수 있다.
list = [i*j for i in range(5) for j in range(5)]

# 또한, 중첩 for문 조건문 사용 예
list = [i*j for i in range(5) for j in range(5) if i*j %2 != 0]
