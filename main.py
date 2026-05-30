import random #randomly position the ai on the board
from colorama import Fore,init
init(autoreset=True)
#winning combinations
win_conditions = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]
#display the board
def display_board(board):
    def colored(cell): #color a cell that the user has selected
        if cell=="X":
            return Fore.RED+cell
        elif cell=="O":
            return Fore.GREEN+cell
        else:
            return Fore.YELLOW+cell
    #create the board separations
    print("\n")#print a blank new line
    print(f"{colored(board[0])} | {colored(board[1])} | {colored(board[2])}")#row1
    print(Fore.CYAN+"--+-+--+-")
    print(f"{colored(board[3])} | {colored(board[4])} | {colored(board[5])}")#row2
    print(Fore.CYAN+"--+-+--+-")
    print(f"{colored(board[6])} | {colored(board[7])} | {colored(board[8])}")#row3
    print(Fore.CYAN+"--+-+--+-")
    print()#print a blank line
#function-to get the player's symbol
def player_choice():
    symbol=""
    while symbol not in ["X","O"]:
        symbol=input(Fore.GREEN+"Choose x or o:").upper()
        if symbol=="X":
            return "X","O"
        else:
            return "O","X"
#player move
def player_move(board,symbol):
    while True:
        move=input(Fore.GREEN+"Enter the position(1-9):")
        if not move.isdigit():
            print(Fore.RED+"Please enter a number.")
            continue
        move = int(move)
        if move < 1 or move > 9:
            print(Fore.RED+"Please enter a number between 1 and 9")
            continue
        if board[move-1] in ["X","O"]:
            print(Fore.MAGENTA+"Position is already taken")
            continue
        #add the move to the board
        board[move-1]=symbol
        break
#move the ai
def ai_move(board,symbol):
    available=[i for i in range(9) if board[i] not in ["X","O"]]
    move=random.choice(available)
    board[move]=symbol
    print(Fore.BLUE+f"AI choose position {move+1}")
#check for winner
def check_winner(board,symbol):
    for combo in win_conditions:
        if board[combo[0]]==board[combo[1]]==board[combo[2]]==symbol:
            return True#won
        return False #loss
#check for draw
def is_draw(board):
    return all(cell in ["X","O"] for cell in board)
#main program
def play_game():
    board=[" "]*9 #blank board
    player_symbol,ai_symbol=player_choice()
    print(Fore.CYAN+"\n GAME STARTS!")
    current_turn="player"
    while True:
        display_board(board)
        if current_turn=="player":
            player_move(board,player_symbol)
            if check_winner(board,player_symbol):
                display_board(board)
                print(Fore.GREEN+"You win🥳")
                break
            current_turn="ai"
        else:
            ai_move(board,ai_symbol)
            if check_winner(board,ai_symbol):
                display_board(board)
                print(Fore.RED+"AI wins🤖")
                break
            current_turn="player"
        if is_draw(board):
            display_board(board)
            print(Fore.YELLOW+"It is a draw😊")
            break
if __name__=="__main__":
    play_game()#check the function names if there is any that controls the entire game.