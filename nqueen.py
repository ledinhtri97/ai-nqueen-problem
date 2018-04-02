import time, random
from operator import itemgetter

MAXITER = 5000
ROW, COL = range(2)


class Board(object):
	def __init__(self, n):
		self.n = n
		self.queens = []
		self.board = []
	
	def printQueens(self):
		# prints location of queens
		list = []
		for queen in self.queens:
			list.append((queen[ROW], queen[COL]))
		print ('Possible Location =', list)

	def findSolution(self):
		# solves n-queens problem up until max iteration
		# returns True if solution is found and False if exceeds max iteration
		it = 0
		solution = False
		while not solution and it < MAXITER:
			solution = self.move()
			it += 1
		if it == MAXITER:
			return False
		return True

	def move(self):
		# adds queen or moves queen
		# returns True if a solution is found, False otherwise

		# Initalize board with greedy approach
		if len(self.queens) < self.n:
			possibleMoves = []
			[possibleMoves.append(self.numConflictsByPos(row, len(self.queens))) for row in range(self.n)]
			nextMove = min(enumerate(possibleMoves), key=itemgetter(1))[0]
			self.board[nextMove][len(self.queens)] = 1
			self.queens.append([nextMove, len(self.queens)])
			return False
	
		# Deal with conflicted queens
		else:
			conflicted = self.conflictedQueens()

			# Base case: problem is solved when there are no conflicts
			if len(conflicted) == 0:
				return True

			# Move random queen in conflict set
			queen = random.choice(conflicted)

			# Choose move based on minimum number of conflicts and randomly breaking ties
			possibleMoves = []
			[possibleMoves.append(self.numConflictsByPos(row, queen[COL])) for row in range(self.n)]
			nextMove = random.choice(min(enumerate(possibleMoves), key=itemgetter(1)))
			if nextMove == queen[ROW]:
				possibleMoves[nextMove] = 8	# sets smallest to max conflicts (8)
				nextMove = random.choice(min(enumerate(possibleMoves), key=itemgetter(1)))

			# Update board
			self.board[queen[ROW]][queen[COL]] = 0
			self.board[nextMove][queen[COL]] = 1

			# Update queen in queens list
			for i in range(len(self.queens)):
				if self.queens[i] == queen:
					self.queens[i][ROW] = nextMove
					self.queens[i][COL] = queen[COL]
			return False

	def conflictedQueens(self):
		# returns list of queens that are in conflict with another
		conflict = []
		for queen in self.queens:
			if self.numConflictsByPos(queen[ROW], queen[COL]) > 0:
				conflict.append(queen)
		return conflict

	def numConflictsByPos(self, row, col):
		# checks constraints: unique row, col and diagonal for each queen placed
		# returns # of conflicts at position
		conflicts = 0
		for q in self.queens:
			if q[COL] != col and (q[ROW] == row or abs(q[ROW] - row)==abs(q[COL] - col)):
				conflicts += 1
		return conflicts

	def printBoard(self):
		# prints board at current state
		for row in self.board:
			line = str()
			for pos in row:
				if pos == 0:
					line += '- '
				else:
					line += 'Q '
			print (line)
		print ('')

	def emptyBoard(self):
		# initiates an empty nxn board
		for row in range(self.n):
			self.board.append([])
			for col in range(self.n):
				self.board[row].append(0)


if __name__ == '__main__':

	# User input, validify user input
	n = ''
	print ('Input an integer value 4 <= n <= 15.')
	while type(n) != int or (int(n) < 4 or int(n) > 15):
			try:
				n = int(input('n = '))
				if not isinstance(n, int):
					print ('Invalid input')
			except NameError:
				print ('Invalid input')

	start_time = time.time()

	solution = False
	b = Board(n)
	b.emptyBoard()
	b.printBoard()
	solution = b.findSolution()

	# Randomizes if solution is not found within max number of iterations
	while not solution:
		b = Board(n)
		b.emptyBoard()
		solution = b.findSolution()

	b.printQueens()
	b.printBoard()

	elapsed_time = time.time() - start_time
	print ('%.3f milliseconds' % (elapsed_time*1000))