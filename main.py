# Simple Math Interpreter
# This is my first project that i am practicing typing and git at the same time.
# plus i am learning how to create interpreter!

from lexer import Lexer

while True:
    text = input("input: ")
    lexer = Lexer(text)
    token = lexer.generate_token()
    print(list(token))