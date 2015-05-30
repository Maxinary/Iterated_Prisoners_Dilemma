class Board():
	def __init__(self,player_one, player_two):
		self.playermoves = []#True is cooperate, False is defect 
				     #Format is [[p1move,p2move],[p1move,p2move]]
		self.points = [0,0]
		self.player_one = player_one
		self.player_two = player_two

	def play(self,roundnum):
		for i in range(roundnum):
			self.round()
		if self.points[0] < self.points[1]:
			return self.player_one.__name__+" wins"
		elif self.points[1] < self.points[0]:
			return self.player_one.__name__+" wins"

		else:
			return "It's a tie"
	def round(self):
		self.playermoves.append([self.player_one(), self.player_two()])
		if self.playermoves[-1][0] == True and self.playermoves[-1][1] == True:
			self.points[0] += 1
			self.points[1] += 1
		elif self.playermoves[-1][0] == False and self.playermoves[-1][1] == False:
			self.points[0] += 2
			self.points[1] += 2
		elif self.playermoves[-1][0] == True and self.playermoves[-1][1] == False:
			self.points[0] += 3
		else:
			self.points[1] += 3
		#print(self.playermoves[-1])
		#print(self.points)
