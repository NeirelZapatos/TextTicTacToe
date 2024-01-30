class Board:
    def __init__(self):
        self.board = [" " for i in range(9)]

    def display(self):
        print("  1 | 2 | 3")
        print(f"a {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("  --+---+--")
        print(f"b {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("  --+---+--")
        print(f"c {self.board[6]} | {self.board[7]} | {self.board[8]}")

    def check_win(self, symbol):
        # check rows
        for i in range(0, 9, 3):
            if all(self.board[i + j] == symbol for j in range(3)):
                return True

        # check columns
        for i in range(3):
            if all(self.board[i + j] == symbol for j in range(0, 9, 3)):
                return True

        # check diagonals
        if all(self.board[i] == symbol for i in [0, 4, 8]) or all(self.board[i] == "x" for i in [2, 4, 6]):
            return True

        return False

    def add_symbol(self, symbol):
        while True:
            location = input(f"What location do you want to add {symbol}? e.g. a1: ")
            # add first row
            for i in range(1, 4):
                if location == f"a{i}":
                    if self.board[i - 1] == " ":
                        self.board[i - 1] = symbol
                        return
                    print("Location already has symbol")

            # add second row
            for i in range(1, 4):
                if location == f"b{i}":
                    if self.board[i + 2] == " ":
                        self.board[i + 2] = symbol
                        return
                    print("Location already has symbol.")

            # add third row
            for i in range(1, 4):
                if location == f"c{i}":
                    if self.board[i + 5] == " ":
                        self.board[i + 5] = symbol
                        return
                    print("Location already has symbol")

            # player didn't add proper location
            print()
            print("Please enter proper location")
            print()

    def check_full(self):
        if all(box != " " for box in self.board):
            return True
        return False
