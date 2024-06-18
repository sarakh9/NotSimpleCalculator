from nodes import NumberNode, BinopNode

################################################################################################################
# Interpreter
################################################################################################################

class Calculate:
    def __init__(self, value):
        self.value = value
    
    def add_to(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value + operand.value)
    def sub_by(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value - operand.value)
    def mult_by(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value * operand.value)
    def div_by(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value / operand.value)

class Intrpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit)
        return method(node)
    
    def no_visit(self, node):
        raise Exception(f"No method visit_{type(node).__name__} found!")
    
    def visit_NumberNode(self, node):
        print(f"found number node {node.token.value}")
    
    def visit_BinopNode(self, node):
        print(f"found binop node {node.op.value}")
        self.visit(node.left_child)
        self.visit(node.right_chield)
    
    
        
