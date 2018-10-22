from board import *
from buffer import *


a = [1,2,3,4,5,6]
c = ['a','b','c','d','e','f']
d = [[7,8,9,10,11,12],['g','h','i','j','k','l']]
b = [[1,2],
[3,4],
[5,6]]

#print(replay_byffer.convert_to_1d(b))
#print(replay_byffer.convert_to_1d(b))
#print(replay_byffer.flip_vertical(b))
#print(replay_byffer.flip_horizontal(b))
#print([a,c])
#temp = replay_byffer.remove_duplicate(replay_byffer.mirror([[a,c],d],3,2))

#for i in temp:
	#print(i)

temp = replay_byffer.random_selector(replay_byffer.remove_duplicate([[[5, 6, 3, 4, 1, 2], ['e', 'f', 'c', 'd', 'a', 'b']],
[[5, 6, 3, 4, 1, 2], ['e', 'f', 'c', 'd', 'a', 'b']],
[[2, 1, 4, 3, 6, 5], ['b', 'a', 'd', 'c', 'f', 'e']],
[[2, 0, 4, 3, 6, 5], ['b', 'a', 'd', 'c', 'f', 'e']]]))



print(temp)