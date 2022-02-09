import matplotlib.pyplot as plt

points_scored = [90, 94, 53, 89, 80, 86, 69, 52, 76, 96, 77, 68, 66, 67, 66, 79, 68, 64, 78, 51, 90, 81]
games = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
plt.plot(games, points_scored, linewidth=2)
plt.title("Team Points Scored Each Game", fontsize=22)
plt.xlabel("Number of games", fontsize=14)
plt.ylabel("Points", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()