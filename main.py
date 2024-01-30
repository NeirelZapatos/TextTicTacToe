from boards import Board

board = Board()

board_full = False
while not board_full:
    # display board
    board.display()
    print()

    # add and x and check if x wins
    board.add_symbol("x")
    print()
    board.display()
    if board.check_win("x"):
        print(f"player x has won!")
        break

    # add and o and check if o wins
    board.add_symbol("o")
    print()
    board.display()
    if board.check_win("o"):
        print(f"player o has won!")
        break

    # check if board is full
    board_full = board.check_full()



