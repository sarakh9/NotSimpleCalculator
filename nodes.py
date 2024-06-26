#################################################################################################################
# DIAGRAM NODE
#################################################################################################################

# NUMBERS
class NumberNode:
    def __init__(self, token):
        self.token = token
    
    def __repr__(self):
        return f'{self.token}'

# BINARY OPERATORS
class BinopNode:
    def __init__(self, token, left_child, right_child):
        self.op = token
        self.left_child = left_child
        self.right_child = right_child
    
    def __repr__(self):
        return f"({self.left_child}, {self.op}, {self.right_child})"

class UnaryopNode:
    def __init__(self, token, operand):
        self.op = token
        self.operand = operand
    def __repr__(self):
        return f"({self.op}, {self.operand})"


class IdNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'
    
class AssignNode:
    def __init__(self, token, left_child, right_child):
        self.op = token
        self.left_child = left_child
        self.right_child = right_child
    def __repr__(self):
        return f"({self.left_child}, {self.op}, {self.right_child})"