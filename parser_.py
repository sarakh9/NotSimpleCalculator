from tokens import TokenType
from nodes import NumberNode, BinopNode, IdNode, AssignNode, UnaryopNode, IfNode, WhileNode, ForNode, LoopNode, PrintNode, StatementsNode, ProgramNode
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
        tree = self.program()
        if not tree.error and self.current_token.type != TokenType.EOF:
            return tree.fail(InvalidSyntaxError(self.pos, "expected binary operation"))
        return tree

    def power(self):
        res = ParseResult()
        tok = self.current_token
        if tok.type == TokenType.NUMBER:
            res.register(self.advance())
            return res.succes(NumberNode(tok))
        elif tok.type == TokenType.IDENTIFIER:
            id = res.register(self.id())
            if res.error: return res
            return res.succes(id)
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
        while self.current_token.type == TokenType.BINOP and (self.current_token.value == "*" or self.current_token.value == "/"):
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
        while self.current_token.type == TokenType.BINOP and (self.current_token.value == "+" or self.current_token.value == "-"):
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
    
    def comparison(self):
        res = ParseResult()
        valid_op = ["<", ">", "<=", ">=", "==", "!="]
        if self.current_token == '!':
            op_tok = self.current_token
            res.register(self.advance())
            left = res.register(self.comparison())
            if res.error: return res
            return res.succes(UnaryopNode(op_tok, left))
        left = res.register(self.expr())
        if res.error: return res
        while self.current_token.value in valid_op:
            op_tok = self.current_token
            res.register(self.advance())
            right = res.register(self.expr())
            if res.error: return res
            left = BinopNode(op_tok, left, right)
        return res.succes(left)
                    
    def if_expr(self):
        res = ParseResult()
        if self.current_token.type != TokenType.IF:
            return res.fail(InvalidSyntaxError(self.pos, "expected 'if'"))
        res.register(self.advance())
        condition = res.register(self.comparison())
        if res.error: return res
        while self.current_token.type == TokenType.IDENTIFIER or self.current_token.type == TokenType.BINOP or self.current_token.type == TokenType.NUMBER:
            condition = res.register(self.comparison())
            if res.error: return res
        if self.current_token.type == TokenType.THEN:
            res.register(self.advance())
            true_statement = res.register(self.stmt())
            if res.error: return res
            false_statement = None
            if self.current_token.type == TokenType.ELSE:
                res.register(self.advance())
                false_statement = res.register(self.stmt())
                if res.error: return res
            return res.succes(IfNode(condition, true_statement, false_statement))
        else:
            return res.fail(InvalidSyntaxError(self.pos, "expected 'then'"))

    def stmt(self):
        res = ParseResult()
        if self.current_token.type == TokenType.IDENTIFIER:
            left = res.register(self.id())
            if res.error: return res
            if self.current_token.type == TokenType.ASSIGN:
                tok = self.current_token
                res.register(self.advance())
                right = res.register(self.comparison())
                if res.error: return res
                if self.current_token.type == TokenType.SEMICOLON:
                    res.register(self.advance())
                    return res.succes(AssignNode(tok, left, right))
                else:
                    return res.fail(InvalidSyntaxError(self.pos, "expected ';' after assignment"))
            else:
                return res.fail(InvalidSyntaxError(self.pos, "expected assign operator '='"))
        elif self.current_token.type == TokenType.BEGIN:
            res.register(self.advance())
            statements = res.register(self.stmts())
            if res.error: return res
            if self.current_token.type == TokenType.END:
                res.register(self.advance())
                return res.succes(statements)
            else:
                return res.fail(InvalidSyntaxError(self.pos, "expected 'end'"))
        elif self.current_token.type == TokenType.IF:
            if_expr =  res.register(self.if_expr())
            if res.error: return res
            return res.succes(if_expr)
        elif self.current_token.type == TokenType.WHILE:
            res.register(self.advance())
            condition = res.register(self.expr())
            if res.error: return res
            if self.current_token.type == TokenType.DO:
                res.register(self.advance())
                body = res.register(self.stmt())
                if res.error: return res
                return res.succes(WhileNode(condition, body))
            else:
                return res.fail(InvalidSyntaxError(self.pos, "expected 'do'"))
        elif self.current_token.type == TokenType.FOR:
            res.register(self.advance())
            if self.current_token.type == TokenType.IDENTIFIER:
                var_name = res.register(self.id())
                if res.error: return res
                if self.current_token.type == TokenType.OF:
                    res.register(self.advance())
                    start_value = res.register(self.expr())
                    if res.error: return res
                    if self.current_token.type == TokenType.TO:
                        res.register(self.advance())
                        end_value = res.register(self.expr())
                        if res.error: return res
                        if self.current_token.type == TokenType.DO:
                            res.register(self.advance())
                            body = res.register(self.stmt())
                            if res.error: return res
                            return res.succes(ForNode(var_name, start_value, end_value, body))
                        else:
                            return res.fail(InvalidSyntaxError(self.pos, "expected 'do'"))
                    else:
                        return res.fail(InvalidSyntaxError(self.pos, "expected 'to'"))
                else:
                    return res.fail(InvalidSyntaxError(self.pos, "expected 'of'"))
            else:
                return res.fail(InvalidSyntaxError(self.pos, "expected variable name"))
        elif self.current_token.type == TokenType.LOOP:
            res.register(self.advance())
            if self.current_token.type == TokenType.IDENTIFIER:
                var_name = res.register(self.id())
                if res.error: return res
                if self.current_token.type == TokenType.COLON:
                    res.register(self.advance())
                    count = res.register(self.expr())
                    if res.error: return res
                    if self.current_token.type == TokenType.DO:
                        res.register(self.advance())
                        body = res.register(self.stmt())
                        if res.error: return res
                        return res.succes(LoopNode(var_name, count, body))
                    else:
                        return res.fail(InvalidSyntaxError(self.pos, "expected 'do'"))
                else:
                    return res.fail(InvalidSyntaxError(self.pos, "expected ':'"))
            else:
                return res.fail(InvalidSyntaxError(self.pos, "expected variable name"))
        elif self.current_token.type == TokenType.PRINT:
            res.register(self.advance())
            if self.current_token.type == TokenType.IDENTIFIER:
                var_name = res.register(self.id())
                if res.error: return res
                if self.current_token.type == TokenType.SEMICOLON:
                    res.register(self.advance())
                    return res.succes(PrintNode(None, var_name))
                else:
                    return res.fail(InvalidSyntaxError(self.pos, "expected ';'"))
            elif self.current_token.type == TokenType.STRINGLITERAL:
                message = self.current_token.value
                res.register(self.advance())
                if self.current_token.type == TokenType.COMMA:
                    res.register(self.advance())
                    if self.current_token.type == TokenType.IDENTIFIER:
                        var_name = res.register(self.id())
                        if res.error: return res
                        if self.current_token.type == TokenType.SEMICOLON:
                            res.register(self.advance())
                            return res.succes(PrintNode(message, var_name))
                        else:
                            return res.fail(InvalidSyntaxError(self.pos, "expected ';'"))
                    else:
                        return res.fail(InvalidSyntaxError(self.pos, "expected variable name"))
                else:
                    return res.fail(InvalidSyntaxError(self.pos, "expected ','"))
            else:
                return res.fail(InvalidSyntaxError(self.pos, "expected variable name or string literal"))
        elif self.current_token.type == TokenType.ASSIGN:
            return res.fail(InvalidSyntaxError(self.pos, "expected variable name or keyword"))
        else :
            left = res.register(self.comparison())
            if res.error: return res
            if self.current_token.type == TokenType.SEMICOLON:
                res.register(self.advance())
                return res.succes(left)
            else:
                return res.fail(InvalidSyntaxError(self.pos, "expected ';'"))
    def stmts(self):
        res = ParseResult()
        statements = []
        
        while self.current_token.type != TokenType.EOF and self.current_token.type != TokenType.END:
            statement = res.register(self.stmt())
            if res.error: return res
            statements.append(statement)
        return res.succes(StatementsNode(statements))
    def program(self):
        res = ParseResult()
        stmts = res.register(self.stmts())
        g = res.succes(ProgramNode(stmts))
        return g



