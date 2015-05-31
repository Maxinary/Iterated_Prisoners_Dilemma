from random import randint
def melkor(board):
	return False

def eru_iluvatar(board):
	return True

def random(board):
	return bool(randint(0,1))

def tit_for_tat(board):
	if board.playermoves != []:
		if board.player_one.__name__ == __name__:
			return board.playermoves[-1][1]
		else:
			return board.playermoves[-1][0]
	else:
		return True

def massive_retaliatory_strike(board):
	for i in board.playermoves:
		if i[0] == False or i[1] == False:
			print("Betrayal")
			return False
	return True
