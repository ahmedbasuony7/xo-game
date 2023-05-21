import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe Simulator")

# Create the game board
board = [[" " for _ in range(3)] for _ in range(3)]

# Variable to keep track of the current player
current_player = "X"

# Function to handle button clicks
def button_click(row, col):
    global current_player

    # Ignore button click if the cell is already occupied
    if board[row][col] != " ":
        return

    # Update the board with the current player's symbol
    board[row][col] = current_player

    # Update the button text on the GUI
    buttons[row][col].config(text=current_player)

    # Check for a winning condition
    if check_winner():
        message = f"Player {current_player} wins!"
        tk.messagebox.showinfo("Game Over", message)
        window.quit()  # Close the window
        return

    # Switch to the next player
    current_player = "O" if current_player == "X" else "X"

# Function to check for a winning condition
def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

# Create the buttons
buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text=" ", width=10, height=5,
                           command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Start the GUI event loop
window.mainloop()
