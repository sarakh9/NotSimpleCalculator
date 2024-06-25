from tokens import TokenType
from nodes import NumberNode, BinopNode, IdNode, AssignNode
from errors import Position, InvalidSyntaxError
class ParseResult():
    def __init__(self) -> None:
        self.error = None
        self.node = None
    
    def register(self, result):
        if isinstance(result, ParseResult):
            if result.error: self.error = result.error
            return result.node

    def succes(self, node,):
        self.node = node
        return self

    def fail(self, error):
        self.error = error
        return self


class Parser:
    def __init__(self, file_name, tokens):
        self.file_name = file_name
        self.tokens = tokens
        self.token_index = -1
        self.pos = Position(self.file_name, -1, '')
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
        tree = self.stmt()
        if not tree.error and self.current_token.type != TokenType.EOF:
            return tree.fail(InvalidSyntaxError(self.pos, "expected binary operation"))
        return tree

    def power(self):
        res = ParseResult()
        tok = self.current_token
        if tok.type == TokenType.NUMBER:
            res.register(self.advance())
            return res.succes(NumberNode(tok))
        elif tok.type == TokenType.OPAREN:
            res.register(self.advance())
            expr = res.register(self.expr())
            if res.error: return res
            if self.current_token.type == TokenType.CPAREN:
                res.register(self.advance())
                return res.succes(expr)
            else:
                return res.fail(InvalidSyntaxError(self.pos,"expected cparen"))
        else:
            return res.fail(InvalidSyntaxError(self.pos, "expected int or float."))

    def factor(self):
        res = ParseResult()
        left = res.register(self.power())
        if res.error: return res
        while self.current_token.type == TokenType.BINOP and self.current_token.value == "^":
            op_tok = self.current_token
            res.register(self.advance())
            right = res.register(self.factor())
            if res.error: return res
            left = BinopNode(op_tok, left, right)
        return res.succes(left)
        

    def term(self):
        res = ParseResult()
        left = res.register(self.factor())
        if res.error: return res
        while self.current_token.type == TokenType.BINOP and self.current_token.value == "*" or self.current_token.value == "/":
            op_tok = self.current_token
            res.register(self.advance())
            right = res.register(self.factor())
            if res.error: return res
            left = BinopNode(op_tok, left, right)
        return res.succes(left)

    def expr(self):
        res = ParseResult()
        left = res.register(self.term())
        if res.error: return res
        while self.current_token.type == TokenType.BINOP and self.current_token.value == "+" or self.current_token.value == "-":
            op_tok = self.current_token
            res.register(self.advance())
            right = res.register(self.term())
            if res.error: return res
            left = BinopNode(op_tok, left, right)
        return res.succes(left)
    
    def id(self):
        res = ParseResult()
        tok = self.current_token
        if tok.type == TokenType.IDENTIFIER:
            res.register(self.advance())
            return res.succes(IdNode(tok))
        else:
            return res.fail(InvalidSyntaxError(self.pos, "invalid variable name"))
    
    def stmt(self):
        res = ParseResult()
        if self.current_token.type == TokenType.IDENTIFIER:
            left = res.register(self.id())
            if res.error: return res
            if self.current_token.type == TokenType.ASSIGN:
                tok = self.current_token
                res.register(self.advance())
                right = res.register(self.expr())
                if res.error: return res
                if self.current_token.type == TokenType.SEMICOLON:
                    res.register(self.advance())
                    return res.succes(AssignNode(tok, left, right))
                else:
                    return res.fail(InvalidSyntaxError(self.pos, "expected ';' after assignment"))
            else:
                return res.fail(InvalidSyntaxError(self.pos, "expected assign operator '='"))
        elif self.current_token.type == TokenType.ASSIGN:
            return res.fail(InvalidSyntaxError(self.pos, "expected variable name"))
        else :
            left = res.register(self.expr())
            return res.succes(left)



