from __future__ import print_function
import sys
from flask import Flask, request, jsonify, render_template
import json

from agent1.alpha_beta import *
from agent1.board import *
from agent2.DQN import *
board = Board()

network = QNetwork()
app = Flask(__name__)
app.config["DEBUG"] = True




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/postmethod', methods=['POST'])
def main():
	game_mode = int(request.form['mode'])
	agent_turn = int(request.form['player'])
	cur_board = json.loads(request.form['board'], encoding="utf-8")
	print(game_mode, file=sys.stderr)
	print(agent_turn, file=sys.stderr)
	print(cur_board, file=sys.stderr)

	board.input(cur_board,agent_turn)

	if game_mode == 2:
		return json.dumps(list(alpha_beta(board,4)))
	
	elif game_mode == 3:
		#network = QNetwork()
		#network.model._make_predict_function()
		if board.player == 1:
			file_name = 'agent2/player1.h5'
		else:
			file_name = 'agent2/player2.h5'
		with network.graph[0].as_default():
			action = network.act(board,file_name = file_name)
			action=[int(action[0]),int(action[1])]


		return json.dumps(action)


	elif game_mode == 4:
		agent1_turn = request.form['agent1']
		print(agent1_turn, file=sys.stderr)
		if (int(agent1_turn)==1 and int(agent_turn==1)) or (int(agent1_turn)==-1 and int(agent_turn)==-1):
			return json.dumps(list(alpha_beta(board,4)))
		elif (int(agent1_turn)==1 and int(agent_turn)==-1) or (int(agent1_turn)==-1 and int(agent_turn)==1):
			return json.dumps(list(alpha_beta(board,4)))

app.run()
