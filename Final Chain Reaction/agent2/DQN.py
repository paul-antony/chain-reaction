import keras
import numpy as np
import random

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam

import tensorflow as tf


input_dim = 54
output_dim = 54

epsilon = 1.0
epsilon_min = 0.10
epsilon_decay = 0.93 #we want to decrease the number of explorations as it gets good at playing games.
lr = 0.001


class QNetwork:
	def __init__(self):

		self.input_dim = input_dim
		self.output_dim = output_dim		
		self.epsilon = epsilon
		self.epsilon_min = epsilon_min
		self.epsilon_decay = epsilon_decay
		self.lr = lr


		self.filename_player1 = "player1.h5"
		self.filename_player2 = "player2.h5"
		self.model = self.build_model()
		self.graph = []
		self.graph.append(tf.get_default_graph())
	
	def build_model(self):

		model = Sequential()
		
		model.add(Dense(60, input_dim = self.input_dim,activation = "relu")) 
		
		model.add(Dense(60, activation = "relu")) 
		model.add(Dense(60, activation = "relu"))
		model.add(Dense(60, activation = "relu"))
		
		model.add(Dense(self.output_dim, activation = "linear")) # output layer
		
		model.compile(loss="mse",optimizer = Adam(lr=self.lr))
		
		#model.summary()
		
		return model

	
	def load(self,player,file_name=[]):

		if file_name == []:

			if player == 1:
				file_name = self.filename_player1
			else:
				file_name = self.filename_player2
		print('111111111111111111111111111111111111111')
			
		self.model.load_weights(file_name)
		print("2222222222222222222222222222222222222")

	def save(self,player,file_name=[]):

		if file_name == []:
			
			if player == 1:
				file_name = self.filename_player1
			else:
				file_name = self.filename_player2
			
		self.model.save_weights(file_name)



	def action_training(self,board):

		if np.random.rand() <= self.epsilon:
			action = random.randrange(self.output_dim)
			return self.act_convert(action)

		else:
			return self.act(board,0)



	def qvalue(self, input,player):

		self.load(player)	
		action_reward = self.model.predict(np.array([input]))[0]
		return action_reward.tolist()

	@staticmethod
	def act_convert(action):
		return (int(action/6),action%6)
	

	def act(self,board,file_name=[],flag = 1):
		self.load(board.player,file_name)
		action_reward = self.model.predict(np.array([board.list()]))

		action = np.argmax(action_reward[0])
		if flag == 1:
			valid_moves = board.valid_move()
			if self.act_convert(action) not in valid_moves:
				
				for i in self.sort(action_reward[0].tolist(),1):
					if self.act_convert(i[1]) in valid_moves:
						action = i[1]
						break

		return self.act_convert(action)






	
	def eps_update(self):
		if self.epsilon > self.epsilon_min:
			self.epsilon = self.epsilon * self.epsilon_decay

	
	def train(self,x,y):
		self.model.fit(np.array(x), np.array(y), epochs=1, verbose=0)


	@staticmethod
	def sort(input,rev):
		output = []
		for i in range(0,len(input)):
			output.append([input[i],i])
		if rev == -1:
			output.sort(key = lambda x: x[0],reverse = False)
		else:
			output.sort(key = lambda x: x[0],reverse = True)
		return output



if __name__ == "__main__":
	#print(QNetwork.sort([10,3,-200,6,3.14,-3.323],1))

	a=QNetwork()
	a.save(1)
	a.save(-1)
