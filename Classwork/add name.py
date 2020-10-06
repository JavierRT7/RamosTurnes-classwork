def subroutine(array):
  choice = 4
  while choice < 3 or choice > 3:
    while choice > 3 or choice < 1:
        print("1. Add name")
        print("2. Display list")
        print("3. Quit")
        choice = input("Enter your choice:")
        if choice.isdigit:
            choice = int(choice)
            if choice > 3 or choice < 1:
                print("Invalid choice")
            #End If
        else:
            print("Invalid choice")
        #End If
    #End While
    if choice == 1:
        name = input("Enter the name to be added to the list")
        choice = 4
        location = input("Enter the position in the list to insert the name:")
        if location.isdigit:
            location = int(location)
            array[location - 1] = name
            print(location, array[location - 1])
        else:
            print("Invalid choice")
        #End If
        choice = 4
    #End If 
    if choice == 2:
        for counter in range(0, 9):
            print(array[counter])
        #Next
        choice = 4
    #End If
  #End While
  print("Program terminated")
#End Procedure
array = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
subroutine(array)
