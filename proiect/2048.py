import random
import tkinter as tk

def initialize_board():
    board = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(0)
        board.append(row)
    add_number(board)
    add_number(board)
    return board

def add_number(board):
    empty_positions = find_empty_positions(board)
    if empty_positions:
        position = random.choice(empty_positions)
        value = 2 if random.random() < 0.5 else 4
        board[position[0]][position[1]] = value

def find_empty_positions(board):
    empty_positions = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty_positions.append((i, j))
    return empty_positions

def print_board(board):
    for row in board:
        for number in row:
            print(number, end="\t")
        print()

def move_up(board):
    for column in range(4):
        column_values = [board[i][column] for i in range(4) if board[i][column] != 0]
        column_values = combine_numbers(column_values)
        column_values += [0] * (4 - len(column_values))

        for i in range(4):
            board[i][column] = column_values[i]

def move_down(board):
    for column in range(4):
        column_values = [board[i][column] for i in range(3, -1, -1) if board[i][column] != 0]
        column_values = combine_numbers(column_values)
        column_values = [0] * (4 - len(column_values)) + column_values[::-1]

        for i in range(4):
            board[i][column] = column_values[i]

def move_left(board):
    for row in range(4):
        row_values = [number for number in board[row] if number != 0]
        row_values = combine_numbers(row_values)
        row_values += [0] * (4 - len(row_values))

        for i in range(4):
            board[row][i] = row_values[i]

def move_right(board):
    for row in range(4):
        row_values = [number for number in board[row][::-1] if number != 0]
        row_values = combine_numbers(row_values)
        row_values = [0] * (4 - len(row_values)) + row_values[::-1]

        for i in range(4):
            board[row][i] = row_values[i]

def combine_numbers(list_to_combine):
    for i in range(len(list_to_combine) - 1):
        if list_to_combine[i] == list_to_combine[i + 1]:
            list_to_combine[i] *= 2
            list_to_combine[i + 1] = 0
    list_to_combine = [number for number in list_to_combine if number != 0]
    list_to_combine += [0] * (4 - len(list_to_combine))
    return list_to_combine

def update_interface():
    for i in range(4):
        for j in range(4):
            cell_value = board[i][j]
            cell_label = board_labels[i][j]
            cell_label.config(text=str(cell_value) if cell_value != 0 else "", bg=color_background(cell_value))

def color_background(value):
    #https://www.plus2net.com/python/tkinter-colors.php  colors were chosen from this site.
    colors = {
        0: "#FAEBD7",
        2: "#DFFF00",
        4: "#00FFFF",
        8: "#66CDAA",
        16: "#E3CF57",
        32: "#0000FF",
        64: "#A52A2A",
        128: "#FF6103",
        256: "#FFF8DC",
        512: "#DC143C",
        1024: "#BF3EFF",
        2048: "#8B6914"
    }
    return colors[value]

def on_key(event):
    direction = ""
    if event.keysym in ['Up', 'w']:
        direction = 'w'
    elif event.keysym in ['Down', 's']:
        direction = 's'
    elif event.keysym in ['Left', 'a']:
        direction = 'a'
    elif event.keysym in ['Right', 'd']:
        direction = 'd'

    if direction:
        if direction == 'w':
            move_up(board)
        elif direction == 's':
            move_down(board)
        elif direction == 'a':
            move_left(board)
        elif direction == 'd':
            move_right(board)

        add_number(board)
        update_interface()


root = tk.Tk()
root.title("2048 Game By Gelu Galan")


board = initialize_board()
board_labels = [[None]*4 for _ in range(4)]


for i in range(4):
    for j in range(4):
        cell_label = tk.Label(root, text="", width=5, height=2)
        cell_label.grid(row=i, column=j, padx=5, pady=5)
        board_labels[i][j] = cell_label

update_interface()
root.bind("<Key>", on_key)
root.mainloop()
