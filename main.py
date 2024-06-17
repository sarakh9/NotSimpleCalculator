# Simple Math Interpreter
# This is my first project that i am practicing typing and git at the same time.
# plus i am learning how to create interpreter!

from lexer import Lexer, IllegalCharacterError

while True:
    try:
        text = input("input: ")
    except EOFError:
        print("EOFError")
        break
    lexer = Lexer("testing.sk",text)
    token, error = lexer.generate_token()
    if error:
        print(error.as_string())
        break
    else:
        print(list(token))