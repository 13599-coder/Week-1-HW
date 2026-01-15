num_records = int(input('Enter the number of how many potential job opportunities that you would like to record. ')) # get number of records
with open('records.txt','w') as record_file: # Open file for writing
  going = 'y'
  while going == 'y' or going == 'Y':
    print(f'Enter data for record ')
    # get fields for a record
    job = input('Job: ')
    money = input('Money: ')
    hours = input('Hours: ')
    # write record to file
    record_file.write(f'{job}\n')
    record_file.write(f'{money}\n')
    record_file.write(f'{hours}\n')
    going =  input('Y = continue, anything else will end the loop')
found =
with open('records.txt','r') as record_file:
  job = record_file.readline()
  while job != '':
    money = int(record_file.readline())
    hours = float(record_file.readline())
    job = job.rstrip('\n')
    print() # prints a blank line
    print(f'job: {job}')
    print(f'money: {money}')
    print(f'hours: {hours}')

    job = record_file.readline()



print() # prints a blank line
print('Records have been written to records.txt')
