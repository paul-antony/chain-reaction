import pygame
from alpha_beta import *
from board import Board
import _thread as thread

m, n = 9, 6

pygame.init()
surface = pygame.display.set_mode((50*n, 50*m))
pygame.display.set_caption('Chain Reaction')
lock = thread.allocate_lock()

def drawBoard(board_ui):
	surface.fill((0,0,0))
	font = pygame.font.Font('Font.ttf', 48)
	for pos in [(x,y) for x in range(board_ui.m) for y in range(board_ui.n)]:
		if abs(board_ui.board[pos[0]][pos[1]]) >= board_ui.critical_mass(pos):
			color = (255,255,0)
		elif board_ui.board[pos[0]][pos[1]]/board_ui.player > 0:
			color = (90,90,90)
		elif board_ui.board[pos[0]][pos[1]]/board_ui.player < 0:
			color = (255,0,0)
		else:
			color = (0,255,0)
		text = font.render(str(board_ui.board[pos[0]][pos[1]])[-1], 1, color)
		textpos = text.get_rect(centerx = pos[1]*50 + 25, centery = pos[0]*50 + 25)
		surface.blit(text, textpos)
	pygame.display.update()

def slowMove(board_ui, pos):
	while True:
		drawBoard(board_ui)
		pygame.time.wait(250)
		unstable = []
		for pos in [(x,y) for x in range(board_ui.m) for y in range(board_ui.n)]:
			if abs(board_ui.board[pos[0]][pos[1]]) >= board_ui.critical_mass(pos):
				unstable.append(pos)
		#raw_input()
		if not unstable:
			break
		for pos in unstable:
			board_ui.board[pos] -= board_ui.board.player*board_ui.board.critical_mass(pos)
			for i in board.neighbors(pos):
				board_ui.board[i] = board_ui.board[pos[0]][pos[1]]/board_ui.board.player*(abs(board_ui.board[i])+1)
	drawBoard(board_ui)
	lock.release()

def show_move(pos):
	rect = pygame.Rect(pos[1]*50,pos[0]*50,50,50)
	pygame.draw.rect(surface,(255,255,0),rect,0)
	pygame.display.update()
	pygame.time.wait(250)


def main():
	global m,n, surface

	#start screen
	font = pygame.font.Font('Font.ttf', 72)
	text = font.render("Red", 1, (255,0,0))
	textpos = text.get_rect(centerx = 25*n, centery = 12*m)
	surface.blit(text, textpos)
	text = font.render("Green", 1, (0,255,0))
	textpos = text.get_rect(centerx = 25*n, centery = 36*m)
	surface.blit(text, textpos)
	font = pygame.font.Font('Font.ttf', 12)
	text = font.render("Choose a Color", 1, (100,100,100))
	textpos = text.get_rect(centerx = 25*n, centery = 25*m)
	surface.blit(text, textpos)
	pygame.display.update()

	this_loop = True
	while this_loop:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				y = pygame.mouse.get_pos()[1]
				if y < 25*m:
					player_first = True
				else:
					player_first = False
				this_loop = False



	#some initialization code
	m, n = 9, 6
	surface = pygame.display.set_mode((50*n, 50*m))
	pygame.display.set_caption('Chain Reaction')
	board_ui = Board(m=m,n=n)
	total_moves = 0

	#game screen
	drawBoard(board_ui)

	if not player_first:
		new_move = alpha_beta(board_ui,2)
		lock.acquire()
		thread.start_new_thread(slowMove, (board_ui, new_move))
		board_ui = board_ui.move(new_move)
		total_moves += 1

	this_loop = True
	while this_loop:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y = pygame.mouse.get_pos()
				pos = (int(y/50), int(x/50))
				print(pos)
				#if not (board_ui.player == board_ui.board[pos[0]][pos[1]]/board_ui.player or 0 == board_ui.board[pos[0]][pos[1]]/board_ui.player):
				print("player = " ,board_ui.player)
				if board_ui.board[pos[0]][pos[1]]/board_ui.player < 0:
					print("Illegal Move!")
					continue
				show_move(pos)
				lock.acquire()
				thread.start_new_thread(slowMove, (board_ui, pos, ))
				board_move = board_ui.move(pos)
				total_moves += 1
				if total_moves >= 2:
					if board_ui.cal_heuristics() == 200:
						winner = board_ui.player*(-1)
						this_loop = False
						break
				new_move = alpha_beta(board_ui, 2)
				print("new_move ", new_move)
				print(new_move)
				show_move(new_move)
				lock.acquire()
				thread.start_new_thread(slowMove, (board_ui, new_move, ))
				board = board_ui.move(new_move)
				total_moves += 1
				if total_moves >= 2:
					if board_ui.cal_heuristics() == 200:
						winner = board_ui.player*(-1)
						this_loop = False
						break

	#winning screen
	while lock.locked():
		continue
	m, n = 9, 6
	surface = pygame.display.set_mode((50*n, 50*m))
	font = pygame.font.Font('Font.ttf', 72)
	pygame.display.set_caption('Chain Reaction')
	if winner == 1:
		text = font.render("Red", 1, (255,0,0))
	else:
		text = font.render("Green", 1, (0,255,0))
	textpos = text.get_rect(centerx = 25*n, centery = 12*m)
	surface.blit(text, textpos)
	font = pygame.font.Font('Font.ttf', 48)
	text = font.render("Wins!", 1, (100,100,100))
	textpos = text.get_rect(centerx = 25*n, centery = 25*m)
	surface.blit(text, textpos)
	pygame.display.update()


if __name__ == "__main__":
	main()
