import random
import tkinter as tk
import json


class Game2048:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("2048 Game By Gelu Galan")
        self.player_name = ""
        self.opponent_type = ""
        self.game_size_var=""
        self.opponent_options = ["solo", "computer", "human"]
        self.game_size_options = ["2", "3", "4", "5", "6", "7", "8", "9"]
        self.score = 0
        with open("scores.json", "r") as json_file:
            self.scoruri_json = json.load(json_file)
        self.create_start_screen()
        self.root.mainloop()
        


    def create_game_board(self,best_score_val):
        player_name_label = tk.Label(self.root, text="Name: {}".format(self.player_name))
        player_name_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        opponent_type_label = tk.Label(self.root, text="Opponent: {}".format(self.opponent_type))
        opponent_type_label.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

        # Etichete pentru scor și cel mai bun scor
        self.score_label = tk.Label(self.root, text="Score: {}".format(self.score))
        self.score_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        best_score_label = tk.Label(self.root, text="Best: {}".format(best_score_val))
        best_score_label.grid(row=1, column=2, columnspan=2, padx=5, pady=5)

        for i in range(int(self.game_size_var)):
            for j in range(int(self.game_size_var)):
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
        self.game_size_var = self.game_size_var.get()
        index_joc = int(self.game_size_var)
        game_info = self.scoruri_json["scoruri"].get(f"{index_joc}x{index_joc}") 
        
        
            
        for widget in self.root.winfo_children():
            widget.destroy()
        best_score = game_info.get("best_score", {}).get("scor", 0)
        self.board = self.initialize_board()
        self.board_labels = [[None] * int(self.game_size_var) for _ in range(int(self.game_size_var))]
        self.create_game_board(best_score)
        self.update_interface()
        self.root.bind("<Key>", self.on_key)

        self.root.mainloop()


    def initialize_board(self):
        board = []
        for i in range(int(self.game_size_var)):
            row = []
            for j in range(int(self.game_size_var)):
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
        for i in range(int(self.game_size_var)):
            for j in range(int(self.game_size_var)):
                if board[i][j] == 0:
                    empty_positions.append((i, j))
        return empty_positions

    def print_board(self, board):
        for row in board:
            for number in row:
                print(number, end="\t")
            print()

    def move_up(self):
        for column in range(int(self.game_size_var)):
            column_values = [self.board[i][column] for i in range(int(self.game_size_var)) if self.board[i][column] != 0]
            column_values = self.combine_numbers(column_values)
            column_values += [0] * (int(self.game_size_var) - len(column_values))

            for i in range(int(self.game_size_var)):
                self.board[i][column] = column_values[i]

    def move_down(self):
        for column in range(int(self.game_size_var)):
            column_values = [self.board[i][column] for i in range(int(self.game_size_var) - 1, -1, -1) if self.board[i][column] != 0]
            column_values = self.combine_numbers(column_values)
            column_values = [0] * (int(self.game_size_var) - len(column_values)) + column_values[::-1]

            for i in range(int(self.game_size_var)):
                self.board[i][column] = column_values[i]

    def move_left(self):
        for row in range(int(self.game_size_var)):
            row_values = [number for number in self.board[row] if number != 0]
            row_values = self.combine_numbers(row_values)
            row_values += [0] * (int(self.game_size_var) - len(row_values))

            for i in range(int(self.game_size_var)):
                self.board[row][i] = row_values[i]

    def move_right(self):
        for row in range(int(self.game_size_var)):
            row_values = [number for number in self.board[row][::-1] if number != 0]
            row_values = self.combine_numbers(row_values)
            row_values = [0] * (int(self.game_size_var) - len(row_values)) + row_values[::-1]

            for i in range(int(self.game_size_var)):
                self.board[row][i] = row_values[i]

    def combine_numbers(self, list_to_combine):
        for i in range(len(list_to_combine) - 1):
            if list_to_combine[i] == list_to_combine[i + 1]:
                list_to_combine[i] *= 2
                self.score += list_to_combine[i]
                list_to_combine[i + 1] = 0
        list_to_combine = [number for number in list_to_combine if number != 0]
        list_to_combine += [0] * (int(self.game_size_var) - len(list_to_combine))
        self.update_scores(self.player_name, self.score)
        return list_to_combine

    def update_interface(self):
        for i in range(int(self.game_size_var)):
            for j in range(int(self.game_size_var)):
                cell_value = self.board[i][j]
                cell_label = self.board_labels[i][j]
                cell_label.config(text=str(cell_value) if cell_value != 0 else "", bg=self.color_background(cell_value))
                self.score_label.config(text="Score: {}".format(self.score))


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

    def update_scores(self, player_name, new_score):
        index_joc = int(self.game_size_var)
        game_info = self.scoruri_json["scoruri"].get(f"{index_joc}x{index_joc}")

        if game_info:
            scores = game_info.get("scores", {})
            best_score_info = game_info.get("best_score", {})

            player_info = scores.get(player_name, {})

            
            if player_info.get("score_player", 0) < new_score:
                player_info["player_name"] = player_name
                player_info["score_player"] = new_score
                scores[player_name] = player_info

                
                if new_score > best_score_info.get("scor", 0):
                    best_score_info["jucator"] = player_name
                    best_score_info["scor"] = new_score
                    game_info["best_score"] = best_score_info

                
                game_info["scores"] = scores
                self.scoruri_json["scoruri"][f"{index_joc}x{index_joc}"] = game_info

                with open("scores.json", "w") as json_file:
                    json.dump(self.scoruri_json, json_file, indent=4)


if __name__ == "__main__":
    game = Game2048()
 