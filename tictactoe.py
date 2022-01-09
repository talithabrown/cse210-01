# Tic-Tac-Toe Game by Talitha Brown

def main():

    print("\nWelcome to this Tic-Tac-Toe game!")
    print()

    xo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_winner = False
    is_draw = False
    i = 2


    while not is_winner and not is_draw:

        if i % 2 == 0:
            x_or_o = "x"
        elif i % 2 == 1:
            x_or_o = "o"

        display_grid(xo_list)

        player_turn(x_or_o, xo_list)

        is_winner = check_for_winner(x_or_o, xo_list)

        if is_winner:
            print(f"\n{x_or_o} wins! Game over")
        else:
            is_draw = check_for_draw(xo_list)
            if is_draw:
                print("This game is a draw.")

        i += 1

    display_grid(xo_list)
    
    
def display_grid(xo_list):
    print()
    print(f"{xo_list[0]}|{xo_list[1]}|{xo_list[2]}")
    print("-+-+-")
    print(f"{xo_list[3]}|{xo_list[4]}|{xo_list[5]}")
    print("-+-+-")
    print(f"{xo_list[6]}|{xo_list[7]}|{xo_list[8]}")
    print()


def player_turn(x_or_o, xo_list):
    player_move = int(input(f"{x_or_o}'s turn to choose a square (1-9): "))
    player_move = player_move - 1
    xo_list[player_move] = x_or_o


def check_for_winner(x_or_o, xo_list):
    if xo_list[0] == x_or_o and xo_list[1] == x_or_o and xo_list[2] == x_or_o:
        is_winner = True
    elif xo_list[3] == x_or_o and xo_list[4] == x_or_o and xo_list[5] == x_or_o:
        is_winner = True
    elif xo_list[6] == x_or_o and xo_list[7] == x_or_o and xo_list[8] == x_or_o:
        is_winner = True
    elif xo_list[0] == x_or_o and xo_list[3] == x_or_o and xo_list[6] == x_or_o:
        is_winner = True
    elif xo_list[1] == x_or_o and xo_list[4] == x_or_o and xo_list[7] == x_or_o:
        is_winner = True
    elif xo_list[2] == x_or_o and xo_list[5] == x_or_o and xo_list[8] == x_or_o:
        is_winner = True
    elif xo_list[0] == x_or_o and xo_list[4] == x_or_o and xo_list[8] == x_or_o:
        is_winner = True
    elif xo_list[2] == x_or_o and xo_list[4] == x_or_o and xo_list[6] == x_or_o:
        is_winner = True
    else:
        is_winner = False

    return is_winner

def check_for_draw(xo_list):
    for i in range(9):
        if xo_list[i] != "x" and xo_list[i] != "o":
            return False
    return True 

if __name__ == "__main__":
    main()
