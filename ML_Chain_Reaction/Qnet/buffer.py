#game replay buffer and pre process of training data

# buffer type (board(list), action(1d index), board_q(list), player(int),invalid_list(list of 1d_index of invalid move), reward(int))
import random
alpha = 0.09
gama = 0.99

class replay_byffer:

	def __init__(self,alpha,gama):
		self.buffer = []
		self.alpha = alpha
		self.gama = gama 

	def reset(self):
		self.buffer = []

	
	def push(self,item):
		self.buffer.append(item)



	#Generates training data
	def generate_data(self):

		pre = self.pre_process()#pre process data and returns input and output of data
		multiply = self.mirror(pre,9,6)#incress the no of entries by adding mirror layouts

		data = self.random_selector(multiply)#selects random elements from list 

		return self.x_y_split(data)



	#process the buffer
	def pre_process(self):
		x = []
		y = []
		for entry in self.buffer[::-1]:
			x.append(entry[0])
			output = entry[2]
			
			if entry[5] in (100,-100):
				output[entry[1]] = entry[5]

			else:
				if entry[3] == -1:
					new = output[entry[1]] +self.alpha*(entry[5] + self.gama*(max(y[-1][1])) - output[entry[1]])
				else:
					new = output[entry[1]] +self.alpha*(entry[5] + self.gama*(min(y[-1][1])) - output[entry[1]])
				output[entry[1]] = new

			output = self.illegal_preprocess(output,entry[4],entry[3])
			
			x.append(output)
			y.append(x)
			x=[]

		return y


	@staticmethod
	def illegal_preprocess(input,index,player):
		
		for i in index:
			input[i] = player * -1 * 200

		return input

	#converts list of 2d index'es to list of 1d index'es
	@staticmethod
	def index21(input):
		output=[]
		for i in input:
			output.append(a[0]*6 + a[1])
		return output


	

	
	#adds mirror states to board
	@staticmethod
	def mirror(x,m,n):
		output = []
		for entry in x:
			
			output.append(entry)
			a = (replay_byffer.convert_to_2d(entry[0], m, n), replay_byffer.convert_to_2d(entry[1], m, n))
			b = (replay_byffer.flip_horizontal(a[0]),replay_byffer.flip_horizontal(a[1]))
			c = (replay_byffer.flip_vertical(a[0]),replay_byffer.flip_vertical(a[1]))
			d = (replay_byffer.flip_horizontal(c[0]),replay_byffer.flip_horizontal(c[1]))
			output.append([replay_byffer.convert_to_1d(b[0]),replay_byffer.convert_to_1d(b[1])])
			output.append([replay_byffer.convert_to_1d(c[0]),replay_byffer.convert_to_1d(c[1])])
			output.append([replay_byffer.convert_to_1d(d[0]),replay_byffer.convert_to_1d(d[1])])
		
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


	#converts 1d list to 2d
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


	#removes duplicate entries
	@staticmethod
	def remove_duplicate(input): 
    		output = [] 
    		for entry in input: 
        		if entry not in output: 
            			output.append(entry) 

    		return output 
	#selects 
	@staticmethod
	def random_selector(input):
		random.shuffle(input)
		return input[::2]


	#converts 2d index to id index
	@staticmethod
	def index_1d(input):
		output = input[0]*6 + input[1]
		return output



	#splits data into two list
	@staticmethod
	def x_y_split(input):
		x = []
		y = []
		for i in input:
			x.append(i[0])
			y.append(i[1])

		return (x,y)



	#converts list of 2d index to id index
	@staticmethod
	def index_list_converter(input):
		output = []
		for i in input:
			output.append(replay_byffer.index_1d(i))

		return output



if __name__ == "__main__":
	print(replay_byffer.index_list_converter([[1,1],[2,2],[3,4]],1))
