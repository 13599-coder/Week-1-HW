#Name: Evan Machica
#Period 6
#try_and_exceptHW
#Time Spent
def math_ops(a, b):
  add = a + b
  sub = a - b
  mul = a * b
  try: 
    div = a / b
  except:
    div = "cannot be divided by zero"
  return add, sub, mul, div
print('Welcome to your very basic calculator!!!!')
try:
  operation = (input('Which operation would you like your calculator to perform? Add/Sub/Divide/Multiple: ')).lower()
  num_1 = float(input('enter the first number: '))
  num_2 = float(input('enter the second number: '))
  a, s, m, d = math_ops(num_1, num_2)
  if operation == "add":
    print("addition:", a)
  elif operation == "sub":
    print("subtractaion:", s)
  elif operation == "multiple":
    print("multiplication:", m)
  elif operation == "divide":
    print("division:", d)
  else: 
    print("invalid operation")

file = open("calculator_file.txt, "a")
file.write(f"{num1}, {num2}\n")
file.write(f"add: {add}\n")
file.write(f"sub: {sub}\n")
file.write(f"mul: {mul}\n")
file.write(f"div: {div}\n")
file.close()
except ValueError:
  print('please enter only interger values.')
except ZeroDivisionError:
  print("excuse me you cant divide by zero...")
