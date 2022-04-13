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
t_list = input()
opstack = Stack()
outstack = []

prec = {'*':2, '/':2, '+':1, '-':1, '(':0}

for token in t_list:
  if token == '(':
    opstack.push(token)
  elif token == ')':
    while opstack[-1] != '(':
      outstack.append(opstack.pop())
    opstack.pop()
  elif token in '+-/*':
    while True:
      if len(opstack) == 0:
        opstack.push(token)
        break
      elif prec[opstack[-1]]<prec[token]:
        opstack.push(token)
        break
      else:
        outstack.append(opstack.pop())
  else:
    outstack.push(token)
while len(opstack) != 0:
  outstack.append(opstack.pop())

print("".join(outstack))

# postfix -> infix
