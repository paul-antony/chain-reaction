import copy

class Board():
	def __init__(self, m = 9, n = 6, player = 1):
		self.m = m
		self.n = n
		self.board = [[0 for i in range(self.n)] for i in range(self.m)]
		self.player = player

	def __getitem__(self, pos):
		return self.board[pos[0]][pos[1]]

	def __setitem__(self, pos, value):
		self.board[pos[0]][pos[1]] = value

	def __str__(self):
		state = ""
		for i in range(self.m):
			for j in range(self.n):
				state += str(self.board[i][j])
				state += " "
			state += "\n"
		return state

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
		for i in range(self.m):
			for j in range(self.n):
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
        #                                       If it is an edge cell, then the critical mass of that cell is 3. And if it is a cell inside the board, then the critical mass of that cell 
        #                                       is 4.
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
        #                   2) pos --> the position (index) of any cell in the m*n board
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
        #
        #
        # Function Name:    input()
        # Input:            1) self --> the object of the class 
        #                   2) state --> Board state as a 2d list
        # Output:           None
        # Logic:            used to set the board state.
        # Example Call:     self.input(state)
        #
        #



	def input(self, state, player):
		for pos in [(x,y) for x in range(self.m) for y in range(self.n)]:
			self.board[pos[0]][pos[1]] = state[pos[0]][pos[1]]
		self.player = player

	def valid_move(self):
		if self.cal_heuristics() in [200,-200]:
			return []
		valid = []
		for pos in [(x,y) for x in range(self.m) for y in range(self.n)]:
			if self.board[pos[0]][pos[1]]/self.player >= 0:
				valid.append(pos)
		return valid
        #
        #
        # Function Name:    invalid_move()
        # Input:            self --> the object of the class 
        # Output:           invalid --> the list of invalid moves for a player
        # Logic:            This function is used to find and return the list of invalid moves for a player at any given state.
        # Example Call:     self.invalid_move()
        #
        # 

	def invalid_move(self):
		invalid = []
		for pos in [(x,y) for x in range(self.m) for y in range(self.n)]:
			if self.board[pos[0]][pos[1]]/self.player < 0:
				invalid.append(pos)
		return invalid

	def move(self, pos):
		self.board[pos[0]][pos[1]] += self.player
		unstable = []
		unstable.append(pos)
		while len(unstable) > 0:
			pos = unstable.pop(0)
			if self.cal_heuristics() in [200,-200]:
				break
			if abs(self.board[pos[0]][pos[1]]) >= self.critical_mass(pos):
				self.board[pos[0]][pos[1]] -= self.player * self.critical_mass(pos)
				for i in self.neighbors(pos):
					self.board[i[0]][i[1]] = self.player * (abs(self.board[i[0]][i[1]]) + 1)
					unstable.append(i)
		self.player *= -1      

        #
        #
        # Function Name:    cal_heuristics()
        # Input:            self --> the object of the class 
        # Output:           heuristicValue --> the heuristic value in a given state
        # Logic:            This function is used to find and return the heuristic value at a particular state of the board. For finding the heuristic value, we take 
        #                   into account the number of our orbs present on the board, the number of our opponent's orbs present on the board, our orb cells that are
        #                   about to reach their critical mass and our opponent neighboring cells that are about to reach their critical mass.  
        # Example Call:     self.neighbors([0,1])
        #
        #

	def cal_heuristics(self,player = 1):

		heuristic_value = 0

		positive_orbs, negative_orbs = 0, 0

		for pos in [(x,y) for x in range(self.m) for y in range(self.n)]:
			if self.board[pos[0]][pos[1]] > 0:
				positive_orbs += self.board[pos[0]][pos[1]]
			else:
				negative_orbs += self.board[pos[0]][pos[1]]

		heuristic_value = positive_orbs + negative_orbs

		if negative_orbs == 0 and positive_orbs > 1:
			heuristic_value = 200

		elif positive_orbs == 0 and negative_orbs < -1:
			heuristic_value = -200

		return heuristic_value * player

	def list(self):
		state = []
		for i in range(self.m):
			for j in range(self.n):
				state.append(self.board[i][j])
		return state

	def reset(self):
		self.board = [[0 for i in range(self.n)] for i in range(self.m)]
		self.player = 1
