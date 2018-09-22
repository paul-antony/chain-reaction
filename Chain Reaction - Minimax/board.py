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
	#                   2) m --> the number of rows for the board
	#                   3) n --> the number of columns for the board
	#                   4) player --> used to determine which player's turn it is at any particular instance
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
	#                   2) pos --> the position (index) of any cell in the m*n board
	# Output:           self.board[pos[0]][pos[1]] --> the number of orbs present in the given cell position
	# Logic:            This function is used to return the number of orbs in a particular cell.
	# Example Call:     self.__getitem__([0,1])
	#
	#
	def __getitem__(self, pos):
		return self.board[pos[0]][pos[1]]

	#
	#
	# Function Name:    __setitem__()
	# Input:            1) self --> the object of the class
	#                   2) pos --> the position (index) of any cell in the m*n board
	#                   3) value --> the number of orbs present in the given cell position
	# Output:           None
	# Logic:            This function is used to assign the number of orbs to the board position.
	# Example Call:     self.__setitem__([0,1], 2)
	#
	#
	def __setitem__(self, pos, value):
		self.board[pos[0]][pos[1]] = value

	#
	#
	# Function Name:    __str__()
	# Input:            self --> the object of the class
	# Output:           state --> the current state of the board
	# Logic:            This function is used to return the current state of the board (as a string).
	# Example Call:     self.__str__()
	#
	#
	def __str__(self):
		state = ""
		for i in xrange(self.m):
			for j in xrange(self.n):
				state += str(self.board[i][j])
				state += " "
			state += "\n"
		return state

	#
	#
	# Function Name:    criticalMass()
	# Input:            1) self --> the object of the class 
	#                   2) pos --> the position (index) of any cell in the m*n board
	# Output:           1) 2 --> the critical mass of the given cell if it is a corner cell
	#                   2) 3 --> the critical mass of the given cell if it is an edge cell
	#                   3) 4 --> the critical mass of the given cell if it is a cell inside the board
	# Logic:            This function is used to return the critical mass of a particular cell. If the cell is a corner, then the critical mass of that cell is 2. 
	#					If it is an edge cell, then the critical mass of that cell is 3. And if it is a cell inside the board, then the critical mass of that cell 
	#					is 4.
	# Example Call:     self.criticalMass([0,1])
	#
	#
	def critical_mass(self, pos):
		if pos == (0, 0) or pos == (self.m-1, self.n-1) or pos == (self.m-1, 0) or pos == (0, self.n-1):
			return 2
		elif pos[0] == 0 or pos[0] == self.m-1 or pos[1] == 0 or pos[1] == self.n-1:
			return 3
		else:
			return 4

	#
	#
	# Function Name:    neighbors()
	# Input:            1) self --> the object of the class 
	#					2) pos --> the position (index) of any cell in the m*n board
	# Output:           neighborsList --> the list of neighbors of the given cell
	# Logic:            This function is used to return the list of orthogonally adjacent neighbors of a particular cell.
	# Example Call:     self.neighbors([0,1])
	#
	#
	def neighbors(self, pos):
		neighbors_list = []
		for i in [(pos[0],pos[1]+1), (pos[0],pos[1]-1), (pos[0]+1,pos[1]), (pos[0]-1,pos[1])]:
			if 0 <= i[0] < self.m and 0 <= i[1] < self.n:
				neighbors_list.append(i)
		return neighbors_list





	def input(self, state):
		for pos in [(x,y) for x in range(self.m) for y in range(self.n)]:
			self.board[pos[0]][pos[1]] = state[pos[0]][pos[1]]




	#
	#
	# Function Name:    valid_move()
	# Input:            self --> the object of the class 
	# Output:           valid --> the list of moves valid for a player
	# Logic:            This function is used to find and return the list of valid moves a player can take at any given state.
	# Example Call:     self.valid_move()
	#
	#             
	def valid_move(self):
		valid = []
		for pos in [(x,y) for x in range(self.m) for y in range(self.n)]:
			if cell_owner(board[pos]) == player or cell_owner(board[pos]) == 0:
				valid.append(pos)
		return valid

	#
	#
	# Function Name:    move()
	# Input:            1) self --> the object of the class 
	#                   2) pos --> the position (index) of any cell in the m*n board
	# Output:			None
	# Logic:            This function is used to execute a move by us. This includes putting an orb at the given cell and also the resulting chain reaction if the 
	#					cell has reached its critical mass.
	# Example Call:     self.valid_move()
	#
	#     
	def move(self, pos):
		self.board[pos[0]][pos[1]] += self.player
 		unstable = []
 		unstable.append(pos)
		for pos in unstable:
			if abs(self.board[pos[0]][pos[1]]) >= self.critical_mass(pos):
				self.board[pos[0]][pos[1]] -= self.player * self.critical_mass(pos)
					for i in self.neighbors(pos):
						self.board[i[0]][i[1]] = self.player * (abs(self.board[i[0]][i[1]]) + 1)
						unstable.append(i)
		self.player *= -1      

	#
	#
	# Function Name:    cell_owner()
	# Input:            n --> the number of orbs at a particular cell 
	# Output:			1) 0 --> if the cell is not owner by anyone
	#                   2) n/abs(n) --> the owner of the given cell position
	# Logic:            This function is used to execute a move by us. This includes putting an orb at the given cell and also the resulting chain reaction if the 
	#					cell has reached its critical mass.
	# Example Call:     self.valid_move()
	#
	# 
	def cell_owner(n):
		if n == 0:
			return 0
		else:
			return n/abs(n)

	#
	#
	# Function Name:    cal_heuristics()
	# Input:            self --> the object of the class 
	# Output:           heuristicValue --> the heuristic value in a given state
	# Logic:            This function is used to find and return the heuristic value at a particular state of the board. For finding the heuristic value, we take 
	#					into account the number of our orbs present on the board, the number of our opponent's orbs present on the board, our orb cells that are
	#					about to reach their critical mass and our opponent neighboring cells that are about to reach their critical mass.  
	# Example Call:     self.neighbors([0,1])
	#
	#
	def cal_heuristics(self):
		heuristic_value = 0
		my_orbs, opponent_orbs = 0, 0
		for pos in [(x,y) for x in xrange(board.m) for y in xrange(board.n)]:
			if cell_owner(board[pos]) == player:
				my_orbs += abs(board[pos])
				flag_not_vulnerable = True
				for i in board.neighbors(pos):
					if cell_owner(board[i]) == -player and (abs(board[i]) == board.critical_mass(i)-1):
						heuristic_value -= 5-board.critical_mass(pos)
						flag_not_vulnerable = False
				if flag_not_vulnerable:
					if board.critical_mass(pos) == 3:
						heuristic_value += 2
					elif board.critical_mass(pos) == 2:
						heuristic_value += 3
					if abs(board[pos]) == board.critical_mass(pos)-1:
						heuristic_value += 2
			else:
				opponent_orbs += abs(board[pos])
		heuristic_value = my_orbs - opponent_orbs
		if opponent_orbs == 0 and my_orbs > 1:
			return 10000
		elif my_orbs == 0 and opponent_orbs > 1:
			return -10000
		return heuristic_value

