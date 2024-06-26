# Errors base
class Error:
    def __init__(self, error_name, position, detail):
        self.name_error = error_name
        self.position = position
        self.detail = detail
    def as_string(self):
        error = f"""  File '{self.position.file_name}', in line '{self.position.line}':\n\t'{self.position.line_context}'\n  {self.name_error}: {self.detail}"""
        return error

################################################################################################################
# LEXER ERRORS
################################################################################################################

# Undefined character or illigal character
class IllegalCharacterError(Error):
    def __init__(self ,position, detail):
        super().__init__("EllegalCharacterError", position, detail)

################################################################################################################
# SYNTAX ERROR
################################################################################################################

# Invalid syntax
class InvalidSyntaxError(Error):
    def __init__(self ,position, detail):
        super().__init__("InvalidSyntaxError", position, detail)


################################################################################################################
# RUN TIME ERROR
################################################################################################################

class RunTimeError(Error):
    def __init__(self ,position, detail):
        super().__init__("RunTimeError", position, detail)

################################################################################################################
# POSITION: keeps track of where the error occurred
################################################################################################################

class Position:
    def __init__(self, file_name, line, line_context):
        self.file_name = file_name
        self.line = line
        self.line_context = line_context