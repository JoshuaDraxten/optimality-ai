import os
from optimality_ai import Optimality


def flip_game(game):
    """
        Flip the game 
    """
    flipped_game = []
    for move in game["moves"]:
        flipped_game.append([space*-1 for space in move])
    return flipped_game


def game_won(board):
    """
        If a player has one, this returns that player's mark (-1 or 1).
        Otherwise this function returns 0
    """
    possible_rows = [
        board[0:3], board[3:6], board[6:9],    # Horizontal
        board[::3], board[1::3], board[2::3],  # Vertical
        board[::4], board[2::2][0:3]           # Diagonal
    ]
    for row in possible_rows:
        if min(row) == max(row):
            return row[0]
    return 0


def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    x_and_o = [["X", "-", "O"][space+1] for space in board]
    print()
    print(' '.join(x_and_o[0:3]))
    print(' '.join(x_and_o[3:6]))
    print(' '.join(x_and_o[6:9]))
    print()


def generate_move_candidates(board):
    candidate_boards = []
    zero_indexes = [i for i, x in enumerate(board) if x == 0]
    for move in zero_indexes:
        candidate_board = board.copy()
        candidate_board[move] = 1
        candidate_boards.append(candidate_board)
    return candidate_boards


def play_game(get_next_move):
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    moves = []
    turn = 1

    while not game_won(board) and 0 in board:
        if (turn == 1):
            moves.append(get_next_move(board))
            turn = -1
        else:
            move = input("(x,y)> ")
            if "," not in move or len(move) != 3:
                continue
            x, y = move.split(',')
            move_index = int(x)-1+(3*(int(y)-1))
            # If that space is available, put the X there
            if board[move_index] == 0:
                board[move_index] = -1
                moves.append(board)
                turn = 1
        board = moves[-1]
        print_board(moves[-1])

    winner = game_won(board)

    # Let the user know what happened
    if winner == 1:
        input("You lose")
    elif game_won(board) == -1:
        input("You win!")
    else:
        input("Cats game")

    return {"winner": winner, "moves": moves}

##### CONSTRAINTS #####


def will_lose_game(board):
    return game_won(board) == -1


def will_win_game(board):
    return game_won(board) == 1


def avoided_losses(board):
    """
        The more losses we're avoiding the better
    """
    rows = [
        board[0:3], board[3:6], board[6:9],    # Horizontal
        board[::3], board[1::3], board[2::3],  # Vertical
        board[::4], board[2::2][0:3]           # Diagonal
    ]
    possible_wins = [
        row for row in rows if row.count(-1) == 2 and 1 in row]
    return len(possible_wins)


def possible_win(board):
    rows = [
        board[0:3], board[3:6], board[6:9],    # Horizontal
        board[::3], board[1::3], board[2::3],  # Vertical
        board[::4], board[2::2][0:3]           # Diagonal
    ]
    possible_wins = [row for row in rows if row.count(
        1) == 2 and -1 not in row]
    return len(possible_wins)

##### GAME LOOP #####


tic_tac_toe = Optimality(
    play_game, generate_move_candidates, flip_game, verbose=False)
tic_tac_toe.set_constraints(
    [possible_win, will_lose_game, will_win_game, avoided_losses])
tic_tac_toe.train()
