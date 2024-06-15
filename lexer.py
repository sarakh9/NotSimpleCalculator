import re
from tokens import Token, TokenType
from token_regex import KEY_FIRST_LETTER as kfl
from token_regex import *

class Lexer:
    state = 0
    def __init__(self, lexim):
        self.lexim = iter(lexim)
        self.advance()

    # iterates to next char
    def advace(self):
        try:
            self.current_char = next(self.lexim)
        except StopIteration:
            self.current_char = None
    def generate_token(self):
        while self.current_char != None :
            if self.current_char.lower() in kfl:
                pass
            elif re.search(WHITESPACE,self.current_char):
                pass
            elif re.search(NUMBER,self.current_char):
                pass
            elif re.search(IDENTIFIER,self.current_char):
                pass
            elif re.search(BINOP,self.current_char):
                pass
            elif re.search(STRINGLITERAL,self.current_char):
                pass
            elif re.search(ASSIGN,self.current_char):
                pass
            elif re.search(COLON,self.current_char):
                pass
            elif re.search(SEMICOLON,self.current_char):
                pass
            elif re.search(COMMA,self.current_char):
                pass
            elif re.search(NOT,self.current_char):
                pass
            elif re.search(OPAREN,self.current_char):
                pass
            elif re.search(CPAREN,self.current_char):
                pass
    
    def key_token(self):
        while self.current_char != None:
            match state:
                case 0:
                    # while
                    if self.current_char == 'w':
                        state = 1
                        self.advance()
                    # loop
                    elif self.current_char == 'l':
                        state = 6
                        self.advance()
                    # begin
                    elif self.current_char == 'b':
                        state = 10
                        self.advance()
                    # end/else
                    elif self.current_char == 'e':
                        state = 15
                        self.advance()
                    # for
                    elif self.current_char == 'f':
                        state = 21
                        self.advance()
                    # of
                    elif self.current_char == 'o':
                        state = 24
                        self.advance()
                    # to/then
                    elif self.current_char == 't':
                        state = 26
                        self.advance()
                    # do
                    elif self.current_char == 'd':
                        state = 31
                        self.advance()
                    # print
                    elif self.current_char == 'p':
                        state = 33
                        self.advance()
                    # if
                    elif self.current_char == 'i':
                        state = 38
                        self.advance()
                # while
                case 1:
                    if self.current_char == 'h':
                        state = 2
                        self.advance()
                case 2:
                    if self.current_char == 'i':
                        state = 3
                        self.advance()
                case 3:
                    if self.current_char == 'l':
                        state = 4
                        self.advance()
                case 4:
                    if self.current_char == 'e':
                        state = 5
                        self.advance()
                case 5 :
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                # loop
                case 6:
                    if self.current_char == 'o':
                        state = 7
                        self.advance()
                case 7:
                    if self.current_char == 'o':
                        state = 8
                        self.advance()
                case 8:
                    if self.current_char == 'p':
                        state = 9
                        self.advance()
                case 9:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                # begin
                case 10:
                    if self.current_char == 'e':
                        state = 11
                        self.advance()
                case 11:
                    if self.current_char == 'g':
                        state = 12
                        self.advance()
                case 12:
                    if self.current_char == 'i':
                        state = 13
                        self.advance()
                case 13:
                    if self.current_char == 'n':
                        state = 14
                        self.advance()
                case 14:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                # end/else
                case 15:
                    if self.current_char == 'n':
                        state = 16
                        self.advance()
                    elif self.current_char == 'l':
                        state = 18
                case 16:
                    if self.current_char == 'd':
                        state = 17
                        self.advance()
                case 17:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                case 18:
                    if self.current_char == 's':
                        state = 19
                        self.advance()
                case 19:
                    if self.current_char == 'e':
                        state = 20
                        self.advance()
                case 20:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                # for
                case 21:
                    if self.current_char == 'o':
                        state = 22
                        self.advance()
                case 22:
                    if self.current_char == 'r':
                        state = 23
                        self.advance()
                case 23:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                # of
                case 24:
                    if self.current_char == 'f':
                        state = 25
                        self.advance()
                case 25:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                # to/then
                case 26:
                    if self.current_char == 'o':
                        state = 27
                        self.advance()
                    elif self.current_char == 'h':
                        state = 28
                        self.advance()
                case 27:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                case 28:
                    if self.current_char == 'e':
                        state = 29
                        self.advance()
                case 29:
                    if self.current_char == 'n':
                        state = 30
                        self.advance()
                case 30:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                # do
                case 31:
                    if self.current_char == 'o':
                        state = 32
                        self.advance()
                case 32:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                # print
                case 33:
                    if self.current_char == 'r':
                        state = 34
                        self.advance()
                case 34:
                    if self.current_char == 'i':
                        state = 35
                        self.advance()
                case 35:
                    if self.current_char == 'n':
                        state = 36
                        self.advance()
                case 36:
                    if self.current_char == 't':
                        state = 37
                        self.advance()
                case 37:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                # if
                case 38:
                    if self.current_char == 'f':
                        state = 39
                        self.advance()
                case 39:
                    if re.search("[^a-zA-Z]",self.current_char):
                        state = 40
                case 40:
                    pass

