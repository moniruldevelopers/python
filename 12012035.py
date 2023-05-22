class Stack:  
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    return self.stack.pop()

  def display(self):
    
    for element in self.stack:
      print(element, end=" ")
    print()


if __name__ == "__main__":
  stack = Stack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  stack.display()
  element = stack.pop()
  print("The popped element is:", element)
  stack.display()
