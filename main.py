# Simple Math Interpreter
# This is my first project that i am practicing typing and git at the same time.
# plus i am learning how to create interpreter!

from lexer import Lexer, IllegalCharacterError
from parser_ import Parser

while True:
    try:
        text = input("input: ")
    except EOFError:
        print("EOFError")
        break
    lexer = Lexer("testing.sk",text)
    tokens, error = lexer.generate_token()
    parser = Parser("testing.sk",tokens)
    tree = parser.parse()
    if error or tree.error:
        print(tree.error.as_string())
        break
    else:
        print(list(tokens))
        print(tree.node)