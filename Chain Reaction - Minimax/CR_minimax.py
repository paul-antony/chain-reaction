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


class Board:
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
                self.board = [[0 for i in range(self.n)] for i in range(self.m)]
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
                for i in range(self.m):
                        for j in range(self.n):
                                s += str(self[(i,j)])
                                s += " "
                        s += "\n"
                return s
        


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

        def input(self,state):
                for pos in [(x,y) for x in range(self.m) for y in range(self.n)]:
                        self.board[pos[0]][pos[1]] = state[pos[0]][pos[1]]