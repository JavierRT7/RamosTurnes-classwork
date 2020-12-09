leaderboard = {'Bob': 16, 'James': 24, 'Daniel': 55, 'Matt': 4}
leaderboard_list = []
leaderboard_names = []
finished = False
while finished == False:
    score = input("Please input the score achieved")
    name = input("Who achieved that score?")
    leaderboard[name] = score
    answer = input("Do you want to enter another score? (Y/N)")
    if answer == "N":
        finished = True
    #End If
#End While
for counter in range(len(leaderboard)):
    leaderboard_list[counter] = leaderboard
#Next
leaderboard_list.sort
print(leaderboard)
print(leaderboard_list)