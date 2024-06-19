# Testin and Running Interpreter

from lexer import Lexer, IllegalCharacterError
from parser_ import Parser
from interpreter import Intrpreter

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
        print("lexer succes!")
        print(list(tokens))
        parser = Parser("testing.sk",tokens)
        tree = parser.parse()
    if tree.error:
        print(tree.error.as_string())
        break
    else:
        print("parser succes!")
        print(tree.node)
        interpreter = Intrpreter("testing.sk")
        res = interpreter.visit(tree.node)
    if res.error:
        print(res.error.as_string())
        break
    else:
        print("run succes!")
        print(f"result: {res.value.value}")