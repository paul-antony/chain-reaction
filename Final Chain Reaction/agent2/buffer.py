#game replay buffer and pre process of training data


#buffer entry format(present_state,player,action,next_state,reward)
import pickle
import random
import copy


from DQN import *

train_network = QNetwork()

alpha = 0.9
gama = 0.9
max_size = 1000




class replay_buffer:

	def __init__(self):
		self.buffer = []
		self.alpha = alpha
		self.gama = gama 
		self.max_size = max_size
		self.size = 0

	def reset(self):
		self.buffer = []
		self.size = 0



	def push(self,item):
		input = item
		self.index_convert(input)

		if self.max_size - self.size == 0:
			self.pop(1)
		
		self.buffer.append(input)
		
		self.size += 1



	def pop(self,count):
		for i in range(0,count):
			self.buffer.pop(0)
			self.size -= 1


	def minibatch(self,size):
		
		output = random.sample(self.buffer,size)
		return copy.deepcopy(output)











###########################################################################################################
	def train(self,size,player):

		if size < self.size:
			batch = self.minibatch(size)

			train_network.load(player)

			batch = self.update_q(batch)
			batch = replay_buffer.illegal_move(batch)
			x,y = replay_buffer.x_y_split(batch)
			train_network.train(x,y)
			train_network.save(player)


	def update_q(self,input):

		output = []

		for entry in input:
			temp = []
			temp.append(entry[0])#board state

			present_state = entry[0][:]
			
			temp.append(train_network.qvalue(present_state,entry[4]))#q value

			if entry[4] in (1,-1):
				temp[1][entry[2]] = entry[4]#update q value
			
			else:	

				next_state = entry[3]

				max_q = max(train_network.qvalue(next_state,entry[4]))

				temp[1][entry[2]] = temp[1][entry[2]] + self.alpha * (entry[4] + self.gama * max_q - temp[1][entry[2]] )#update q value

			temp.append(entry[1])

			output.append(temp)
		
		return output


	@staticmethod
	def illegal_move(input):
		output = []
		for entry in input:
			temp = []
			temp.append(entry[0])
			temp.append(entry[1])

			invalid_index = replay_buffer.invalid_move(entry[0],entry[2])
			for i in invalid_index:
				temp[1][i] = -1
		
			output.append(temp)

		return output

	@staticmethod
	def invalid_move(input,player):
		invalid = []
		for pos in range(0,len(input)):
			if input[pos]/player < 0:
				invalid.append(pos)
		return invalid




	@staticmethod
	def x_y_split(input):
		x = []
		y = []
		for i in input:
			x.append(i[0])
			y.append(i[1])

		return (x,replay_buffer.limiter(y))

	@staticmethod
	def limiter(input,upper = 1,lower = -1):
		
		output = []
		for i in input:
			temp = []
			for j in i:

				if j>upper:
					temp.append(upper)
				elif j<lower:
					temp.append(lower)
				else:
					temp.append(j)
			output.append(temp)
		return output






###########################################################################################################

	@staticmethod
	def index_convert(input,m = 9, n = 6):
		input[2] = replay_buffer.index_1d(input[2],m,n)

	#converts 2d index to id index
	@staticmethod
	def index_1d(input,m = 9, n = 6):
		output = input[0]*n + input[1]
		return output








##############################################################################################################

if __name__ == "__main__":
	a = replay_buffer()
	#b = [1,2,3,4,5,6]
	#c = ['a','b','c','d','e','f']
	#a.push([b,1,(1,1),c,-1,0.9])

	filename = 'BUFFER.pickle'
	outfile = open('Buffer_Player1.pickle','wb')
	pickle.dump(a,outfile)
	outfile.close()

	outfile = open('Buffer_Player2.pickle','wb')
	pickle.dump(a,outfile)
	outfile.close()

	#infile = open(filename,'rb')
	#d = pickle.load(infile)
	#infile.close()

	#print(a==d)
	#print(a.buffer)
	#print(d.buffer)