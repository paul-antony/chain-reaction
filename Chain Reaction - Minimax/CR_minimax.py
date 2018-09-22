#
#
# Task Name:        Implementation of MiniMax algorithm in Chain Reaction
# Author List:      Job Jacob, Paul Antony
# File Name:        CR_minimax.py
# Functions:        
#
# Global variables:
#
#


class Board():
	#
	#
	# Function Name:    __init__()
	# Input:            1) self --> the object of the class
	#					2) m --> the number of rows for the board
	#					3) n --> the number of columns for the board
	#					4) player --> used to determine which player's turn it is at any particular instance
	# Output:           None
	# Logic:            This function is used to initialize the Board object variables. 
	# Example Call:     Board.__init__(9, 6, 1)
	#
	#
	def __init__(self, m=9, n=6, player=1):
		self.m = m
		self.n = n
		self.board = [[0 for i in xrange(self.n)] for i in xrange(self.m)]
		self.player = player

	#
	#
	# Function Name:    __getitem__()
	# Input:            1) self --> the object of the class
	#					2) pos --> 
	# Output:           None
	# Logic:            This function is used to return the number of orbs in a particular cell.
	# Example Call:     self.__getitem__([0,1])
	#
	#
	def __getitem__(self, pos):
		return self.board[pos[0]][pos[1]]

	#
	#
	# Function Name:    __init__()
	# Input:            1) self --> the object of the class
	#					2) m --> the number of rows for the board
	#					3) n --> the number of columns for the board
	#					4) player --> used to determine which player's turn it is at any particular instance
	# Output:           None
	# Logic:            This function is used to return the number of orbs in a particular cell.
	# Example Call:     self.__getitem__([0,1])
	#
	#
	def __setitem__(self, pos, value):
		self.board[pos[0]][pos[1]]=value
	def __str__(self):
		s = ""
		for i in xrange(self.m):
			for j in xrange(self.n):
				s += str(self[(i,j)])
				s += " "
			s += "\n"
		return s
	def hash(self):
		return str(self.board)+str(self.new_move)
	def critical_mass(self,pos):
		if pos == (0,0) or pos == (self.m - 1, self.n - 1) or pos == (self.m - 1, 0) or pos == (0, self.n - 1):
			return 2
		elif pos[0] == 0 or pos[0] == self.m-1 or pos[1] == 0 or pos[1] == self.n-1:
			return 3
		else:
			return 4
	def neighbors(self,pos):
		n = []
		for i in [(pos[0],pos[1]+1), (pos[0],pos[1]-1), (pos[0]+1,pos[1]), (pos[0]-1,pos[1])]:
			if 0 <= i[0] < self.m and 0 <= i[1] < self.n:
				n.append(i)
		return n
	def move(board, pos):
		board = copy.deepcopy(board)
		assert board.new_move == sgn(board[pos]) or 0 == sgn(board[pos])
		board[pos] = board[pos] + board.new_move
		t = time.time()
		while True:
			unstable = []
			for pos in [(x,y) for x in xrange(board.m) for y in xrange(board.n)]:
				if abs(board[pos]) >= board.critical_mass(pos):
					unstable.append(pos)
			if time.time() - t >= 3:
				#Can't afford to spend more time, strange loop here!
				#print board, pos
				#raw_input()
				break
			#print board
			#raw_input()
			if not unstable:
				break
			for pos in unstable:
				board[pos] -= board.new_move*board.critical_mass(pos)
				for i in board.neighbors(pos):
					board[i] = sgn(board.new_move)*(abs(board[i])+1)
		board.new_move *= -1
		return board
	def input(self):
		

