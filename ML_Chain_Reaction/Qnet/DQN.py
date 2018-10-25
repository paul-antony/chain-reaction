import keras
import numpy as np
import random

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import Adam
from collections import deque



input_dim = 54
output_dim = 54

epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995 #we want to decrease the number of explorations as it gets good at playing games.
lr = 0.001

class QNetwork:
	def __init__(self, input_dim, output_dim, lr, epsilon, epsilon_min, epsilon_decay):

		self.input_dim = input_dim
		self.output_dim = output_dim		
		self.epsilon = epsilon
		self.epsilon_min = epsilon_min
		self.epsilon_decay = epsilon_decay
		self.lr = lr
		self.model = self.build_model()
	
	def build_model(self):

		model = Sequential()
		
		model.add(Dense(60, input_dim = self.input_dim,activation = "relu")) 
		
		model.add(Dense(60, activation = "relu")) 
		
		model.add(Dense(self.output_dim, activation = "linear")) # output layer
		
		model.compile(loss="mse",optimizer = Adam(lr=self.lr))
		
		#model.summary()
		
		return model

	
	def load(self, name):

        	self.model.load_weights(name)

	def save(self, name):

        	self.model.save_weights(name)

	def action_training(self,board):

		action_reward = self.model.predict(np.array([board.list()]))

		if np.random.rand() <= self.epsilon:
			action = random.randrange(self.output_dim)

		else:
			if board.player == 1:
				action = np.argmax(action_reward[0])

			else:
				action = np.argmin(action_reward[0])

			valid_moves = board.valid_move()
			if self.act_convert(action) not in valid_moves:
				return valid_moves[random.randrange(len(valid_moves))], action_reward[0].tolist()
		
		return self.act_convert(action), action_reward[0].tolist()



	def qvalue(self, board):
		action_reward = self.model.predict(np.array([board.list()]))[0]
		return action_reward.tolist()

	@staticmethod
	def act_convert(action):
		return (int(action/6),action%6)
	

	def act(self,board):
		action_reward = self.model.predict(np.array([board.list()]))
		if board.player == 1:
			action = np.argmax(action_reward[0])

		else:
			action = np.argmin(action_reward[0])

		valid_moves = board.valid_move()
		if self.act_convert(action) not in valid_moves:
			return valid_moves[random.randrange(len(valid_moves))]

		return self.act_convert(action)

	
	def eps_update(self):
		if self.epsilon > self.epsilon_min:
			self.epsilon = self.epsilon * self.epsilon_decay

	
	def train(self,x,y):
		self.model.fit(np.array(x), np.array(y), epochs=2, verbose=0)

