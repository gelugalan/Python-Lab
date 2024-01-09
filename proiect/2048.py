import random
import tkinter as tk
import json


class Game2048:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="darkgrey")

        self.root.title("2048 Game By Gelu Galan")
        self.player_name = []
        
        self.opponent_type = ""
        self.game_size_var = ""
        self.opponent_options = ["solo", "computer", "human"]
        self.game_size_options = ["2", "3", "4", "5", "6", "7", "8", "9"]
        self.score = 0
        self.current_page = 0
        self.buttons_created = False
        self.num_players = 1
        with open("scores.json", "r") as json_file:
            self.scoruri_json = json.load(json_file)
        self.create_start_screen()
        self.root.mainloop()

    def create_game_board(self, best_score_val, player_num):
        if self.board_labels is None:
            self.board_labels = [[[None] * int(self.game_size_var) for _ in range(int(self.game_size_var))] for _ in range(2)]
        else:
            
            self.board_labels[player_num] = [[None] * int(self.game_size_var) for _ in range(int(self.game_size_var))]
        if player_num==0:
            player_name_label = tk.Label(self.root, text="Name: {}".format(self.player_name[0]))
            player_name_label.grid(row=0, column=player_num * (int(self.game_size_var) + 2), columnspan=2, padx=5, pady=5)
        else:
            player_name_label = tk.Label(self.root, text="Name: {}".format(self.player_name[1]))
            player_name_label.grid(row=0, column=player_num * (int(self.game_size_var) + 2), columnspan=2, padx=5, pady=5)

        

        opponent_type_label = tk.Label(self.root, text="Opponent: {}".format(self.opponent_type))
        opponent_type_label.grid(row=0, column=player_num * (int(self.game_size_var) + 2) + 2, columnspan=2, padx=5, pady=5)

        
        score_label = tk.Label(self.root, text="Score: {}".format(self.score))
        score_label.grid(row=1, column=player_num * (int(self.game_size_var) + 2), columnspan=2, padx=5, pady=5)

        best_score_label = tk.Label(self.root, text="Best: {}".format(best_score_val))
        best_score_label.grid(row=1, column=player_num * (int(self.game_size_var) + 2) + 2, columnspan=2, padx=5, pady=5)

        
        

        for i in range(int(self.game_size_var)):
            for j in range(int(self.game_size_var)):
                cell_label = tk.Label(self.root, text="", width=5, height=2)
                cell_label.grid(row=i + 3, column=player_num * (int(self.game_size_var) + 2) + j, padx=5, pady=5)
                self.board_labels[player_num][i][j] = cell_label
        

        if not self.buttons_created and self.opponent_type == "human":
            self.buttons_created = True  # Set the flag to True to avoid creating buttons again

            new_game_button = tk.Button(self.root, text="New", command=self.restart_game)
            new_game_button.grid(row=int(self.game_size_var) + 3, column=player_num * (int(self.game_size_var) + 2), columnspan=1, padx=5, pady=5)

            # Add Quit button
            quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
            quit_button.grid(row=int(self.game_size_var) + 3, column=player_num * (int(self.game_size_var) + 2) + 1, columnspan=1, padx=5, pady=5)



        
        
    

    def create_start_screen(self):
        self.start_frame = tk.Frame(self.root)
        self.start_frame.grid(row=0, column=0)

        self.opponent_label = tk.Label(self.start_frame, text="Select opponent:")
        self.opponent_label.grid(row=0, column=0, columnspan=2)

        self.opponent_var = tk.StringVar(self.start_frame)
        self.opponent_var.set(self.opponent_options[0])

        solo_radio = tk.Radiobutton(self.start_frame, text="Solo", variable=self.opponent_var, value="solo")
        solo_radio.grid(row=1, column=0, padx=5, pady=5)

        multiplayer_radio = tk.Radiobutton(self.start_frame, text="Multiplayer", variable=self.opponent_var, value="human")
        multiplayer_radio.grid(row=1, column=1, padx=5, pady=5)

        next_button = tk.Button(self.start_frame, text="Next", command=self.create_selected_fields)
        next_button.grid(row=2, column=2, padx=5, pady=5)

    def create_selected_fields(self):
        # Destroy the current start frame
        self.start_frame.destroy()

        # Check the selected opponent and call the corresponding function
        selected_opponent = self.opponent_var.get()
        if selected_opponent == "solo":
            self.create_solo_fields()
        elif selected_opponent == "human":
            self.create_multiplayer_fields()

        

    


    def create_solo_fields(self):
        name_label = tk.Label(self.root, text="Name:")
        name_label.grid(row=2, column=0, columnspan=4)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        game_size_label = tk.Label(self.root, text="Select game size:")
        game_size_label.grid(row=4, column=0, columnspan=4)

        self.game_size_var = tk.StringVar(self.root)
        self.game_size_var.set(self.game_size_options[2])

        top_scores_button = tk.Button(self.root, text="Top Scores", command=self.show_top_scores)
        top_scores_button.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

        game_size_menu = tk.OptionMenu(self.root, self.game_size_var, *self.game_size_options)
        game_size_menu.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

        next_button = tk.Button(self.root, text="Next", command=self.start_game)
        next_button.grid(row=7, column=0, columnspan=4, padx=5, pady=5)

    def create_multiplayer_fields(self):
        name_label_p1 = tk.Label(self.root, text="Player 1 Name:")
        name_label_p1.grid(row=2, column=0, columnspan=4)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

        name_entry2 = tk.Label(self.root, text="Player 2 Name:")
        name_entry2.grid(row=4, column=0, columnspan=4)

        self.player2_name_entry = tk.Entry(self.root)
        self.player2_name_entry.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

        game_size_label = tk.Label(self.root, text="Select game size:")
        game_size_label.grid(row=6, column=0, columnspan=4)

        self.game_size_var = tk.StringVar(self.root)
        self.game_size_var.set(self.game_size_options[2])

        top_scores_button = tk.Button(self.root, text="Top Scores", command=self.show_top_scores)
        top_scores_button.grid(row=9, column=0, columnspan=4, padx=5, pady=5)

        game_size_menu = tk.OptionMenu(self.root, self.game_size_var, *self.game_size_options)
        game_size_menu.grid(row=8, column=0, columnspan=4, padx=5, pady=5)

        next_button = tk.Button(self.root, text="Next", command=self.start_game)
        next_button.grid(row=10, column=0, columnspan=4, padx=5, pady=5)


    def restart_game(self):
        self.root.destroy()
        game = Game2048()



    def start_game(self):
        self.player_name.append(self.name_entry.get())
        self.player_name.append(self.player2_name_entry.get())

        self.opponent_type = self.opponent_var.get()
        self.game_size_var = self.game_size_var.get()
        index_joc = int(self.game_size_var)
        game_info = self.scoruri_json["scoruri"].get(f"{index_joc}x{index_joc}")

        for widget in self.root.winfo_children():
            widget.destroy()
        best_score = game_info.get("best_score", {}).get("scor", 0)

        if self.opponent_type == "human":
            self.num_players = 2

        # Create two game boards for each player
        self.board = [self.initialize_board(), self.initialize_board()]
        self.board_labels = [[[None] * int(self.game_size_var) for _ in range(int(self.game_size_var))] for _ in range(2)]
        self.create_game_board(best_score, 0)
        if self.opponent_type == "human":
            self.create_game_board(best_score, 1)
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

    def move_up(self, player_num):
        for column in range(int(self.game_size_var)):
            column_values = [self.board[player_num][i][column] for i in range(int(self.game_size_var)) if self.board[player_num][i][column] != 0]
            column_values = self.combine_numbers(column_values)
            column_values += [0] * (int(self.game_size_var) - len(column_values))

            for i in range(int(self.game_size_var)):
                self.board[player_num][i][column] = column_values[i]

    def move_down(self, player_num):
        for column in range(int(self.game_size_var)):
            column_values = [self.board[player_num][i][column] for i in range(int(self.game_size_var) - 1, -1, -1) if self.board[player_num][i][column] != 0]
            column_values = self.combine_numbers(column_values)
            column_values = [0] * (int(self.game_size_var) - len(column_values)) + column_values[::-1]

            for i in range(int(self.game_size_var)):
                self.board[player_num][i][column] = column_values[i]

    def move_left(self, player_num):
        for row in range(int(self.game_size_var)):
            row_values = [number for number in self.board[player_num][row] if number != 0]
            row_values = self.combine_numbers(row_values)
            row_values += [0] * (int(self.game_size_var) - len(row_values))

            for i in range(int(self.game_size_var)):
                self.board[player_num][row][i] = row_values[i]

    def move_right(self, player_num):
        for row in range(int(self.game_size_var)):
            row_values = [number for number in self.board[player_num][row][::-1] if number != 0]
            row_values = self.combine_numbers(row_values)
            row_values = [0] * (int(self.game_size_var) - len(row_values)) + row_values[::-1]

            for i in range(int(self.game_size_var)):
                self.board[player_num][row][i] = row_values[i]

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

        for player_num in range(self.num_players):
            for i in range(int(self.game_size_var)):
                for j in range(int(self.game_size_var)):
                    cell_value = self.board[player_num][i][j]
                    cell_label = self.board_labels[player_num][i][j]
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
        # movements
        direction_p1 = ""
        direction_p2 = ""
        if event.keysym in ['w']:
            direction_p1 = 'w'
        elif event.keysym in ['s']:
            direction_p1 = 's'
        elif event.keysym in ['a']:
            direction_p1 = 'a'
        elif event.keysym in ['d']:
            direction_p1 = 'd'
        elif event.keysym == 'Up':
            direction_p2 = 'w'
        elif event.keysym == 'Down':
            direction_p2 = 's'
        elif event.keysym == 'Left':
            direction_p2 = 'a'
        elif event.keysym == 'Right':
            direction_p2 = 'd'

        if direction_p1:
            self.process_move(direction_p1, 0)
        if direction_p2:
            self.process_move(direction_p2, 1)

        self.update_interface()

    def process_move(self, direction, player_num):
        if direction == 'w':
            self.move_up(player_num)
        elif direction == 's':
            self.move_down(player_num)
        elif direction == 'a':
            self.move_left(player_num)
        elif direction == 'd':
            self.move_right(player_num)

        self.add_number(self.board[player_num])

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

    def show_top_scores(self):
        top_scores_window = tk.Toplevel(self.root)
        top_scores_window.title("Top Scores")

        
        scores_frame = tk.Frame(top_scores_window)
        scores_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        game_size_label = tk.Label(top_scores_window, text="Select game size:")
        game_size_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        game_size_var = tk.StringVar(top_scores_window)
        game_size_var.set(self.game_size_options[2])

        game_size_menu = tk.OptionMenu(top_scores_window, game_size_var, *self.game_size_options, command=lambda size: self.display_scores(scores_frame, size))
        game_size_menu.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        

    def display_scores(self, scores_frame, selected_game_size):
        for widget in scores_frame.winfo_children():
            widget.destroy()

        game_info = self.scoruri_json["scoruri"].get(f"{selected_game_size}x{selected_game_size}")
        if game_info:
            scores = game_info.get("scores", {})
            scores_label = tk.Label(scores_frame, text="Scores:")
            scores_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)  

            
            sorted_scores = sorted(scores.items(), key=lambda x: x[1]['score_player'], reverse=True)

            for i, (player, score_info) in enumerate(sorted_scores, start=1):
                
                player_label = tk.Label(scores_frame, text=f"{i}. {player}: {score_info['score_player']}")
                player_label.grid(row=i, column=0, columnspan=3, padx=5, pady=2)  



                
if __name__ == "__main__":
    game = Game2048()
 