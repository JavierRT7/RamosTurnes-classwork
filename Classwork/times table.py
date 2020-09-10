table = 0
answer = False
while answer == False:
   table = input("Which times table do you want?")
   if table.isdigit():
       table = int(table)
   # End If
   answer_string = input("You chose " + str(table) + " do you want to proceed?")
   if answer_string == "yes":
       answer = True
   # End If
# End While
for counter in range (1, 150):
   multiplied = table * counter
   print(table, "multiplied by", counter , "is", multiplied)
# Next




