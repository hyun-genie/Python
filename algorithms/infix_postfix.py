class Stack:
  def __init__(self):
    self.items = []

  def push(self, val):
    self.items.append(val)

  def pop(self):
    try:
      return self.items.pop()
    except IndexError:
      print("Stack is empty")

  def top(self):
    try:
      return self.items[-1]
    except IndexError:
      print("Stack is empty")

  def isContain(self, val):
    return val in self.items

  def __len__(self):
    return len(self.items)

  def isEmpty(self):
    return len(self) == 0

  def clear(self):
    self.items=[]
    
# 스택의 응용 [infix -> postfix]
# infix는 일반적인 수식 방법(연산자가 피연산자들 사이에 위치), prefix는 연산자가 앞에 오는 것, postfix는 연산자가 뒤에 오도록 하는 것(연산자가 피연산자들 뒤에 위치)이다. 

# 괄호는 우선순위가 가장 높기 때문에 괄호 안의 연산자가 더 우선적이다. 
# 피연산자는 outstack에 그대로 넣는다.
# 연산자의 경우, 스택에 아무것도 없으면 push한다. 즉 첫번째 연산자는 스택에 push한다.
    
# 스택 안의 연산자가 지금 넣으려는 연산자보다 우선순위가 높으면 pop후에 우선순위가 낮은 연산자는 스택에 push한다.  
# 그 반대로 낮다면 스택에 순서대로 쌓이게 된다. 
# 동일한 연산자의 경우, 먼저 push한 것을 pop하고, 동일한 연산자를 push한다. 
# 스택의 맨 위에 있는 연산자와의 우선순위 비교 : top() 연산을 이용한다.

# 괄호의 처리
# 여는 괄호는 스택에 push한다. 
# 닫는 괄호를 만나게 되면 (가 나올때까지 계속 pop을 한다. 
# 연산자를 만났을 경우, 여는 괄호 너머까지 pop을 하지 않도록 여는 괄호의 우선순위를 가장 낮게 설정한다. 

print('[infix->postfix] 수식을 입력하시오. ')
t_list = input()
opstack = Stack()
outstack = ''

prec = {'*':3, '/':3, '+':2, '-':2, '(':1}

for token in t_list:
  if token == '(':
    opstack.push(token)
    
  elif token == ')':
    while opstack.top() != '(':
      outstack += opstack.pop()
    opstack.pop()
    
  else:
    if token in prec:
      if opstack.isEmpty():
        opstack.push(token)
        
      elif prec[opstack.top()] >= prec[token]:
        while not (opstack.isEmpty()) and (prec[opstack.top()] >= prec[token]):
          outstack += opstack.pop()
        opstack.push(token)   
          
      else:
        opstack.push(token)     
        
    else: 
      outstack += token
    
while not opstack.isEmpty():
  outstack += opstack.pop()
  
print("".join(outstack))

# A*B+C -> AB*C+
# A+B*C -> ABC*+
# A+B+C -> AB+C+ (동일한 연산자의 경우)
# (A+B)*(C+D) -> AB+CD+*
# (A+(B-C))*D -> ABC-+D*
