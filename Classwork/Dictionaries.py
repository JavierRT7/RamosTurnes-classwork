import json
with open('data.json', 'r') as f:
	data = json.load(f)
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
print(leaderboard)
print(leaderboard_list)