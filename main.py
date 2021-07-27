#addition
def add(n1,n2):
  return n1 + n2

#subtraction  
def subtract(n1,n2):
  return n1 - n2

#multiply
def multiply(n1,n2):
  return n1 * n2

#divide
def divide(n1,n2):
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
  }
def calculate():
  
  print(logo) #recursion
  num1 = float(input("What's the first number?:"))
  for operation_sign in operations:
    print(operation_sign)
  calculation_done = False
  while not calculation_done:
    operation_pick = input("Pick an operation:")
    calculation_function = operations[operation_pick]
    num2 = float(input("What's the next number?:"))
    first_answer = calculation_function(num1,num2)
    print(f"{num1} {operation_pick} {num2} = {first_answer}")
    ask = input("Type 'y' to continue calculating with {first_answer}, or type 'n' to start again:")
    if ask == 'y':
      num1 = first_answer
    else:
      calculation_done = True
      calculate()

calculate()  
  
 
