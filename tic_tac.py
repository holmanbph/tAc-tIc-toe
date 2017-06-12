# Tick tack toe
import subprocess
import re

__author__ = "Brett Holman"


Matrix=[[' ' for i in range(3)] for i in range(3)]


def print_grid():
    """Clears out the screen and Prints out the formatted grid."""
    res = subprocess.check_output(['clear'])
    for line in res.splitlines():
        print line
    print '\n\n'
    print '\t     A   B   C'
    print ''
    print '\t1    {} | {} | {}'.format( Matrix[0][0], Matrix[0][1], Matrix[0][2])
    print '\t    -----------'
    print '\t2    {} | {} | {}'.format( Matrix[1][0], Matrix[1][1], Matrix[1][2])
    print '\t    -----------'
    print '\t3    {} | {} | {}'.format( Matrix[2][0], Matrix[2][1], Matrix[2][2])
    print '\n\n'


def get_input(user):
    user_input = str(raw_input('{}\'s Turn: '.format( user ))).strip().lower()
    interpret_input(user_input, user)
    return user_input

def write_piece(y, x, user):

    # check if place is taken
    if (Matrix[y][x] == ' '):
        Matrix[y][x] = user
    else:
        print "That spot is taken, SUCKA!!"
        get_input(user)

def interpret_input(input, user):
    if len(input)<2:
        print 'Too few characters entered.  Try again.'
        get_input(user)
    elif len(input)>2:
        print 'Too many characters entered.  Try again.'
        get_input(user)
    elif not set(input)<=set('abc123'):
        print 'Wrong type of character entered.  Only the characters \'abc123\' are allowed.'
        get_input(user)

    if('a'in input):
        if '1' in input:
            write_piece(0, 0, user)
        elif '2' in input:
            write_piece(1, 0, user)
        elif '3' in input:
            write_piece(2, 0, user)
            Matrix[2][0] = user
        else:
            print 'Logical ERROR in interpret_input, NUMBER case not considered'

    elif('b' in input):
        if '1' in input:
            write_piece(0, 1, user)
        elif '2' in input:
            write_piece(1, 1, user)
        elif '3' in input:
            write_piece(2, 1, user)
        else:
            print 'Logical ERROR in interpret_input, NUMBER case not considered'

    elif('c' in input):
        if '1' in input:
            write_piece(0, 2, user)
        elif '2' in input:
            write_piece(1, 2, user)
        elif '3' in input:
            write_piece(2, 2, user)
        else:
            print 'Logical ERROR in interpret_input, NUMBER case not considered'
    else:
        print 'Logical ERROR in interpret_input, LETTER case not considered'

def check_board(player):

    # Someone wins
    for i in range(3):
        # Check each column
        if (Matrix[0][i]==Matrix[1][i]==Matrix[2][i]):
            if Matrix[0][i] == ' ':
                return [None]
            return ['winner', player]
        # Check each row
        elif(Matrix[i][0]==Matrix[i][1]==Matrix[i][2]):
            if Matrix[i][0] == ' ':
                return [None]
            return ['winner', player]
    if (Matrix[0][0]==Matrix[1][1]==Matrix[2][2]):
        if Matrix[1][1] == ' ':
            return [None]
        return ['winner', player]
    elif (Matrix[0][2]==Matrix[1][1]==Matrix[2][0]):
        if Matrix[1][1] == ' ':
            return [None]
        return ['winner', player]

    # Board is full; no one wins
    # (no items in list are ' ')
    return [None]


def play():
    player_turn = 'X'

    check = check_board(player_turn)[0]
    while(True):
        print_grid()
        print 'check={}'.format(check)
        get_input(player_turn)
        player_turn = 'O' if player_turn=='X' else 'X'
        check = check_board(player_turn)[0]

        if check == 'winner':
            print_grid()
            print 'Player {} wins!!!\n\n'.format(player_turn)
            return

def main():
    while True:
        play()
        response = raw_input("Play again? [Y/n]").strip().lower()
        if response == 'n' or respone == 'no':
            return
if __name__ == "__main__":
    main()

