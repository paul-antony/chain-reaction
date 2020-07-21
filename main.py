from flask import Flask, request, jsonify, render_template
import json

from agent.board import *
from agent.alpha_beta import *
import time

board = Board()

app = Flask(__name__)
app.config["DEBUG"] = False

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/postmethod', methods=['POST'])
def main():
	game_mode = int(request.form['mode'])
	agent_turn = int(request.form['player'])
	cur_board = json.loads(request.form['board'], encoding="utf-8")

	board.input(cur_board,agent_turn)

	if game_mode == 2:
		return json.dumps(list(alpha_beta(board,4)))



app.run()
