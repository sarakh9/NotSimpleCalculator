import re
from tokens import TokenType
NUMBER = re.compile("[0-9]+|[0-9]+[.][0-9]+")
WHITESPACE = re.compile(" |\\n|\\t")
IDENTIFIER = re.compile("^[A-Za-z][_|\w]*")
BINOP = re.compile("[+]|-|[*]|/|<|>|<=|>=|==|!=|\^")
STRINGLITERAL = re.compile("^\".*\"$")
WHILE = re.compile("^while$")
LOOP = re.compile("^loop$")
BEGIN = re.compile("^begin$")
END = re.compile("^end$")
FOR = re.compile("^for$")
OF  = re.compile("^of$")
TO = re.compile("^to$")
DO = re.compile("^do$")
PRINT = re.compile("^print$")
IF = re.compile("^if$")
THEN = re.compile("^then$")
ELSE = re.compile("^else$")
ASSIGN = re.compile("=")
COLON = re.compile("^:$")
SEMICOLON = re.compile("^;$")
COMMA = re.compile("^,$")
NOT = re.compile("^!$")
OPAREN = re.compile("^[(]$")
CPAREN = re.compile("^[)]$")
KEY_FIRST_LETTER = ['e','t','i','p','d','o','f','b','l','w']
KEY_LIST = [(WHILE,TokenType.WHILE), (LOOP,TokenType.LOOP), (BEGIN,TokenType.BEGIN),
            (END,TokenType.END), (FOR,TokenType.FOR), (OF,TokenType.OF), (TO,TokenType.TO),
            (DO,TokenType.DO), (PRINT,TokenType.PRINT), (IF,TokenType.IF), (THEN,TokenType.THEN),
            (ELSE,TokenType.ELSE)]