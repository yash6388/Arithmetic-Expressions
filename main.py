# Stack implementation
class Stack:
  
  # constructor for the Stack class
  def __init__(self):
    # initialise an empty list
    self.stack = []
    # self.stack = list() works the same way as above code
  
  # push the number into the stack
  def push(self, data):
    if data not in self.stack:
      self.stack.append(data)
      return True
    else:
      return False
    [r]
  # remove the top element
  def pop(self):
    if len(self.stack) <= 0:
      return "Stack is empty!"
    else:
      return self.stack.pop()
    
  # returns the size of the element
  def size(self):
    return len(self.stack)
    
  # peek to see the top element
  def peek(self):
    return self.stack[-1]
    
  # to check if stck is empty
  def isEmpty(self):
    if len(self.stack) <= 0:
      return True
    else:
      return False
  
  # show the content of stack
  def show(self):
    return self.stack

# Simple method to apply operator to numbers
def applyOp(op, var2, var1):
  if op == '+':
    print('Adding numbers...')
    return int(var1) + int(var2)
  elif op == '-':
    print('Subtracting numbers...')
    return int(var1) - int(var2)
  elif op == '*':
    print('Multiplying numbers...')
    return int(var1) * int(var2)
  elif op == '/':
    print('Dividing numbers...')
    if var2 == 0:
      return "infinity"
    else:
      return int(var1) / int(var2)
  else:
    return 0

# check for precedence of operators
# returns True if op2 has higher precedence than op1
def hasPrecedence(op1, op2):
  if op2 == '(' or op2 == ')':
    return False
  elif (op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-'):
    return False
  else:
    return True

# Sample expression
expr = raw_input("Enter the expression:")

# breaking down the expression into tokens
tokens = map(str, expr)
# removing the spaces from the list of tokens
tokens = ' '.join(tokens).split()

# stack to hold operands/numbers
var = Stack()
# stack to hold operators and parenthesis
ops = Stack()

# this is to inform the outer for loop
# to skip iteration for elements which together
# for a number, like 1,7 for 17
# we would not want 7 to be pushed again in our stack
skip = 0
for i in range(len(tokens)):
  # if skip is more than 0 skip the iteration
  if skip >= 1:
    # decrement skip flag
    skip -= 1
    continue
  # if we found a number
  if tokens[i] >= '0' and tokens[i] <= '9':
    num = tokens[i]
    # look for consecutive digits and append to num
    for j in range(i+1, len(tokens)):
      if tokens[j] >= '0' and tokens[j] <= '9':
        num = num + tokens[j]
        skip += 1
      else:
        break
    # push the number into var stack
    var.push(num)
    print(var.show())
  
  # if we find a opening parenthesis
  elif tokens[i] == '(':
    # add it to the ops stack
    ops.push(tokens[i])
  
  # if we find a closing parenthesis
  elif tokens[i] == ')':
    print("Encountered closing parenthesis...")
    while ops.peek() != '(':
      # solve the expression uptil this point
      value = applyOp(ops.pop(), var.pop(), var.pop())
      if(value == "infinity"):
        print("Invalid Expression")
        break
      else:
        print(value)
        var.push(value)
    ops.pop()
  
  # if we find any operator
  elif tokens[i] in ('+','-','*','/'):
    while ops.isEmpty() is False and hasPrecedence(tokens[i], ops.peek()):
      x = applyOp(ops.pop(), var.pop(), var.pop())
      print(x)
      var.push(x)
    # otherwise push the operator into ops stack
    ops.push(tokens[i])
    print(ops.show())

# by this point entire expression has been parsed
# now apply operators to values stored in var stack
while(ops.isEmpty() is False):
  var.push(applyOp(ops.pop(), var.pop(), var.pop()))

# print the final result 
print("Result of the expression is " + str(var.pop()))