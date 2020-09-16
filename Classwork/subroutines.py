def multiples(table, startnum, endnum, pupilName):
    print("Hi,", pupilName, "here is your times table:")
    for count in range (startnum, endnum + 1):
        print(table, "x", count, "=", table * count)
    #Next
#End Procedure
pupilName = input("What is your name?")
table = int(input("Please enter the times table you want to display"))
startnum = int(input("Where do you want the table to start?"))
endnum = int(input("Where do you want the table to end?"))
multiples(table, startnum, endnum, pupilName)