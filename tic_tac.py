#!/usr/bin/env python

"""The design of the game was not given much thought, I'm trying to throw something together that can
be used for 'AI' experimentation. This game was not originally object oriented; there are some interesting
design quirks. The goal is to allow PvP and PvComputer game modes, and to focus on learning some 'simple'
AI methods (perhaps using a tool like tensorflow)?


To play:
    $ python tic_tac.py

Dependencies:
    -bash
    -python 2.7.*
    -modules: subprocess, random, time

Attributes:
    Game()
    AI()

Todo:
    - add multiple levels of 'AI'
        - add a random generated one that blocks the opponent if the opponent is about to win
        - learn about tensorflow, potentially look into the monte carlo tree search algorithm
        - allow user to select difficulty
    - improve CLI aesthetics
    - nxn game-play?
    - n**3 game-play?
    - n**n game-play?
    - improve documentation - see google style docstring
    - create some tests to automatically check certain functionalities
"""

import subprocess
import random
import time


__author__ = 'Brett Holman'
__license__ = 'MIT'
__copyright__ = 'Copyright (c) 2017 Brett Holman'
__status__ = 'Prototype'
__credits__ = ['Brett Holman']

class Game(object):
    ''' This game defines the game of tic tac toe. '''
    def __init__(self):
        self.Board = [[' ' for i in range(3)] for i in range(3)]
        self.player_turn = 'X'
        self.default_player = '2'
        self.default_difficulty = '2'
    def print_grid(self):
        """Clears out the screen and Prints out the formatted grid."""
        res = subprocess.check_output(['clear'])
        for line in res.splitlines():
            print line
        print '\n\n'
        print '\t     A   B   C'        # This approach v is kind of a hack.   Find a more precise way to do it.
        print ''            # What if we were to play an nxn game of tic-tac?  nxnxn? n**n?
        print '\t1    {} | {} | {}'.format( self.Board[0][0], self.Board[0][1], self.Board[0][2])
        print '\t    -----------'
        print '\t2    {} | {} | {}'.format( self.Board[1][0], self.Board[1][1], self.Board[1][2])
        print '\t    -----------'
        print '\t3    {} | {} | {}'.format( self.Board[2][0], self.Board[2][1], self.Board[2][2])
        print '\n\n'


    def get_input(self, user, computer):
        '''Prints input message and dispatches computer moves if necessary'''
        if computer == None:
            user_input = str(raw_input('{}\'s Turn: '.format( user ))).strip().lower()
            self.interpret_input(user_input, user, computer)
        # Computer plays the 'O's
        else:
            if user == 'X':
                user_input = str(raw_input('{}\'s Turn: '.format( user ))).strip().lower()
                self.interpret_input(user_input, user, computer)
            else:
                self.interpret_input(computer.turn(self.Board, self.player_turn), user, computer)


    def write_piece(self, y, x, user, computer):
        """Writes user input to the board or prints a message.  If the spot is taken, a recursive call to .get_input() is made """
        # check if place is taken
        if (self.Board[y][x] == ' '):
            self.Board[y][x] = user
        else:
            print "That spot is taken, SUCKA!!"
            self.get_input(user, computer)

    def interpret_input(self, input, user, computer):
        """ Validates user input and calls the write_piece function if input is valid """
        # Indirect recursive calls to get_input
        if len(input)<2:
            print 'Too few characters entered.  Try again.'
            self.get_input(user, computer)
        elif len(input)>2:
            print 'Too many characters entered.  Try again.'
            self.get_input(user, computer)
        elif not set(input)<=set('abc123'):
            print 'Wrong type of character entered.  Only the characters \'abc123\' are allowed.'
            self.get_input(user, computer)
        elif 'a' not in input and 'b' not in input and 'c' not in input:
            print 'Input requires a letter'
            self.get_input(user, computer)
        elif '1' not in input and '2' not in input and '3' not in input:
            print 'Input requires a number'
            self.get_input(user, computer)

        else:
            # Is valid input
            if('a'in input):
                if '1' in input:
                    self.write_piece(0, 0, user, computer)
                elif '2' in input:
                    self.write_piece(1, 0, user, computer)
                elif '3' in input:
                    self.write_piece(2, 0, user, computer)
                    self.Board[2][0] = user
                else:
                    assert False, 'Logical ERROR in self.interpret_input, NUMBER case not considered'

            elif('b' in input):
                if '1' in input:
                    self.write_piece(0, 1, user, computer)
                elif '2' in input:
                    self.write_piece(1, 1, user, computer)
                elif '3' in input:
                    self.write_piece(2, 1, user, computer)
                else:
                    assert False, 'Logical ERROR in self.interpret_input, NUMBER case not considered'

            elif('c' in input):
                if '1' in input:
                    self.write_piece(0, 2, user, computer)
                elif '2' in input:
                    self.write_piece(1, 2, user, computer)
                elif '3' in input:
                    self.write_piece(2, 2, user, computer)
                else:
                    assert False, 'Logical ERROR in self.interpret_input, NUMBER case not considered'
            else:
                assert False, 'Logical ERROR in self.interpret_input, LETTER case not considered'

    def check_board(self, player):
        """ This checkes the board for winners and stalemates"""
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
        for i in range(3):
            for j in range(3):
                if self.Board[i][j] == ' ':
                    return [None]
        return ['draw', "nobody"]


    def game_play(self, computer):
        """This describes the play of the game"""
        # Setup
        print "Human goes first."

        # Turns
        while(True):
            self.print_grid()

            self.get_input(self.player_turn, computer)
            check = self.check_board(self.player_turn)[0]

            if check == 'winner':
                self.print_grid()
                print 'Player {} wins!!!\n\n'.format(self.player_turn)
                return
            elif check == 'draw':
                print "Draw game!  Nobody wins."
                return
            self.player_turn = 'O' if self.player_turn=='X' else 'X'

    def play(self):
        """User options selection.  This includes game setup and teardown"""
        while True:
            try:
                # Human or Machine?
                res = subprocess.check_output(['clear'])
                for i in res.split():
                    print i
                response = raw_input("\n\nGame Type:\n 1) 2 Player\n 2) Computer\n\n>>[2]").strip()

                # Difficulty?
                if response == '2':
                    self.default_difficulty = raw_input('Difficulty: \n1) Easy \n2) Medium \n3) Difficult\n\n>>[2]').strip

                # Default
                if response != '1' and response != '2':
                    response = self.default_player

                # UI Error Handling
                if response != '1' and response != '2':
                    print 'That is not an acceptable input'
                    self.play()# I wonder if this "recursive goto" is very pythonic?
                    return

                # Play the game!!
                self.game_play(computer = AI(self.default_difficulty, self.player_turn) if (response=='2') else None)

                # Play again?
                response = raw_input("Play again? [Y/n]").strip().lower()
                if response == 'n' or response == 'no':
                    return

                # Clear the board each game
                self.Board=[[' ' for i in range(3)] for i in range(3)]

            # Not very pythonic
            except EOFError:
                print 'Have a nice day!\n\n'
                self.print_grid()
                exit()


class AI(object):
    """Randomized computer player.  Literally no strategy going on in this brain."""
    def __init__(self, difficulty, turn):
        random.seed()
        self.letters = ['a', 'b', 'c']
        self.numbers =  ['1','2','3']
        self.difficulty = difficulty
        self.player_turn = turn
    def turn(self, state, turn):
        time.sleep(1)
        if self.difficulty == '1':
            return self.rand(state, turn)
        elif self.difficulty == '2':
            return self.manual(state, turn)
        else:
            return self.Monte(state, turn)

    def rand(self, state, turn):
        """ This randomly selects one of the remaining spots"""
        a = int(random.random()*3)
        b = int(random.random()*3)
        if state[b][a] == ' ':
            return self.letters[a] + self.numbers[b]

        # Only called if the number generator picks a spot that is already full
        return self.turn(state)

    def manual(self, state, turn):
        strategy = self.thinking(state, turn)
        if strategy:
            return strategy
        a = int(random.random()*3)
        b = int(random.random()*3)
        if state[b][a] == ' ':
            return self.letters[a] + self.numbers[b]

        # Only called if the number generator picks a spot that is already full
        return self.turn(state, turn)


    def Monte(self, state, turn):
        '''This is where the real fun will begin.  All other 'computer' components are NOT AI, this is where the fun will begin'''
        return self.manual(state, turn)


    def thinking(self, state, turn):
        '''This checks for places where the opponent has two pieces taken in a row and places in the third spot if available'''

        # This is for checking diagonally
        if state[0][0]==state[1][1]:
           if state[2][2] == ' ':
               return self.letters[2] + self.numbers[2]
        if state[1][1]==state[2][2]:
           if state[0][0] == ' ':
               return self.letters[0] + self.numbers[0]
        if state[2][2] == state[0][0]:
           if state[1][1] == ' ':
               return self.letters[1] + self.numbers[1]

        if state[0][2]==state[1][1]:
           if state[2][0] == ' ':
               return self.letters[0] + self.numbers[2]
        if state[0][2]==state[2][0]:
           if state[1][1] == ' ':
                return self.letters[1] + self.numbers[1]
        if state[1][1]==state[2][0]:
           if state[0][2] == ' ':
                return self.letters[2] + self.numbers[0]
        print '{}\'s turn'.format(turn)

        # Check for the win first
        for turn in range(2):

            # This is the horizontal checker
            X = O = 0
            for i in range(3):
                for j in range(3):
                    if state[i][j] == 'X' and turn == 1:
                        X += 1
                    if state[i][j] == 'O' and turn == 0:
                        O += 1
                if X == 2 or O == 2:
                    for j in range(3):
                        if state[i][j] == ' ':
                            return self.letters[j] + self.numbers[i]
                else:
                    X = O = 0

            # This is the vertical checker
            for j in range(3):
                for i in range(3):
                    if state[i][j] == 'X' and turn == 1:
                        X += 1
                    if state[i][j] == 'O' and turn == 0:
                        O += 1
                if X == 2 or O == 2:
                    for i in range(3):
                        if state[i][j] == ' ':
                            return self.letters[j] + self.numbers[i]
                else:
                    X = O = 0

        return None


if __name__ == "__main__":
    tic_tac = Game()
    tic_tac.play()

