# Testin and Running Interpreter

from lexer import Lexer, IllegalCharacterError
from parser_ import Parser
# from interpreter import Intrpreter
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