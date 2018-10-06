import re

class Display:
    def __init__(self, length, delimiter, row_divider, game_arr):
        self.length = length
        self.delimiter = delimiter
        self.row_divider = row_divider
        self.game_arr = game_arr

    def print_dividing_row(self):
        print(" ".join(self.row_divider for x in range(self.length)))

    def print_value_row(self, r):
        print(self.delimiter.join(str(val) if val else " " for val in self.game_arr[r]))

    def display_full(self):
        for i in range(self.length):
            self.print_dividing_row()
            self.print_value_row(i)
        self.print_dividing_row()

    def reset_display(self, game_arr):
        self.game_arr = game_arr

class Game:
    def __init__(self, length):
        self.length = int(input("Please choose the length of each side: "))
        self.game_arr = [[None for x in range(length)] for _ in range(length)]
        self.display = Display(length, "|", "-", self.game_arr)
        self.start_loop()

    def start_loop(self):
        player_turn = 1
        while True:
            self.display.display_full()
            player_turn = player_turn % 2
            print("Player {}'s turn".format(player_turn))
            choice_is_valid = False
            while not (choice_is_valid):
                choice = input("Enter your choice in the format x y.")
                if not re.fullmatch(r"\d\s\d", choice):
                    print("Invalid format")
                    continue
                i, j = [int(x) for x in choice.split(" ")]
                if self.game_arr[i][j] != None:
                    print("{} is already in your desired choice! ".format(self.game_arr[i][j]))
                    continue
                if 0 <= i < self.length and 0 <= j < self.length:
                    choice_is_valid = True
                else:
                    print("Your values are out of boundaries")
            if player_turn == 1:
                self.game_arr[i][j] = 'O'
            else:
                self.game_arr[i][j] = 'X'
            self.check_won()

            player_turn += 1



    def check_won(self):
        for row in self.game_arr:
            if all(x == 'X' for x in row):
                self.end_game(2)
                return True
            elif all(x == 'O' for x in row):
                self.end_game(1)
                return True
        for col in range(self.length):
            if all(x[col] == 'X' for x in self.game_arr):
                self.end_game(2)
                return True
            elif all(x[col] == 'O' for x in self.game_arr):
                self.end_game(1)
                return True
        if all(self.game_arr[i][i] == 'X' for i in range(self.length)):
            self.end_game(2)
            return True
        if all(self.game_arr[i][i] == 'O' for i in range(self.length)):
            self.end_game(1)
            return True
        return False

    def end_game(self, i):
        self.display.display_full()
        print("Player {} has won! Resetting game. ".format(i))
        new_arr = [[None for x in range(self.length)] for _ in range(self.length)]
        self.game_arr = new_arr
        self.display.reset_display(new_arr)


disp = Display(3, "|", "-", [[x for x in range(3)] for _ in range(3)])

Game(3)