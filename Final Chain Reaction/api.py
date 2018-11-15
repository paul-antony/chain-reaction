from __future__ import print_function
import sys
from flask import Flask, request, jsonify, render_template
from agent1.alpha_beta import *
import json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postmethod', methods=['POST'])
def main():
    game_mode = request.form['mode']
    agent_turn = request.form['player']
    cur_board = json.loads(request.form['board'], encoding="utf-8")
    print(game_mode, file=sys.stderr)
    print(agent_turn, file=sys.stderr)
    print(cur_board, file=sys.stderr)
    if int(game_mode) == 2:
        return json.dumps(list(alpha_beta(cur_board, int(agent_turn))))
    elif int(game_mode) == 3:
        return json.dumps(list(alpha_beta(cur_board, int(agent_turn))))
    elif int(game_mode) == 4:
        agent1_turn = request.form['agent1']
        print(agent1_turn, file=sys.stderr)
        if (int(agent1_turn)==1 and int(agent_turn==1)) or (int(agent1_turn)==-1 and int(agent_turn)==-1):
            return json.dumps(list(alpha_beta(cur_board, int(agent_turn))))
        elif (int(agent1_turn)==1 and int(agent_turn)==-1) or (int(agent1_turn)==-1 and int(agent_turn)==1):
            return json.dumps(list(alpha_beta(cur_board, int(agent_turn))))

app.run()
