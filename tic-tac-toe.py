# Week 2 Tic-Tac-Toe Prove Assignment
# Jordan Waite

# Create a global dictionary for the board that corresponds with the number
# pad on the keyboard.
theboard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

# This will allow us to print an updated version of the game board.
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

board_keys = []
for key in theboard:
    board_keys.append(key)

# Define the main function that will begin the game.
def main():

    turn = 'X'
    count = 0

    # Check to see if the input from the player is a valid move. If so 
    # we want fill that spot, if not we want to alert the player that
    # they cannot fill that position.
    for i in range(10):
        printBoard(theboard)
        print("It's your turn " + turn + ". Move to which place?")

        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count += 1

        else:
            print("That position is already filled. \nMove to which position?")
            continue

        if count >= 5:
            if theboard['7'] == theboard['8'] == theboard['9'] != ' ': # across the top
                printBoard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " is victorious. ****")                
                break
            elif theboard['4'] == theboard['5'] == theboard['6'] != ' ': # across the middle
                printBoard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " is victorious. ****")
                break
            elif theboard['1'] == theboard['2'] == theboard['3'] != ' ': # across the bottom
                printBoard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " is victorious. ****")
                break
            elif theboard['1'] == theboard['4'] == theboard['7'] != ' ': # down the left side
                printBoard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " is victorious. ****")
                break
            elif theboard['2'] == theboard['5'] == theboard['8'] != ' ': # down the middle
                printBoard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " is victorious. ****")
                break
            elif theboard['3'] == theboard['6'] == theboard['9'] != ' ': # down the right side
                printBoard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " is victorious. ****")
                break 
            elif theboard['7'] == theboard['5'] == theboard['3'] != ' ': # diagonal
                printBoard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " is victorious. ****")
                break
            elif theboard['1'] == theboard['5'] == theboard['9'] != ' ': # diagonal
                printBoard(theboard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " is victorious! ****")
                break 

        # If the board is full and neither player has won we will say it's a tie.
        if count == 9:
            print("\nGame Over\n")                
            print("It's a tie!")

        # We have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X' 


    # Now we want to ask the players if they want to replay.
    restart = input("Play again?(y/n)")

    while restart == "y" or restart == "Y":
        for key in board_keys:
            theboard[key] = " "

        main()

if __name__ == "__main__":
    main()
