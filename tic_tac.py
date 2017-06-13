# Tic tac to
import subprocess

__author__ = "Brett Holman"



class Game(object):

    def __init__(self):
        self.Board=[[' ' for i in range(3)] for i in range(3)]


    def print_grid(self):
        """Clears out the screen and Prints out the formatted grid."""
        res = subprocess.check_output(['clear'])
        for line in res.splitlines():
            print line
        print '\n\n'
        print '\t     A   B   C'
        print ''
        print '\t1    {} | {} | {}'.format( self.Board[0][0], self.Board[0][1], self.Board[0][2])
        print '\t    -----------'
        print '\t2    {} | {} | {}'.format( self.Board[1][0], self.Board[1][1], self.Board[1][2])
        print '\t    -----------'
        print '\t3    {} | {} | {}'.format( self.Board[2][0], self.Board[2][1], self.Board[2][2])
        print '\n\n'


    def get_input(self, user):
        user_input = str(raw_input('{}\'s Turn: '.format( user ))).strip().lower()
        self.interpret_input(user_input, user)
        return user_input

    def write_piece(self, y, x, user):

        # check if place is taken
        if (self.Board[y][x] == ' '):
            self.Board[y][x] = user
        else:
            print "That spot is taken, SUCKA!!"
            self.get_input(user)

    def interpret_input(self, input, user):
        if len(input)<2:
            print 'Too few characters entered.  Try again.'
            self.get_input(user)
        elif len(input)>2:
            print 'Too many characters entered.  Try again.'
            self.get_input(user)
        elif not set(input)<=set('abc123'):
            print 'Wrong type of character entered.  Only the characters \'abc123\' are allowed.'
            self.get_input(user)

        if('a'in input):
            if '1' in input:
                self.write_piece(0, 0, user)
            elif '2' in input:
                self.write_piece(1, 0, user)
            elif '3' in input:
                self.write_piece(2, 0, user)
                self.Board[2][0] = user
            else:
                print 'Logical ERROR in self.interpret_input, NUMBER case not considered'

        elif('b' in input):
            if '1' in input:
                self.write_piece(0, 1, user)
            elif '2' in input:
                self.write_piece(1, 1, user)
            elif '3' in input:
                self.write_piece(2, 1, user)
            else:
                print 'Logical ERROR in self.interpret_input, NUMBER case not considered'

        elif('c' in input):
            if '1' in input:
                self.write_piece(0, 2, user)
            elif '2' in input:
                self.write_piece(1, 2, user)
            elif '3' in input:
                self.write_piece(2, 2, user)
            else:
                print 'Logical ERROR in self.interpret_input, NUMBER case not considered'
        else:
            print 'Logical ERROR in self.interpret_input, LETTER case not considered'

    def check_board(self, player):

        # Someone wins
        for i in range(3):
            # Check each column
            if (self.Board[0][i]==self.Board[1][i]==self.Board[2][i]):
                if self.Board[0][i] == ' ':
                    return [None]
                return ['winner', player]
            # Check each row
            elif(self.Board[i][0]==self.Board[i][1]==self.Board[i][2]):
                if self.Board[i][0] == ' ':
                    return [None]
                return ['winner', player]
        if (self.Board[0][0]==self.Board[1][1]==self.Board[2][2]):
            if self.Board[1][1] == ' ':
                return [None]
            return ['winner', player]
        elif (self.Board[0][2]==self.Board[1][1]==self.Board[2][0]):
            if self.Board[1][1] == ' ':
                return [None]
            return ['winner', player]

        # Board is full; no one wins
        # (no items in list are ' ')
        return [None]


    def game_play(self):
        player_turn = 'X'

        check = self.check_board(player_turn)[0]
        while(True):
            self.print_grid()
            self.get_input(player_turn)
            player_turn = 'O' if player_turn=='X' else 'X'
            check = self.check_board(player_turn)[0]

            if check == 'winner':
                self.print_grid()
                print 'Player {} wins!!!\n\n'.format(player_turn)
                return

    def play(self):
        while True:
            try:
                self.game_play()
                response = raw_input("Play again? [Y/n]").strip().lower()
                if response == 'n' or response == 'no':
                    return
            except EOFError:
                print 'Have a nice day!\n\n'
                self.print_grid()
                exit()

if __name__ == "__main__":
    tic_tac = Game()
    tic_tac.play()

