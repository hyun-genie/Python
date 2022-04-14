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

# postfix -> infix