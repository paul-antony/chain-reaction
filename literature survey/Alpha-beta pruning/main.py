from numerical_tic_tac_toe import Board
from numerical_tic_tac_toe import Player


def main():
    human_vs_ai = prompt_user_for_game_type()

    if human_vs_ai:
        human_player_first = prompt_user_for_play_order()
        players = create_players(human_player_first)
    else:
        players = [Player(is_human=0, is_max=1), Player(is_human=0, is_max=0)]

    max_, min_ = get_max_and_min(players)
    board = Board(4)

    print(board)

    while True:
        max_move = max_.get_move(board)
        board = max_.perform_move(*max_move, board)
        print(board)
        if board.has_winning_sum:
            print('Max wins!')
            break
        if len(list(board.all_possible_moves)) == 0:
            print('Draw!')
            break
        if not human_vs_ai:
            input('Press enter to continue...')

        min_move = min_.get_move(board)
        board = min_.perform_move(*min_move, board)
        print(board)
        if board.has_winning_sum:
            print('Min wins!')
            break
        if len(list(board.all_possible_moves)) == 0:
            print('Draw!')
            break
        if not human_vs_ai:
            input('Press enter to continue...')


def prompt_user_for_game_type():
    human_vs_ai = -1

    while human_vs_ai < 0:
        human_vs_ai = input('Would you like to play against an AI [Y/n]?:').lower()
        if human_vs_ai == '' or human_vs_ai == 'y':
            human_vs_ai = 1
        elif human_vs_ai == 'n':
            human_vs_ai = 0

    return human_vs_ai


def prompt_user_for_play_order():
    human_player_first = -1

    while human_player_first < 0:
        human_player_first = input('Would you like to go first [Y/n]?:').lower()
        if human_player_first == '' or human_player_first == 'y':
            human_player_first = 1
        elif human_player_first == 'n':
            human_player_first = 0

    return human_player_first


def create_players(human_player_first):
    if human_player_first == 1:
        human_player = Player(is_human=1, is_max=1)
        ai_player = Player(is_human=0, is_max=0)
    else:
        human_player = Player(is_human=1, is_max=0)
        ai_player = Player(is_human=0, is_max=1)

    return [human_player, ai_player]


def get_max_and_min(players):
    max_ = min_ = None
    for player in players:
        if player.is_max:
            max_ = player
        else:
            min_ = player
    return max_, min_


if __name__ == '__main__':
    main()
