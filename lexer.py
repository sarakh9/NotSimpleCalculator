from tokens import Token, TokenType

class Lexer:
    def __init__(self, lexim):
        self.lexim = iter(lexim)
        self.advance()

    # iterates to next char
    def advace(self):
        try:
            self.current_char = next(self.lexim)
        except StopIteration:
            self.current_char = None
    def generate_token(self):
        pass
