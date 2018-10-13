from board import *
from minmax import *




def test():
	b=Board()
	#print(b)
	#b.input(((0,0,0,0,0,0),(0,0,0,0,0,0),(0,0,0,1,-1,0),(0,0,2,-3,3,-1),(0,-1,-3,3,-3,0),(0,0,1,3,0,1),(0,0,-1,-1,0,0),(0,0,0,0,0,0),(0,0,0,0,0,0)))
	#print(b)
	#b.move((4,3))
	#print(b)
	#print(b.player)
	#print(b.valid_move())
	#b.move((0,0))
	#print(b)
	#print(b.cal_heuristics())
	#b.player *= -1
	print("Present State:")
	b.input(((1,2,-1,2,2,1),(2,-1,-1,-1,3,2),(2,2,-1,3,3,2),(2,0,3,-2,-1,2),(-1,3,-1,-3,-1,-1),(-2,-3,-2,-3,-2,-2),(-2,-2,3,-3,-1,-2),(-1,3,-1,-1,3,2),(1,2,2,2,1,1)))
	print(b)
	print("Best Move:",minmax(b))
	#print(b)
	#print(b.valid_move())
	#print(b.cal_heuristics())
	#b.move((4,2))


test()
