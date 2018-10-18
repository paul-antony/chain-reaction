from board import *


b = Board()
b.move((1,1))
print(b)
print(b.list())
print(b.player)
b.reset()
print(b)
print(b.player)