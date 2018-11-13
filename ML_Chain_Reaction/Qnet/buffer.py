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
		mirror_boards = self.mirror(item)
		self.index_convert(mirror_boards)

		if self.max_size - self.size < len(mirror_boards):
			self.pop(len(mirror_boards))
		
		for entry in mirror_boards:
			self.buffer.append(entry)
		
		self.size += len(mirror_boards)


	def pop(self,count):
		for i in range(0,count):
			self.buffer.pop(0)
			self.size -= 1

	def minibatch(self,size):
		
		output = random.sample(self.buffer,size)
		return copy.deepcopy(output)
#################################################################################################################



	def train(self,size):
		if size < self.size:
			batch = self.minibatch(size)

			train_network.load()

			batch = self.update_q(batch)
			batch = replay_buffer.illegal_move(batch)
			x,y = replay_buffer.x_y_split(batch)
			train_network.train(x,y)
			train_network.save()



	def update_q(self,input):
		output = []

		train_network.load()

		for entry in input:
			temp = []
			temp.append(entry[0])#board state

			present_state = entry[0][:]
			
			present_state.append(entry[1])
			print(len(present_state),present_state)
			temp.append(train_network.qvalue(present_state))#q value

			if entry[4] in (1,-1):
				temp[1][entry[2]] = entry[4]#update q value
			else:	

				next_state = entry[3]

				next_state.append(entry[1]*-1)

				if entry[1] == 1:
					max_q = min(train_network.qvalue(next_state))
				else:
					max_q = max(train_network.qvalue(next_state))

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
				temp[1][i] = -1 * entry[2]

			temp[0].append(entry[2])#addind player to input			
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

#####################################################################################################################

	@staticmethod
	def mirror(input,m=9,n=6):
		
		output = []

		output.append(input)
			
		a = (replay_buffer.convert_to_2d(input[0], m, n), replay_buffer.convert_to_2d(input[3], m, n))
		b = (replay_buffer.flip_horizontal(a[0]),replay_buffer.flip_horizontal(a[1]))
		c = (replay_buffer.flip_vertical(a[0]),replay_buffer.flip_vertical(a[1]))
		d = (replay_buffer.flip_horizontal(c[0]),replay_buffer.flip_horizontal(c[1]))



		output.append([replay_buffer.convert_to_1d(b[0]), input[1], (input[2][0],n - input[2][1] - 1), replay_buffer.convert_to_1d(b[1]),input[4]])
		output.append([replay_buffer.convert_to_1d(c[0]), input[1], (m - input[2][0]-1,input[2][1]),replay_buffer.convert_to_1d(c[1]),input[4]])
		output.append([replay_buffer.convert_to_1d(d[0]), input[1], (m - input[2][0] - 1, n - input[2][1] - 1),replay_buffer.convert_to_1d(d[1]),input[4]])
		
		return output

	@staticmethod
	def index_convert(input,m = 9, n = 6):
		for entry in input:
			entry[2] = replay_buffer.index_1d(entry[2],m,n)

	#converts 2d index to id index
	@staticmethod
	def index_1d(input,m = 9, n = 6):
		output = input[0]*n + input[1]
		return output


	#flips 2d matrix vertical
	@staticmethod
	def flip_vertical(input):
		output = []
		for i in input[::-1]:
			output.append(i)
		
		return output



	#flips 2d matrix horizontal
	@staticmethod
	def flip_horizontal(input):
		output = []
		
		for i in input:
			temp = []
			for j in i[::-1]:
				temp.append(j)
			output.append(temp)
		return output



	@staticmethod
	def convert_to_2d(input,m,n):
		output = []
		index = 0

		for i in range(0,m):
			temp = []
			for j in range(0,n):
				temp.append(input[index])
				index = index + 1
			output.append(temp)
		return output




	#converts 2d list to 1d
	@staticmethod
	def convert_to_1d(input):
		output = []

		for i in input:
			for j in i:
				output.append(j)
		
		return output





if __name__ == "__main__":
	a = replay_buffer()
	#b = [1,2,3,4,5,6]
	#c = ['a','b','c','d','e','f']
	#a.push([b,1,(1,1),c,-1,0.9])

	filename = 'BUFFER.pickle'
	outfile = open(filename,'wb')
	pickle.dump(a,outfile)
	outfile.close()

	#infile = open(filename,'rb')
	#d = pickle.load(infile)
	#infile.close()

	#print(a==d)
	#print(a.buffer)
	#print(d.buffer)
