#Name: Evan Machica
#Period 6
#try_and_exceptHW
#Time Spent
def math_ops(a, b):
  add = a + b
  sub = a - b
  mul = a * b
  div = a / b
  return add, sub, mul, div
print('Welcome to your very basic calculator!!!!')
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
