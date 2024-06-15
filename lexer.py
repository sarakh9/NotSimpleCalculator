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
        key = ''
        flag = 0
        while self.current_char != None:
            match state:
                case 0:
                    # while
                    if self.current_char == 'w':
                        key = key + self.current_char
                        state = 1
                        self.advance()
                    # loop
                    elif self.current_char == 'l':
                        key = key + self.current_char
                        state = 5
                        self.advance()
                    # begin
                    elif self.current_char == 'b':
                        key = key + self.current_char
                        state = 8
                        self.advance()
                    # end/else
                    elif self.current_char == 'e':
                        key = key + self.current_char
                        state = 12
                        self.advance()
                    # for
                    elif self.current_char == 'f':
                        key = key + self.current_char
                        state = 16
                        self.advance()
                    # of
                    elif self.current_char == 'o':
                        key = key + self.current_char
                        state = 18
                        self.advance()
                    # to/then
                    elif self.current_char == 't':
                        key = key + self.current_char
                        state = 19
                        self.advance()
                    # do
                    elif self.current_char == 'd':
                        key = key + self.current_char
                        state = 22
                        self.advance()
                    # print
                    elif self.current_char == 'p':
                        key = key + self.current_char
                        state = 23
                        self.advance()
                    # if
                    elif self.current_char == 'i':
                        key = key + self.current_char
                        state = 27
                        self.advance()
                # while
                case 1:
                    if self.current_char == 'h':
                        key = key + self.current_char
                        state = 2
                        self.advance()
                case 2:
                    if self.current_char == 'i':
                        key = key + self.current_char
                        state = 3
                        self.advance()
                case 3:
                    if self.current_char == 'l':
                        key = key + self.current_char
                        state = 4
                        self.advance()
                case 4:
                    if self.current_char == 'e':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                # loop
                case 5:
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 6
                        self.advance()
                case 6:
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 7
                        self.advance()
                case 7:
                    if self.current_char == 'p':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                # begin
                case 8:
                    if self.current_char == 'e':
                        key = key + self.current_char
                        state = 9
                        self.advance()
                case 9:
                    if self.current_char == 'g':
                        key = key + self.current_char
                        state = 10
                        self.advance()
                case 10:
                    if self.current_char == 'i':
                        key = key + self.current_char
                        state = 11
                        self.advance()
                case 11:
                    if self.current_char == 'n':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                # end/else
                case 12:
                    if self.current_char == 'n':
                        key = key + self.current_char
                        state = 13
                        self.advance()
                    elif self.current_char == 'l':
                        key = key + self.current_char
                        state = 14
                        self.advace()
                case 13:
                    if self.current_char == 'd':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                case 14:
                    if self.current_char == 's':
                        key = key + self.current_char
                        state = 15
                        self.advance()
                case 15:
                    if self.current_char == 'e':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                # for
                case 16:
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 17
                        self.advance()
                case 17:
                    if self.current_char == 'r':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                # of
                case 18:
                    if self.current_char == 'f':
                        key = key + self.current_char
                        state = 259
                        self.advance()
                # to/then
                case 19:
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                    elif self.current_char == 'h':
                        key = key + self.current_char
                        state = 20
                        self.advance()
                case 20:
                    if self.current_char == 'e':
                        key = key + self.current_char
                        state = 21
                        self.advance()
                case 21:
                    if self.current_char == 'n':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                # do
                case 22 :
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                # print
                case 23:
                    if self.current_char == 'r':
                        key = key + self.current_char
                        state = 24
                        self.advance()
                case 24:
                    if self.current_char == 'i':
                        key = key + self.current_char
                        state = 25
                        self.advance()
                case 25:
                    if self.current_char == 'n':
                        key = key + self.current_char
                        state = 26
                        self.advance()
                case 26:
                    if self.current_char == 't':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                # if
                case 27:
                    if self.current_char == 'f':
                        key = key + self.current_char
                        state = 28
                        self.advance()
                case 28 :
                    if re.search("[^a-zA-Z \\t\\n\\r]",self.current_char):
                        flag = 0
                        break
                    flag = 1
                    break
                case _:
                    flag = 0  
                    break
        # check the key       
        if flag == 0 :
            return
        elif flag == 1 :
            while self.current_char != None:
                if re.search("[a-zA-Z]",self.current_char):
                    key = key + self.current_char
                    self.advace()
                elif re.search("[ \\t\\n\\r]",self.current_char): 
                        self.advace()
                else :
                    return
            for t in KEY_LIST :
                if re.search(t[0],key) :
                    return Token(t[1])

         

