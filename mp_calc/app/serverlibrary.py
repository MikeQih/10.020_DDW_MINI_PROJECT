
# 过程：
# cd mp_calc 
# python -m pipenv shell

# cd app/static
# python -m transcrypt -b -n clientlibrary

# cd ..
# cd ..

# flask db init
# flask db migrate
# flask db upgrade
# flask run 

# def mergesort(array, byfunc=None):
#   pass

def mergesort(array, byfunc=None):
  if len(array) <= 1:
        return

  if byfunc is None:
      byfunc = lambda x: x  # Default comparison function for elements

  middle = len(array) // 2
  left = array[:middle]
  right = array[middle:]

  mergesort(left, byfunc)
  mergesort(right, byfunc)

  result = []
  i = j = 0

  while i < len(left) and j < len(right):
      if byfunc(left[i]) < byfunc(right[j]) or (byfunc(left[i]) == byfunc(right[j]) and left[i] < right[j]):
          result.append(left[i])
          i += 1
      else:
          result.append(right[j])
          j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  # Modify the original array in place
  array.clear()
  array.extend(result)


class Stack:
  # pass
  def __init__(self):
        self.__items = []
        
  def push(self, item):
      self.__items.append(item)

  def pop(self):
      if not self.is_empty:
          return self.__items.pop()
      return None

  def peek(self):
      if not self.is_empty:
          return self.__items[-1]
      return None

  @property
  def is_empty(self):
      return len(self.__items) == 0

  @property
  def size(self):
      return len(self.__items)


class EvaluateExpression:
  # copy the other definitions
  # from the previous parts

  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    # pass
    self._expression = ""
    self.expression = string

  @property
  def expression(self):
    # pass
    return self._expression


  @expression.setter
  def expression(self, new_expr):
    # pass
    # Check if the new expression contains only valid characters
    if all(char in self.valid_char for char in new_expr):
        self._expression = new_expr
    else:
        print("Invalid characters in expression. Expression not set.")
        self._expression = ""
  
  #上面的都是copied的

  def insert_space(self):
    # pass
    operators = "+-*/()"
    result = ""
    for char in self._expression:
        if char in operators:
            result += " " + char + " "
        else:
            result += char
    return result  # Remove leading/trailing spaces
  
  #上面的都是copied的
  
  def process_operator(self, operand_stack, operator_stack):
    # pass
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    # Pop the top operator from the operator stack
    operator = operator_stack.pop()

    # Pop the top two operands from the operand stack
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()

    # Perform the operation based on the operator
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if operand2 != 0:
            result = operand1 // operand2
        else:
            raise ValueError("Division by zero is not allowed")

    # Push the result back onto the operand stack
    operand_stack.push(result)


  def evaluate(self):
    # operand_stack = Stack()
    # operator_stack = Stack()
    # expression = self.insert_space()
    # tokens = expression.split()
    # pass
    
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()

    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    for token in tokens:
        if token.isnumeric():
            operand_stack.push(float(token))
        elif token in "+-*/":
            while (
                not operator_stack.is_empty
                and operator_stack.peek() in "+-*/"
                and precedence[token] <= precedence[operator_stack.peek()]
            ):
                self.process_operator(operand_stack, operator_stack)
            operator_stack.push(token)
        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            while not operator_stack.is_empty and operator_stack.peek() != "(":
                self.process_operator(operand_stack, operator_stack)
            if not operator_stack.is_empty and operator_stack.peek() == "(":
                operator_stack.pop()

    while not operator_stack.is_empty:
        self.process_operator(operand_stack, operator_stack)

    return operand_stack.peek()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]