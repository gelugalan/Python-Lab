import random
import tkinter as tk


class Game2048:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("2048 Game By Gelu Galan")
        self.player_name = ""
        self.opponent_type = ""
        self.game_size_var=""
        self.opponent_options = ["solo", "computer", "human"]
        self.game_size_options = ["2", "3", "4", "5", "6", "7", "8", "9"]
        self.create_start_screen()
        self.root.mainloop()


    def create_game_board(self):
        player_name_label = tk.Label(self.root, text="Name: {}".format(self.player_name))
        player_name_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        opponent_type_label = tk.Label(self.root, text="Opponent: {}".format(self.opponent_type))
        opponent_type_label.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

        # Etichete pentru scor și cel mai bun scor
        score_label = tk.Label(self.root, text="Score: {}".format("xxx"))
        score_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        best_score_label = tk.Label(self.root, text="Best: {}".format("9999"))
        best_score_label.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

        for i in range(int(self.game_size_var.get())):
            for j in range(int(self.game_size_var.get())):
                cell_label = tk.Label(self.root, text="", width=5, height=2)
                cell_label.grid(row=i+2, column=j, padx=5, pady=5)
                self.board_labels[i][j] = cell_label
    

    def create_start_screen(self):
        start_label = tk.Label(self.root, text=" Name:")
        start_label.grid(row=5, column=0, columnspan=4)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

        opponent_label = tk.Label(self.root, text="Select opponent:")
        opponent_label.grid(row=7, column=0, columnspan=4)

        self.opponent_var = tk.StringVar(self.root)
        self.opponent_var.set(self.opponent_options[0])


        opponent_menu = tk.OptionMenu(self.root, self.opponent_var, *self.opponent_options)
        opponent_menu.grid(row=8, column=0, columnspan=4, padx=5, pady=5)


        game_size_label = tk.Label(self.root, text="Select game size:")
        game_size_label.grid(row=9, column=0, columnspan=4)
        

        self.game_size_var = tk.StringVar(self.root)
        self.game_size_var.set(self.game_size_options[2])

        game_size_menu = tk.OptionMenu(self.root, self.game_size_var, *self.game_size_options)
        game_size_menu.grid(row=10, column=0, columnspan=4, padx=5, pady=5)

        

        next_button = tk.Button(self.root, text="Next", command=self.start_game)
        next_button.grid(row=11, column=0, columnspan=4, padx=5, pady=5)

    def start_game(self):
        self.player_name = self.name_entry.get()
        self.opponent_type = self.opponent_var.get()

        for widget in self.root.winfo_children():
            widget.destroy()

        self.board = self.initialize_board()
        self.board_labels = [[None] * 4 for _ in range(4)]
        self.create_game_board()
        self.update_interface()
        self.root.bind("<Key>", self.on_key)

        self.root.mainloop()


    def initialize_board(self):
        board = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(0)
            board.append(row)
        self.add_number(board)
        self.add_number(board)
        return board

    def add_number(self, board):
        empty_positions = self.find_empty_positions(board)
        if empty_positions:
            position = random.choice(empty_positions)
            value = 2 if random.random() < 0.5 else 4
            board[position[0]][position[1]] = value

    def find_empty_positions(self, board):
        empty_positions = []
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    empty_positions.append((i, j))
        return empty_positions

    def print_board(self, board):
        for row in board:
            for number in row:
                print(number, end="\t")
            print()

    def move_up(self):
        for column in range(4):
            column_values = [self.board[i][column] for i in range(4) if self.board[i][column] != 0]
            column_values = self.combine_numbers(column_values)
            column_values += [0] * (4 - len(column_values))

            for i in range(4):
                self.board[i][column] = column_values[i]

    def move_down(self):
        for column in range(4):
            column_values = [self.board[i][column] for i in range(3, -1, -1) if self.board[i][column] != 0]
            column_values = self.combine_numbers(column_values)
            column_values = [0] * (4 - len(column_values)) + column_values[::-1]

            for i in range(4):
                self.board[i][column] = column_values[i]

    def move_left(self):
        for row in range(4):
            row_values = [number for number in self.board[row] if number != 0]
            row_values = self.combine_numbers(row_values)
            row_values += [0] * (4 - len(row_values))

            for i in range(4):
                self.board[row][i] = row_values[i]

    def move_right(self):
        for row in range(4):
            row_values = [number for number in self.board[row][::-1] if number != 0]
            row_values = self.combine_numbers(row_values)
            row_values = [0] * (4 - len(row_values)) + row_values[::-1]

            for i in range(4):
                self.board[row][i] = row_values[i]

    def combine_numbers(self, list_to_combine):
        for i in range(len(list_to_combine) - 1):
            if list_to_combine[i] == list_to_combine[i + 1]:
                list_to_combine[i] *= 2
                list_to_combine[i + 1] = 0
        list_to_combine = [number for number in list_to_combine if number != 0]
        list_to_combine += [0] * (4 - len(list_to_combine))
        return list_to_combine

    def update_interface(self):
        for i in range(int(self.game_size_var.get())):
            for j in range(int(self.game_size_var.get())):
                cell_value = self.board[i][j]
                cell_label = self.board_labels[i][j]
                cell_label.config(text=str(cell_value) if cell_value != 0 else "", bg=self.color_background(cell_value))

    def color_background(self, value):
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

    def on_key(self, event):
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
                self.move_up()
            elif direction == 's':
                self.move_down()
            elif direction == 'a':
                self.move_left()
            elif direction == 'd':
                self.move_right()

            self.add_number(self.board)
            self.update_interface()


if __name__ == "__main__":
    game = Game2048()
 