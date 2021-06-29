again = True
while again == True:
    answer = input("Are you American?")
    if answer == "yes":
        print("Fuck You!")
    else:
        answer = input("Is it savoury?")
        if answer == "yes":
            answer = input("Is it steamed?")
            if answer == "yes":
                answer = input("Does it contain suet?")
                if answer == "yes":
                    answer = input("Does it contain flour?")
                    if answer == "yes":
                        print("It is a pudding!")
                    else:
                        print("It is not a pudding")
                else:
                    print("It's not a pudding")
            else:
                print("It is not a pudding")
        else:
            answer = input("Does it contain milk?")
            if answer == "yes":
                answer = input("Does it contain fruit?")
                if answer == "yes":
                    answer = input("Does it contain egg?")
                    if answer == "yes":
                        answer = input("Is it steamed or baked?")
                        if answer == "yes":
                            print("It is a pudding!")
                            answer = input("Is it milk-thickened?")
                            if answer == "yes":
                                print("It is a blancmange!!! not a pudding idiot!")
                            else:
                                print("It's still just a pudding")
                        else:
                            print("It's not a pudding")
                    else:
                        print("It's not a pudding")
                else:
                    print("It is not a pudding")
            else:
                answer = input("Is it gelatine based?")
                if answer == "yes":
                    print("It is a jelly! not a pudding!")
                else:
                    print("It is nothing")
    answer = input("Do you want to go again?")
    if answer == "no":
        again = False