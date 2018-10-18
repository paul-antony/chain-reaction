#game replay buffer and pre process of training data

# buffer type (board,action,board_q,reward)

class replay_byffer:

	def __init__(self):
		self.buffer = []

	def reset(self):
		self.buffer = []

	
	def push(self,item):
		buffer.append(item)

	def process(self):
		#process the buffer
		x = []
		y = []
		for