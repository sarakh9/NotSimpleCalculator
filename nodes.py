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
    def __init__(self, token, left_child, right_chield):
        self.op = token
        self.left_child = left_child
        self.right_chield = right_chield
    
    def __repr__(self):
        return f"({self.left_child}, {self.op}, {self.right_chield})"
