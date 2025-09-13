# tic_tac_toe.py
import math

player, ai = 'X', 'O'

def print_board(board):
    for row in board:
        print("|".join(row))
    print()

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def minimax(board, depth, is_max):
    winner = check_winner(board)
    if winner == ai: return 1
    if winner == player: return -1
    if all(cell != ' ' for row in board for cell in row): return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = ai
                    best = max(best, minimax(board, depth+1, False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    best = min(best, minimax(board, depth+1, True))
                    board[i][j] = ' '
        return best

def best_move(board):
    move = (-1, -1)
    best_val = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = ai
                move_val = minimax(board, 0, False)
                board[i][j] = ' '
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

def play_game():
    board = [[' ']*3 for _ in range(3)]
    print_board(board)
    while True:
        x, y = map(int, input("Enter row and col (0-2): ").split())
        if board[x][y] == ' ':
            board[x][y] = player
        else:
            print("Invalid move!")
            continue

        if check_winner(board): break
        if all(cell != ' ' for row in board for cell in row): break

        move = best_move(board)
        board[move[0]][move[1]] = ai
        print_board(board)

        if check_winner(board): break
    print("Winner:", check_winner(board) or "Draw")

if __name__ == "__main__":
    play_game()