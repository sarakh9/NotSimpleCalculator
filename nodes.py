class NumberNode:
    def __init__(self, token):
        self.token = token
        # self.number = token.value
    
    def __repr__(self):
        return f'{self.token}'

class BinopNode:
    def __init__(self, token, left_child, right_chield):
        self.op = token
        # self.op = token.value
        self.left_child = left_child
        self.right_chield = right_chield
    
    def __repr__(self):
        return f"({self.left_child}, {self.op}, {self.right_chield})"
