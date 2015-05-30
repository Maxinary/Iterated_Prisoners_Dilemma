from board import Board
from techniques import melkor, eru_iluvatar, random

gameboard = Board(eru_iluvatar, melkor)
print(gameboard.play(100))
print(gameboard.player_one.__name__+" spent " + str(gameboard.points[0]) + " years in prison")
print(gameboard.player_two.__name__+" spent " + str(gameboard.points[1]) + " years in prison")
