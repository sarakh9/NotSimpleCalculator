# Testin and Running Interpreter

from lexer import Lexer, IllegalCharacterError
from parser_ import Parser
from interpreter import Interpreter

from symbol_table import SymbolTable

def print_symbol_table(symbol_table):
    print("Symbol Table:")
    for name, value in symbol_table.symbols.items():
        print(f"{name}: {value}")

def treee(tree):
    if type(tree).__name__ == "NumberNode":
        return tree.token.value
    elif type(tree).__name__ == "BinopNode":
        res = f"[{treee(tree.left_child)}<-({tree.op.value})->{treee(tree.right_child)}]"
        print(res)
        return res

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
        interpreter = Interpreter("testing.sk")
        res = interpreter.visit(tree.node)
        # print(f"main res: {res}")
    # if res != None:
    #     if res.value.error:
    #         print(res.error.as_string())
    #         break
    # else:
    
    if res == None:
        print_symbol_table(interpreter.symbol_table)
        print("?run succes!")
    else:
        print(f">>> {res.value}")
        print_symbol_table(interpreter.symbol_table)
        print("run succes!")
        
