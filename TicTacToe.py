#
# ALA Tic-Tac-Toe
# Name: Irving Reyes Bravo
# Date: 11/27/2023
#


# define function
def displayBoard(board):
  for row in board:
      print(" | ".join(row))
      print("-" * 9)


def findWinner(board):
  # Check rows and columns
  for i in range(3):
      if board[i][0] == board[i][1] == board[i][2] != ' 'or board[0][i] == board[1][i] == board[2][i] != ' ':
          return True

  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
      return True

  return False


def isBoardFull(board):
  for row in board:
      if ' ' in row:
          return False
  return True


def playTicTacToe():
  # Initialize the board
  board = [[' ' for _ in range(3)] for _ in range(3)]

  # Define players
  allPlayers = ['X', 'O']
  currentPlayer = allPlayers[0]

  # Game loop
  while True:
      displayBoard(board)

      # Player move
      while True:
          try:
              row = int(input(f"Player {currentPlayer}, enter row (0-2): "))
              col = int(input(f"Player {currentPlayer}, enter column (0-2): "))
              if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                  break
              else:
                  print("Whoops! Spot taken. Try again.")
          except ValueError:
              print("Invalid input. Enter a number (0-2).")

      # Update the board
      board[row][col] = currentPlayer

      # Check for a winner
      if findWinner(board):
          displayBoard(board)
          print(f"Player {currentPlayer} wins!")
          break

      # Check for a draw
      if isBoardFull(board):
          displayBoard(board)
          print("It's a draw!")
          break

      # Switch to the other player
      currentPlayer = allPlayers[1] if currentPlayer == allPlayers[0] else allPlayers[0]

if __name__ == "__main__":
  playTicTacToe()
