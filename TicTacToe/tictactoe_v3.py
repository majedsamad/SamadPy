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


def PrintBoard():
    print("".join(board[:5]))
    print("".join(board[5:10]))
    print("".join(board[10:15]))


def GetAndCheckInput(symbol):
    moves_dict = {1: 0, 2: 2, 3: 4, 4: 5, 5: 7, 6: 9, 7: 10, 8: 12, 9: 14}
    user_input = input()
    try:
        user_input = int(user_input)
    except:
        user_input = 0
    while user_input not in nums or user_input in prev_inputs:
        print("Invalid entry; enter value between 1 and 9\n")
        user_input = input()
        try:
            user_input = int(user_input)
        except:
            user_input = 0
    board[moves_dict[user_input]] = symbol
    prev_inputs.append(user_input)


PrintBoard()
prev_inputs = []
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Game start
for i in range(9):
    if i % 2 == 0:
        print("Player 1, enter a move (1-9)\n")
        GetAndCheckInput("X")
        PrintBoard()
    else:
        print("Player 2, enter a move (1-9)\n")
        GetAndCheckInput("O")
        PrintBoard()
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
    elif len(prev_inputs) == 9:
        print("It's a draw!")
