### SRC - I think you are on to something here
### I like the mathematical approach, but this
### code didn't work for me, and there's no validation.

import random
playing = True
player_choice = 1
computer_choice = 1
answer = 1
while playing == True:
    player_choice = int(input("Enter your choice: enter 1 for rock, 2 for paper or 3 for scissors"))
    computer_choice = random.randint(1,4)
    if player_choice + 2 == computer_choice:
        print("You win!")
    elif computer_choice + 2 == player_choice:
        print("Computer wins!")        
    elif player_choice + 1 == computer_choice:
        print("Computer wins!")
    elif computer_choice + 1 == player_choice:
        print("You win!")
    elif computer_choice == player_choice:
        print("It's a draw!")
    #End If
    answer = int(input("Would you like to play again? Type 1 for yes or type 2 for no"))
    if answer == 2:
        playing = False
    #End If
#End While







