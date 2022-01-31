print(
    "Players 1 and 2 will take turns choosing a space on the board, where 1 is the first space (top left) and 9 is the last (bottom right)."
)

print("First to connect 3 wins!\n\n")

# Board Initialisation
board = [
    "_",
    "|",
    "_",
    "|",
    "_",
    "_",
    "|",
    "_",
    "|",
    "_",
    "_",
    "|",
    "_",
    "|",
    "_",
]
print(str(board[0]) + str(board[1]) + str(board[2]) + str(board[3]) + str(board[4]))
print(str(board[5]) + str(board[6]) + str(board[7]) + str(board[8]) + str(board[9]))
print(
    str(board[10]) + str(board[11]) + str(board[12]) + str(board[13]) + str(board[14])
)

# Move definition
moves = {1: 0, 2: 2, 3: 4, 4: 5, 5: 7, 6: 9, 7: 10, 8: 12, 9: 14}
mem = []
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Game start
for i in range(9):
    if i % 2 == 0:
        print("Player 1, enter a move (1-9)\n")
        x = input()
        try:
            x = int(x)
        except:
            x = ""
        while x == "" or x in mem:
            print("Invalid entry; enter value between 1 and 9\n")
            x = input(x)
            try:
                x = int(x)
            except:
                x = ""
        board[moves[x]] = "X"
        mem.append(x)
        print(
            str(board[0])
            + str(board[1])
            + str(board[2])
            + str(board[3])
            + str(board[4])
        )
        print(
            str(board[5])
            + str(board[6])
            + str(board[7])
            + str(board[8])
            + str(board[9])
        )
        print(
            str(board[10])
            + str(board[11])
            + str(board[12])
            + str(board[13])
            + str(board[14])
        )

    else:
        print("Player 2, enter a move (1-9)\n")
        x = input()
        try:
            x = int(x)
        except:
            x = ""
        while x == "" or x in mem:
            print("Invalid entry; enter value between 1 and 9\n")
            x = input(x)
            try:
                x = int(x)
            except:
                x = ""
        board[moves[x]] = "O"
        mem.append(x)

        print(
            str(board[0])
            + str(board[1])
            + str(board[2])
            + str(board[3])
            + str(board[4])
        )
        print(
            str(board[5])
            + str(board[6])
            + str(board[7])
            + str(board[8])
            + str(board[9])
        )
        print(
            str(board[10])
            + str(board[11])
            + str(board[12])
            + str(board[13])
            + str(board[14])
        )
        
    # Victory Conditions - within for loop
    if (
        (board[0] == "X" and board[7] == "X" and board[14] == "X")
        or (board[0] == "X" and board[2] == "X" and board[4] == "X")
        or (board[0] == "X" and board[5] == "X" and board[10] == "X")
        or (board[2] == "X" and board[7] == "X" and board[12] == "X")
        or (board[4] == "X" and board[7] == "X" and board[10] == "X")
        or (board[4] == "X" and board[9] == "X" and board[14] == "X")
        or (board[5] == "X" and board[7] == "X" and board[9] == "X")
        or (board[10] == "X" and board[12] == "X" and board[14] == "X")
    ):
        print("Player 1 has won!!")
        break
    elif (
        (board[0] == "O" and board[7] == "O" and board[14] == "O")
        or (board[0] == "O" and board[2] == "O" and board[4] == "O")
        or (board[0] == "O" and board[5] == "O" and board[10] == "O")
        or (board[2] == "O" and board[7] == "O" and board[12] == "O")
        or (board[4] == "O" and board[7] == "O" and board[10] == "O")
        or (board[4] == "O" and board[9] == "O" and board[14] == "O")
        or (board[5] == "O" and board[7] == "O" and board[9] == "O")
        or (board[10] == "O" and board[12] == "O" and board[14] == "O")
    ):
        print("Player 2 has won!!")
        break
    elif len(mem) == 9:
        print("It's a draw!")
