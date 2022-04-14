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

# infix는 일반적인 수식 방법, prefix는 연산자가 앞에 오는 것, postfix는 연산자가 뒤에 오도록 하는 것이다. 
# infix -> postfix
# 괄호는 우선순위가 가장 높기 때문에 괄호 안의 연산자가 더 우선적이다. 
# 피연산자는 스택에 그대로 집어 넣는다.
# 연산자의 경우, 스택에 아무것도 없으면 push한다.
    
# 스택 안의 연산자가 지금 넣으려는 연산자보다 우선순위가 높으면 그냥 push한다. 
# 그 반대로 낮다면 지금 넣으려는 연산자보다 우선순위가 낮은 것이 나올 때까지 pop하고 결과 리스트에 넣는다. 
# 괄호의 경우 (가 나올때까지 계속 pop을 하고, 결과 리스트에 넣는 예외처리를 해준다. 
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
        
      elif prec[opstack.top()] <= prec[token]:
        while (opstack.isEmpty()) and (prec[opstack.top()] >= prec[token]):
          outstack += opstack.pop()
        opstack.push(token)   
          
      else:
        opstack.push(token)     
        
    else: 
      outstack += token
    
while not opstack.isEmpty():
  outstack += opstack.pop()
  
print("".join(outstack))

# postfix -> infix
