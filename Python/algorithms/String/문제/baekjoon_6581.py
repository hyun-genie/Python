# 문제
# <br>, <hr> 태그와 그 외 평문으로만 주어지는 HTML 문서
# 그 결과를 보여주는 코드를 작성

# 조건
# 한 줄에는 80자보다 많은 글자가 출력되어서는 안 된다.
# 단어는 항상 80글자 이하이며, '<'나 '>'를 포함하지 않는다. 입력에 등장하는 태그는 <br>과 <hr> 외에는 없다.
# "abc,123"은 하나의 단어이지만, "abc, 123"은 "abc,", "123" 두 단어

# 입력
# 원래의 HTML 문서가 입력으로 주어진다. 이 텍스트는 단어와 HTML 태그들로 이루어져 있으며, 태그는 한 개 이상의 공백문자나 탭, 개행 문자 등으로 구분
# 단어는 연속된 알파벳, 숫자, 또는 문장 부호

# 출력
# 이번에 출력할 단어를 출력하고 나서도 현재 줄이 80글자를 넘지 않으면 현재 줄에 출력해도 좋다. 단, 80글자를 넘어가게 된다면 새로운 줄에 출력해야 한다.
# <br> 태그를 읽게 되면, 새 줄을 시작한다.
# <hr> 태그를 읽게 되면, 이미 줄의 첫 부분이 아니라면 새 줄을 시작한 뒤, '-'를 한 줄에 80글자를 입력한다. 그 후 다시 새 줄을 시작한다.
# 마지막 줄은 개행 문자로 끝난다.
# 여러 개의 연속된 개행 문자, 공백 문자, 탭 문자는 하나의 공백문자로 출력한다.

# 스택 사용 -> append, pop
# input 개수를 모를 때 입력 처리 방법
# while True문으로 입력을 계속 받다가 EOF를 만나 에러가 발생할 때 except문으로 캐치해 break로 입력을 중단

import sys

full_sentence = ""
for sentence in sys.stdin:  # ctrl+D 입력까지 모든 줄을 입력 받는다
    full_sentence += sentence

result_sentence = full_sentence.split()  # 다중 공백 제거 및 단어 별 리스트화

temp_list = []
temp_line_text = ""

for word in result_sentence:  # 단어별 탐색
    if word == '<br>':  # <br> 태그면 지금까지 출력해야할 문장 출력 후 '줄바꿈'
        temp_line_text = ' '.join(temp_list)
        temp_list = []
        print(temp_line_text)
    elif word == '<hr>':  # 구분선 출력
        if len(temp_list
               ) != 0:  # 첫지점에서 구분선 출력이 아니라면, 지금까지 출력해야할 문장 출력 후 구분선 출력
            temp_line_text = ' '.join(temp_list)
            temp_list = []
            print(temp_line_text)
        print('-' * 80)
    else:
        temp_list.append(word)  # 단어들이면 계속 합쳐준다
        temp_line_text = ' '.join(temp_list)
        if len(temp_line_text) > 80:  # 합치다가 80줄이 넘으면
            temp_list.pop(-1)  # 넘는 단어 빼고
            temp_line_text = ' '.join(temp_list)  # 다시 합쳐서 출력
            print(temp_line_text)
            temp_list = []
            temp_list.append(word)  # 다음 줄은 넘는 단어부터 시작

temp_line_text = ' '.join(temp_list)  # 마지막 줄 출력
print(temp_line_text)
