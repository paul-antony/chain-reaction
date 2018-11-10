m = 9
n = 6

def critical_mass(pos):
	if pos == (0, 0) or pos == (m-1, n-1) or pos == (m-1, 0) or pos == (0, n-1):
		return 2
	elif pos[0] == 0 or pos[0] == (m-1) or pos[1] == 0 or pos[1] == (n-1):
		return 3
	else:
		return 4

def neighbors(pos):
	neighbors_list = []
	for i in [(pos[0], pos[1]+1), (pos[0], pos[1]-1), (pos[0]+1, pos[1]), (pos[0]-1, pos[1])]:
		if 0 <= i[0] < m and 0 <= i[1] < n:
			neighbors_list.append(i)
	return neighbors_list

def valid_moves(board, player):
	if cal_heuristics(board, player) in [200,-200]:
		return []
	valid = []
	for pos in [(x,y) for x in range(m) for y in range(n)]:
		if board[pos[0]][pos[1]]/player >= 0:
			valid.append(pos)
	return valid

def move(board, player, pos):
	board[pos[0]][pos[1]] += player
	unstable = []
	unstable.append(pos)
	while len(unstable) > 0:
		pos = unstable.pop(0)
		if cal_heuristics(board, player) in [200,-200]:
			break;
		if abs(board[pos[0]][pos[1]]) >= critical_mass(pos):
			board[pos[0]][pos[1]] -= player * critical_mass(pos)
			for i in neighbors(pos):
				board[i[0]][i[1]] = player * (abs(board[i[0]][i[1]]) + 1)
				unstable.append(i)
	player *= -1

def cal_heuristics(board, player):
	heuristic_value = 0
	positive_orbs, negative_orbs = 0, 0
	for pos in [(x,y) for x in range(m) for y in range(n)]:
		if board[pos[0]][pos[1]] > 0:
			positive_orbs += board[pos[0]][pos[1]]
		else:
			negative_orbs += board[pos[0]][pos[1]]
	heuristic_value = positive_orbs + negative_orbs
	if negative_orbs == 0 and positive_orbs > 1:
		heuristic_value = 200
	elif positive_orbs == 0 and negative_orbs < -1:
		heuristic_value = -200
	return heuristic_value * player
