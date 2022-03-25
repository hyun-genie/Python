# 6002
# 다음을 실행시키면 "문장1”, "문장2"가 공백( )을 사이에 두고 출력된다.
print("문장1 문장2")
print("문장1", "문장2")

# 6004 - 6005
# 작은 따옴표(‘)가 들어있는 출력문을 출력하기 위해서는 큰 따옴표(“)로 출력하면 된다.큰 따옴표가 들어있는 출력문을 출력하기 위해서는 작은 따옴표로 출력하면 된다.
print(" 'Hello' ")
print(' "Hello" ')

# 6006
# 출력 형식에 필요한 따옴표와 출력할 문자인 따옴표를 구분하기 위하여 \를 이용하면 된다. 
# [출력예시 : "!@#$%^&*()'] 
print('"!@#$%^&()\'')

# 6007
# \도 안전하게 출력하기 위해서는 \\를 사용하는 것이 좋다. 
# [출력예시] : "C:\Download\'hello'.py"
print('"C:\\Download\\\'hello\'.py"')

# 6013
# 줄을 바꿔 문자 2개를 입력받고, 순서를 바꿔 한 줄씩 출력하기 위한 방법은 다음과 같은 방법도 존재한다.  
a = input()
b = input()
print("{b}\n{a}".format(b=b, a=a))

# 6014
# for 반복문은 반복할 수 있는 것 중에 문자열, 리스트, 딕셔너리, 범위가 있다. 
a = float(input())
for i in range(3): # 3번 출력 
	print(a)

# 6015
# input().split()를 사용하면, 공백을 기준으로 입력된 값들을 나누어(split) 자른다.
a, b = input().split()
print('{}\n{}'.format(int(a), int(b)))

# 6018
# input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자르게 된다. 
# 또한, print(a, b, sep=':')를 사용하면 콜론 기호를 사이에 두고 값을 출력하게 된다.  
a, b = input().split(':')
print(a, b, sep=':')

# 6019
date = input().split('.')
date.reverse() # date 값 순서 변환
print('-'.join(date)) # -과 함께 date값 표시

# 6020
# 아무것도 없는 empty 문자는 작은 따옴표 2개를 붙여서 표현한다. 
# 위 식은 -를 제외하여 숫자를 모두 붙여 출력하게 된다. 
print(''.join(input().split('-')))

# 6021
# for 반복문은 문자열도 반복할 수 있다. 
s = input()
for i in s:
    print(i)

# 6022
# 문자는 +로 연결한다. 
# date[a:b]라고 하면, date라는 단어에서 a번째 문자부터 b-1번째 문자까지 잘라낸 부분을 의미한다.
date = input()
print(date[:2] + ' ' + date[2:4] + ' ' + date[4:])

