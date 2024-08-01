from collections import deque

# Initialize an empty board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print(' | '.join(row))
    print()

# Check if a player has won
def check_win(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

# Generate all possible next states for a player
def generate_next_states(board, player):
    next_states = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                new_board = [row[:] for row in board]
                new_board[i][j] = player
                next_states.append((new_board, (i, j)))
    return next_states

# BFS function to find the best move for the AI player
def bfs_best_move(board, player):
    queue = deque([(board, player, 0)])  # (board, current_player, depth)
    best_move = None
    max_depth = float('-inf')

    print("BFS exploring states:")
    
    while queue:
        current_board, current_player, depth = queue.popleft()
        print(f"Depth: {depth}, Player: {current_player}")
        print_board(current_board)
        
        next_player = 'O' if current_player == 'X' else 'X'
        next_states = generate_next_states(current_board, current_player)

        for state, move in next_states:
            if check_win(state, current_player):
                print("Winning move found:")
                print_board(state)
                return move  # Winning move
            if is_full(state):
                continue
            queue.append((state, next_player, depth + 1))
            if depth > max_depth:
                max_depth = depth
                best_move = move

    return best_move

# Function to play the game
def play_game():
    board = initialize_board()
    current_player = 'X'

    while True:
        print_board(board)
        if check_win(board, 'X'):
            print("X wins!")
            break
        if check_win(board, 'O'):
            print("O wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        if current_player == 'X':
            print("Player X's turn.")
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                current_player = 'O'
            else:
                print("Invalid move. Try again.")
        else:
            print("Player O's turn (AI).")
            move = bfs_best_move(board, 'O')
            if move:
                row, col = move
                board[row][col] = 'O'
                current_player = 'X'

play_game()
