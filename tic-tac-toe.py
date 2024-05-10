print("TIC TAC TOE")
print("\n.\n..\n...\nPress Enter to Start....")
input()

print("\nEnter a number n for the dimension of a squared grid: ")
n = int(input())

# 1,2,3,
# 4,5,6,
# 7,8,9,

# 123
# 456
# 789
# 159
# 357
# 147
# 258
# 369

# 1,   2,   3,   4,
# 5,   6,   7,   8,
# 9,  10,  11,  12,
# 13, 14,  15,  16,

# 1234
# 5678
# 9101112
# 13141516
# 161116
# 471013
# 15913
# 261014
# 371115
# 481216

board = [[None for _ in range(n)] for _ in range(n)]


def print_board():
    print("\n")
    for i, row in enumerate(board):
        for j, block in enumerate(row):
            print(f"| {block if block else (j+n*i)} ", end="")
        print("|\n")


def is_game_complete():
    for row in board:
        if None in row:
            return False
    return True


def mark(player, index):
    if board[index[0]][index[1]] is None:
        board[index[0]][index[1]] = player
        return True
    return False


def check(player):
    for row in board:
        if row.count(player) == len(row):
            return True
    columns = []
    diagnal1 = []
    diagnal2 = []
    for i in range(n):
        column = []
        for j in range(n):

            column.append(board[j][i])
            if i == j:
                diagnal1.append(board[i][j])
            if j == n - i - 1:
                diagnal2.append(board[i][j])
        columns.append(column)

    for column in columns:
        if row.count(player) == len(row):
            return True

    if diagnal1.count(player) == len(diagnal1):
        return True
    if diagnal2.count(player) == len(diagnal2):
        return True

    return False


# 012
# 345
# 678

# 036
# 147
# 258

# 048
# 246


# 0 => 0 ,1 ,2  => 0+3*0 ,1 ,2
# 1 => 0 ,1 ,2  => 0+3*1, 1+3*1, 2+3*1
# 2 => 0 ,1 ,2  => 0+3*2, 1+3*2, 2+3*2

# 0 => 0//3=0, 3%3=0 => [0][0]
# 1 => 1//3=0, 1%3=1 => [0][1]
# 2 => 2//3=0, 2%3=2 => [0][2]

# 3 => 3//3=1, 3%3=0 => [1][0]
# 4 => 4//3=1, 4%3=1 => [1][1]
# 5 => 5//3=1, 5%3=2 => [1][2]

# 6 => 6//3=2, 6%3=0 => [2][0]
# 7 => 7//3=2, 7%3=1 => [2][1]
# 8 => 8//3=2, 8%3=2 => [2][2]

# columns:
# 00,  01,  02
# 10,  11,  12
# 20,  21,  22

# diangals:
# 00 , 11, 22
# 02 , 11, 20

play = True
while play:

    print_board()
    print("\nPick a block by entering number")
    input_x = int(input("Player X: "))

    while not mark("X", [input_x // n, input_x % n]):
        print("This blocked is already Marked!")
        input_x = int(input("Player X: "))

    print_board()

    if check("X"):
        print("Player X Won!")
        ch = input("Do you want to play agian! ... Enter (y/Y) to continue:")
        if ch.lower() == "y":
            board = [
                [None, None, None],
                [None, None, None],
                [None, None, None],
            ]
            continue
        else:
            play = False

    if is_game_complete():
        print("Draw! ---- NO ONE WON!  ;;;;")
        ch = input("Do you want to play agian! ... Enter (y/Y) to continue:")
        if ch.lower() == "y":
            board = [
                [None, None, None],
                [None, None, None],
                [None, None, None],
            ]
            continue
        else:
            play = False

    print("\nPick a block by entering number")
    input_o = int(input("Player O: "))
    while not mark("O", [input_o // n, input_o % n]):
        print("This blocked is already Marked!")
        input_o = int(input("Player O: "))
    print_board()

    if check("O"):
        print("Player O Won!")
        ch = input("Do you want to play agian! ... Enter (y/Y) to continue:")
        if ch.lower() == "y":
            board = [
                [None, None, None],
                [None, None, None],
                [None, None, None],
            ]
            continue
        else:
            play = False

    if is_game_complete():
        print("Draw! ---- NO ONE WON!  ;;;;")
        ch = input("Do you want to play agian! ... Enter (y/Y) to continue:")
        if ch.lower() == "y":
            board = [
                [None, None, None],
                [None, None, None],
                [None, None, None],
            ]
            continue
        else:
            play = False

# input()
