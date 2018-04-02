class Board():
	"""initialzing Board class properties"""
	def __init__(self, N):
		self.N = N
		self.board = [0 for i in range(N)]
		self.cnt = 0
	


	def isSafe(self, Clm):
		"""check if new queen places on column number Clm
		attack previous queens (true) or not (false)"""
		for i in range(self.cnt):
			#print("clm = ",Clm ," | self.board[i] = ",self.board[i])
			#print("self.cnt = ",self.cnt, "| i = ", i)
			#print("===")
			if( (self.board[i]==Clm) | (abs(Clm-self.board[i]) == (self.cnt-i))):
				return False
		return True

	def Place(self, Clm):
		"""Places next queen in column number Clm"""

		if(Clm >= 0 & Clm < self.N):
			self.board[self.cnt] = Clm
			self.cnt = self.cnt + 1
			#print(self.board)
		else:
			print("Bad Column")

	def isGoal(self):
		"""if queens tha placed on chess is equal 
		to N that is goal state"""
		if(self.cnt == self.N):
			return True
		else: 
			return False

	def unPlace(self):
		"""unplace that previous place is bad, so do that
		by less one unit from cnt property"""
		if(self.cnt > 0):
			self.cnt = self.cnt - 1
	
	def showBoard(self):
		"""show board chess, where zip(*chess) is used to unzip each row in matrix"""
		chess = [['-' for i in range(self.N)] for j in range(self.N)]
		for x in range(self.cnt):
			chess[x][self.board[x]] = 'Q'
		print("\n".join(" ".join(row) for row in zip(*chess)))


def DFS(_board_):
	if (_board_.isGoal()):
		return _board_
	else:
		for i in range(_board_.N):
			#print(i," isSafe = ", _board_.isSafe(i))
			if(_board_.isSafe(i)):
				_board_.Place(i)
				res = DFS(_board_)
				if(res != None):
					return res
				#print("unplace")
				_board_.unPlace()
	return None
		

def main():
	N = int(input("Input NxN chess: N = "))
	chessNqueen = Board(N)
	res = DFS(chessNqueen)
	if(res != None):
		chessNqueen.showBoard()
	else:
		print("no result!")

main()