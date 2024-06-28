# Testin and Running Interpreter

from lexer import Lexer, IllegalCharacterError
from parser_ import Parser
from interpreter import Interpreter

from symbol_table import SymbolTable

def print_symbol_table(symbol_table):
    print("Symbol Table:")
    for name, value in symbol_table.symbols.items():
        print(f"{name}: {value}")


while True:
    try:
        text = input("input: ")
    except EOFError:
        print("EOFError")
        break
    lexer = Lexer("testing.sk",text)
    tokens, error = lexer.generate_token()
    
    
    if error:
        print(error.as_string())
        break
    else:
        print(f"tokens: {list(tokens)}")
        parser = Parser("testing.sk",tokens)
        tree = parser.parse()
    if tree.error:
        print({tree.error.as_string()})
        break
    else:
        print(f"parse tree: {tree.node}")
    #     interpreter = Interpreter("testing.sk")
    #     res = interpreter.visit(tree.node)
    
    # if res == None:
    #     print("res is none!")
    #     print_symbol_table(interpreter.symbol_table)
    #     print("?run succes!")
    # else:
    #     if res.error: 
    #         print(res.error.as_string())
    #         break
    #     print(f">>> {res}")
    #     print_symbol_table(interpreter.symbol_table)
    #     print("run succes!")
        
