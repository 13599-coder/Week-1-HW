user_years = int(input('Enter the amount of years you would like to add: '))
file_variable = open('example_file.txt','w')
  for num in range(1, num_lines + 1):
entry = input('#{num} What would you like to add to the file? ')
file_variable.write(f'{entry}\n')
file_variable.close
file_object = open('example.txt','r')
  for line in file_object:
print(line)
file_object.close
num_list= open('num_list.txt', 'r')
line = num_list.readline()
sum = 0
while line != '':
    sum += int(line)
    line = num_list.readline()
num_list.close()
print(f'The sum of the numbers in the list is {sum}')
