from enum import Enum
from dataclasses import dataclass

# token type + id
class TokenType(Enum):
    NUMBER        = 0
    IDENTIFIER    = 1
    STRINGLITERAL = 2
    BINOP         = 3
    WHILE         = 4
    LOOP          = 5
    BEGIN         = 6
    END           = 7
    FOR           = 8
    OF            = 9
    TO            = 10
    DO            = 11
    PRINT         = 12
    IF            = 13
    THEN          = 14
    ELSE          = 15
    ASSIGN        = 16
    COLON         = 17
    SEMICOLON     = 18
    COMMA         = 19
    NOT           = 20
    OPAREN        = 21
    CPAREN        = 22
    EOF           = 23

@dataclass
class Token:
    type : TokenType
    value : any = None

    # debug helper:
    def __repr__(self):
        return "<" + self.type.name + (f", {self.value}>" if self.value != None else  ">")