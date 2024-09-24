# Function to print the Tic Tac Toe board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check for a win or a tie
def check_win(board, player):
    # Define winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    
    # Check if any winning combination is satisfied
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check if the board is full (tie)
def check_tie(board):
    return all(space != " " for space in board)

# Function to handle player moves
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("This spot is already taken. Try again.")
        except (IndexError, ValueError):
            print("Invalid move. Please enter a number between 1 and 9.")

# Main function to run the game
def play_game():
    # Initialize the board
    board = [" "] * 9
    current_player = "X"
    
    while True:
        print_board(board)
        player_move(board, current_player)
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Ask if players want to play again
if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
