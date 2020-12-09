leaderboard = {}
leaderboard_list = []
leaderboard_names = []
for counter in range (1,5):
    score = input("Please input the score achieved")
    name = input("Who achieved that score?")
    leaderboard[name] = score
    print(leaderboard)
#Next