user_minutes = int(input("How many minutes do you want to enter?")
with open("step_counter",'w') as minutes_file:
  for minute in range(1, user_minutes + 1):
    minutes = input('#{num} what would you like to add to your mintues file? : ')
    minutes_file.write(f"{minutes}\n")
  mintues_file.close()

  
    
