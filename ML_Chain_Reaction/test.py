from board import *


def act_convert(action):
	return (int(action/6),action%6)

#b = Board()
#b.move((1,1))
#print(b)
#print(b.list())
#print(b.player)
#b.reset()
#print(b)
#print(b.player)

print(act_convert(10))