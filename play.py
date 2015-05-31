from board import Board
from techniques import melkor, eru_iluvatar, random, tit_for_tat, massive_retaliatory_strike
techniques = [melkor, eru_iluvatar, random, tit_for_tat, massive_retaliatory_strike]

technipoints = []
for i in techniques:
	technipoints.append(0)
	for j in techniques:
		gameboard = Board(i, j)
		print(gameboard.play(100))
		print(gameboard.player_one.__name__+" spent " + str(gameboard.points[0]) + " years in prison")
		print(gameboard.player_two.__name__+" spent " + str(gameboard.points[1]) + " years in prison\n")
		technipoints[-1] += gameboard.points[0]

print("\n")
for i in range(len(techniques)):
	print(techniques[i].__name__+" spent "+str(technipoints[i]) + " years in prison")
