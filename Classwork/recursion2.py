def sum(n):
    total = 0
    total = int(total)
    if n % 2 == 0:
        count = 1
        for counter in range(0, n + 1, 2):
            print("The", count, "even number is", counter)
            total = total + counter
            count = count + 1
        #Next
        print("The sum of the even numbers is", total)
    else:
        print("Invalid input")
    #End If
#End Procedure
number = 0
number = int(input("What number do you want to use"))
sum(number)
