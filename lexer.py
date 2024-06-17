import re
from tokens import Token, TokenType
from token_regex import KEY_FIRST_LETTER as kfl
from token_regex import *
from errors import IllegalCharacterError, Position


class Lexer:
    def __init__(self,file_name, lexim):
        self.pos = Position(file_name, -1, '')
        self.lexim = iter(lexim)
        self.advance()

    # iterates to next char
    def advance(self):
        try:
            self.current_char = next(self.lexim)
        except StopIteration:
            self.current_char = None
    
    def generate_token(self):
        tokens=[]
        self.pos.line = 0
        while self.current_char != None :
            if re.search(IDENTIFIER,self.current_char):
                tokens.append(self.id_token(0))
            elif re.search(WHITESPACE,self.current_char):
                if re.search("\\n",self.current_char):
                    self.pos.line = self.pos.line + 1
                    self.pos.line_context = ''
                self.advance()
            elif re.search(NUMBER,self.current_char):
                tokens.append(self.number_token(0))
            elif re.search(BINOP,self.current_char):
                tokens.append(self.binop_token(0))
            elif re.search("\"",self.current_char):
                tokens.append(self.string_token(0))
            elif re.search(ASSIGN,self.current_char):
                tokens.append(self.assign_eq_token(0))
            elif re.search(COLON,self.current_char):
                self.advance()
                tokens.append(Token(TokenType.COLON))
            elif re.search(SEMICOLON,self.current_char):
                self.advance()
                tokens.append(Token(TokenType.SEMICOLON))
            elif re.search(COMMA,self.current_char):
                self.advance()
                tokens.append(Token(TokenType.COMMA))
            elif re.search(NOT,self.current_char):
                tokens.append(self.not_nq_token(0))
            elif re.search(OPAREN,self.current_char):
                self.advance()
                tokens.append(Token(TokenType.OPAREN))
            elif re.search(CPAREN,self.current_char):
                self.advance()
                tokens.append(Token(TokenType.CPAREN))
            else :
                error_char = self.current_char
                while self.current_char != None and re.search("[^\\n]",self.current_char):
                    self.pos.line_context = self.pos.line_context + self.current_char
                    self.advance()
                return [] , IllegalCharacterError(self.pos, error_char)
        return tokens, None
    
    def key_token(self, state):
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
                    else : 
                        flag = 0
                        break
                # while
                case 1:
                    if self.current_char == 'h':
                        key = key + self.current_char
                        state = 2
                        self.advance()
                    else : state = -1
                case 2:
                    if self.current_char == 'i':
                        key = key + self.current_char
                        state = 3
                        self.advance()
                    else : state = -1
                case 3:
                    if self.current_char == 'l':
                        key = key + self.current_char
                        state = 4
                        self.advance()
                    else : state = -1
                case 4:
                    if self.current_char == 'e':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                # loop
                case 5:
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 6
                        self.advance()
                    else : state = -1
                case 6:
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 7
                        self.advance()
                    else : state = -1
                case 7:
                    if self.current_char == 'p':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                # begin
                case 8:
                    if self.current_char == 'e':
                        key = key + self.current_char
                        state = 9
                        self.advance()
                    else : state = -1
                case 9:
                    if self.current_char == 'g':
                        key = key + self.current_char
                        state = 10
                        self.advance()
                    else : state = -1
                case 10:
                    if self.current_char == 'i':
                        key = key + self.current_char
                        state = 11
                        self.advance()
                    else : state = -1
                case 11:
                    if self.current_char == 'n':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                # end/else
                case 12:
                    if self.current_char == 'n':
                        key = key + self.current_char
                        state = 13
                        self.advance()
                    elif self.current_char == 'l':
                        key = key + self.current_char
                        state = 14
                        self.advance()
                    else : state = -1
                case 13:
                    if self.current_char == 'd':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                case 14:
                    if self.current_char == 's':
                        key = key + self.current_char
                        state = 15
                        self.advance()
                    else : state = -1
                case 15:
                    if self.current_char == 'e':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                # for
                case 16:
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 17
                        self.advance()
                    else : state = -1
                case 17:
                    if self.current_char == 'r':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                # of
                case 18:
                    if self.current_char == 'f':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                # to/then
                case 19:
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    elif self.current_char == 'h':
                        key = key + self.current_char
                        state = 20
                        self.advance()
                    else : state = -1
                case 20:
                    if self.current_char == 'e':
                        key = key + self.current_char
                        state = 21
                        self.advance()
                    else : state = -1
                case 21:
                    if self.current_char == 'n':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                # do
                case 22 :
                    if self.current_char == 'o':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                # print
                case 23:
                    if self.current_char == 'r':
                        key = key + self.current_char
                        state = 24
                        self.advance()
                    else : state = -1
                case 24:
                    if self.current_char == 'i':
                        key = key + self.current_char
                        state = 25
                        self.advance()
                    else : state = -1
                case 25:
                    if self.current_char == 'n':
                        key = key + self.current_char
                        state = 26
                        self.advance()
                    else : state = -1
                case 26:
                    if self.current_char == 't':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                # if
                case 27:
                    if self.current_char == 'f':
                        key = key + self.current_char
                        state = 28
                        flag = 1
                        self.advance()
                    else : state = -1
                case 28 :
                    if re.search("[^a-zA-Z \\t\\n\\r]",self.current_char):
                        flag = 0
                        break
                    flag = 1
                    break
                case -1:
                    flag = 0
                    break
        # check the key       
        if flag == 0 :
            return 0, key
        elif flag == 1 :
            while self.current_char != None:
                if re.search("[^a-zA-Z \\t\\n\\r]",self.current_char):
                    return 0, key
                elif re.search("[a-zA-Z]",self.current_char):
                    key = key + self.current_char
                    self.advance()
                elif re.search(WHITESPACE,self.current_char):
                    break
            self.pos.line_context = self.pos.line_context + key
            for t in KEY_LIST :
                if re.search(t[0],key) :
                    return Token(t[1]), key
            return 0, key

    def number_token(self, state):
        number = ''
        flag = 0
        dc_point = 0
        while self.current_char != None:
            match state:
                case 0:
                    if re.search("[0-9]",self.current_char):
                        number = number + self.current_char
                        state = 1
                        flag = 1
                        self.advance()
                case 1:
                    if re.search("[0-9]",self.current_char):
                        number = number + self.current_char
                        state = 1
                        self.advance()
                        flag = 1
                    elif self.current_char == '.':
                        number = number + self.current_char
                        state = 2
                        self.advance()
                        flag = 0
                        dc_point = 1
                    elif re.search("[^0-9]",self.current_char):
                        state = 3
                        flag = 1
                case 2:
                    if re.search("[0-9]",self.current_char):
                        number = number + self.current_char
                        state = 2
                        self.advance()
                        flag = 1
                    elif re.search("[^0-9]",self.current_char):
                        state = 3
                case 3:
                    if re.search("[^0-9 \t\r\n]",self.current_char):
                        break
                    flag = 1
                    break
        # check the number       
        if flag == 0 :
            self.pos.line_context = self.pos.line_context + number
            return
        elif flag == 1 :
            if dc_point:
                self.pos.line_context = self.pos.line_context + number
                return Token(TokenType.NUMBER,float(number))
            else:
                return Token(TokenType.NUMBER,int(number))
            
    def id_token(self, state):
        word = ''
        key = 0
        key,word = self.key_token(state)
        w = iter(word)
        try:
            char = next(w)
        except StopIteration:
            char = None
        if key != None and key != 0:
            return key
        else:
            id = ''
            flag = 0
            while char != None:
                match state:
                    case 0:
                        if re.search("[a-zA-Z]", char):
                            id = id + char
                            try:
                                char = next(w)
                            except StopIteration:
                                char = None
                            state = 1
                            flag = 1
                        else: 
                            flag = 0
                    case 1:
                        if re.search("[a-zA-Z]|[0-9]|_", char):
                            id = id + char
                            try:
                                char = next(w)
                            except StopIteration:
                                char = None
                            state = 1
                            flag = 1
                        else: state = 2
                    case 2:
                        flag = 1
            while self.current_char != None:
                match state:
                    case 0:
                        if re.search("[a-zA-Z]", self.current_char):
                            id = id + self.current_char
                            self.advance()
                            state = 1
                            flag = 1
                        else: 
                            flag = 0
                    case 1:
                        if re.search("[a-zA-Z]|[0-9]|_", self.current_char):
                            id = id + self.current_char
                            self.advance()
                            state = 1
                            flag = 1
                        else: state = 2
                    case 2:
                        flag = 1
            if flag == 0 :
                return
            elif flag == 1:
                self.pos.line_context = self.pos.line_context + id
                return Token(TokenType.IDENTIFIER, id)
         
    def binop_token(self, state):
        op = ''
        flag = 0
        while self.current_char != None:
            match state:
                case 0:
                    if re.search("[+]|-|[*]|/|\^", self.current_char):
                        op = op + self.current_char
                        self.advance()
                        flag = 1
                        state = 2
                    elif re.search("<|>", self.current_char):
                        op = op + self.current_char
                        self.advance()
                        flag = 1
                        state = 1
                    elif re.search("=|!", self.current_char):
                        op = op + self.current_char
                        self.advance()
                        flag = 0
                        state = 1
                    else :
                        flag = 0
                        break
                case 1:
                    if re.search("=", self.current_char):
                        op = op + self.current_char
                        flag = 1
                        self.advance()
                        state = 2
                    elif re.search("[^=]", self.current_char):
                        break
                case 2:
                    flag = 1
                    break
        if flag == 0:
            return
        elif flag == 1:
            self.pos.line_context = self.pos.line_context + op
            return Token(TokenType.BINOP, op)

    def string_token(self, state):
        flag = 0
        while self.current_char != None:
            match state:
                case 0:
                    if re.search("\"", self.current_char):
                        self.pos.line_context = self.pos.line_context + self.current_char
                        self.advance()
                        state = 1
                case 1:
                    if re.search("\"", self.current_char):
                        self.pos.line_context = self.pos.line_context + self.current_char
                        flag = 1
                        state = 2
                        self.advance()    
                    else:
                        self.pos.line_context = self.pos.line_context + self.current_char
                        self.advance()  
                case 2:
                    flag = 1
                    break 
        if flag == 0:
            return
        elif flag == 1:
            return Token(TokenType.STRINGLITERAL)

    def assign_eq_token(self, state):
        flag = 0
        while self.current_char != None:
            match state:
                case 0:
                    if re.search(ASSIGN, self.current_char):
                        flag = 1
                        state = 1
                        self.advance()
                case 1:
                    if re.search(ASSIGN, self.current_char):
                        flag = 2
                        state = 2
                        self.advance()
                    else:
                        state = 3
                case 2 :
                    state = 3
                case 3:
                    break
        if flag == 0:
            return
        elif flag == 1:
            self.pos.line_context = self.pos.line_context + "="
            return Token(TokenType.ASSIGN)
        elif flag == 2:
            self.pos.line_context = self.pos.line_context + "=="
            return Token(TokenType.BINOP, "==")

    def not_nq_token(self, state):
        flag = 0
        while self.current_char != None:
            match state:
                case 0:
                    if re.search(NOT, self.current_char):
                        flag = 1
                        state = 1
                        self.advance()
                case 1:
                    if re.search(ASSIGN, self.current_char):
                        flag = 2
                        state = 2
                        self.advance()
                    else:
                        state = 3
                case 2 :
                    state = 3
                case 3:
                    break
        if flag == 0:
            return
        elif flag == 1:
            self.pos.line_context = self.pos.line_context + "!"
            return Token(TokenType.NOT)
        elif flag == 2:
            self.pos.line_context = self.pos.line_context + "!="
            return Token(TokenType.BINOP, "!=")