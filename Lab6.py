"""
Name:Emmanuel Okezie
Section:2
"""

def drawBoard(board):
    for row in board:
        for space in row:
            if space == 0:
                print(".", end=" ")
            else:
                print(space, end=" ")
        print()
    print("0 1 2 3 4 5 6")  # column numbers


def switchPlayer(player):
    if player == "O":
        return "X"
    else:
        return "O"


def dropPiece(board, player, column):
    # Check if column is full
    if board[0][column] != 0:
        return False

    # Start from bottom row
    for row in range(len(board) - 1, -1, -1):
        if board[row][column] == 0:
            board[row][column] = player
            return True

    return False


def checkWinner(board, player):
    ROWS = len(board)
    COLS = len(board[0])

    # Horizontal check
    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] == player:
                return True

    # Vertical check
    for r in range(ROWS - 3):
        for c in range(COLS):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] == player:
                return True

    # Diagonal (down-right)
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] == player:
                return True

    # Diagonal (up-right)
    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] == player:
                return True

    return False


def main():
    ROWS = 6
    COLUMNS = 7
    BOARD = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

    CURRENT_PLAYER = "X"

    while True:
        drawBoard(BOARD)
        print(f"Player {CURRENT_PLAYER}'s turn")

        try:
            col = int(input("Enter column (0-6): "))
            if col < 0 or col >= COLUMNS:
                print("Invalid column. Try again.")
                continue
        except:
            print("Please enter a number.")
            continue

        if not dropPiece(BOARD, CURRENT_PLAYER, col):
            print("Column full! Try another one.")
            continue

        if checkWinner(BOARD, CURRENT_PLAYER):
            drawBoard(BOARD)
            print(f" Player {CURRENT_PLAYER} wins!")
            break

        CURRENT_PLAYER = switchPlayer(CURRENT_PLAYER)


if __name__ == "__main__":
    main()