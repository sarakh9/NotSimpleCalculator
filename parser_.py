from tokens import TokenType
from nodes import NumberNode, BinopNode
from errors import Position

class Parser:
    def __init__(self, file_name, tokens):
        self.file_name = file_name
        self.tokens = tokens
        self.token_index = -1
        self.pos = Position(self.file_name, -1, '')
        self.tree = ''
        self.advance()
        self.pos.line = 0
        self.token_index = 0
    def advance(self):
        try:
            self.token_index = self.token_index +1
            self.current_token = self.tokens[self.token_index]
            return self.current_token
        except:
            return None
    def parse(self):
        tree = self.expr()
        return tree

    def factor(self):
        tok = self.current_token
        if tok.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(tok)

    def term(self):
        left = self.factor()
        while self.current_token.type == TokenType.BINOP and self.current_token.value == "*" or self.current_token.value == "/":
            op_tok = self.current_token
            self.advance()
            right = self.factor()
            left = BinopNode(op_tok, left, right)
        return left

    def expr(self):
        left = self.term()
        while self.current_token.type == TokenType.BINOP and self.current_token.value == "+" or self.current_token.value == "-":
            op_tok = self.current_token
            self.advance()
            right = self.term()
            left = BinopNode(op_tok, left, right)
        return left

