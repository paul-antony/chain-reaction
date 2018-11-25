import pygame
from Qnet.DQN import *
from Qnet.board import Board


m, n = 9, 6

pygame.init()
surface = pygame.display.set_mode((50*n, 50*m))
pygame.display.set_caption('Chain Reaction')


def drawBoard(board_ui):
	surface.fill((0,0,0))
	font = pygame.font.Font('Font.ttf', 48)
	for pos in [(x,y) for x in range(board_ui.m) for y in range(board_ui.n)]:
		if board_ui[pos] < 0:
			color = (0,255,0)
		elif board_ui[pos] > 0:
			color = (255,0,0)
		else:
			color = (90,90,90)
		text = font.render(str(board_ui[pos])[-1], 1, color)
		textpos = text.get_rect(centerx = pos[1]*50 + 25, centery = pos[0]*50 + 25)
		surface.blit(text, textpos)
	pygame.display.update()
	pygame.time.wait(250)



def show_move(pos):
	rect = pygame.Rect(pos[1]*50,pos[0]*50,50,50)
	pygame.draw.rect(surface,(255,255,0),rect,0)
	pygame.display.update()
	pygame.time.wait(250)
	


def main():
	global m,n, surface

	network = QNetwork()
	m,n = 9,6
	surface = pygame.display.set_mode((50*n, 50*m))
	pygame.display.set_caption('Chain Reaction')
	board_ui = Board()
	total_moves = 0
	drawBoard(board_ui)

    
	game_loop = True
	while game_loop:
		pygame.event.clear()
		player_loop = True
		while player_loop:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					x,y = pygame.mouse.get_pos()
					pos = (int(y/50), int(x/50))
					show_move(pos)
					if board_ui[pos]/board_ui.player < 0:
						drawBoard(board_ui)
						continue
					player_loop = False
		board_ui.move(pos)
		drawBoard(board_ui)
		total_moves += 1
		if total_moves >= 2:
			if board_ui.cal_heuristics() == -200:
				winner = board_ui.player*(-1)
				game_loop = False
				break


		new_move = network.act(board_ui,file_name='Qnet/player2.h5')
		show_move(new_move)
		board_ui.move(new_move)
		drawBoard(board_ui)
		total_moves += 1
		if total_moves >= 2:
			if board_ui.cal_heuristics() == -200:
				winner = board_ui.player*(-1)
				game_loop = False
				break
	#winning screen

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
	pygame.time.wait(2000)

if __name__ == "__main__":
	main()
