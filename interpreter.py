import math
from nodes import NumberNode, BinopNode
from errors import RunTimeError, Position
# from main import treee
################################################################################################################
# Interpreter
################################################################################################################

class RunTimeResult():
    def __init__(self) -> None:
        self.error = None
        self.value = None
    
    def register(self, result):
        if isinstance(result, RunTimeResult):
            if result.error: self.error = result.error
            return result.value

    def succes(self, value):
        self.value = value
        return self

    def fail(self, error):
        self.error = error
        return self

class Calculate:
    def __init__(self, value, pos):
        self.value = value
        self.pos = pos
    
    def add_to(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value + operand.value, self.pos), None
    def sub_by(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value - operand.value, self.pos), None
    def mult_by(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value * operand.value, self.pos), None
    def div_by(self, operand):
        if isinstance(operand, Calculate):
            if operand.value == 0:
                return None, RunTimeError(self.pos,"Division by zero")
            return Calculate(self.value / operand.value, self.pos), None

class Intrpreter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.pos = Position(self.file_name, 0, '')

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit)
        return method(node)
    
    def no_visit(self, node):
        raise Exception(f"No method visit_{type(node).__name__} found!")
    
    def visit_NumberNode(self, node):
        rtr = RunTimeResult()
        return rtr.succes(Calculate(node.token.value, self.pos))
    
    def visit_BinopNode(self, node):
        rtr = RunTimeResult()
        left = rtr.register(self.visit(node.left_child))
        if rtr.error : return rtr
        right = rtr.register(self.visit(node.right_child))
        if rtr.error : return rtr
        match node.op.value:
            case '+':
                result, error =  left.add_to(right)
            case '-':
                result, error = left.sub_by(right)
            case '*':
                result, error = left.mult_by(right)
            case '/':
                result, error = left.div_by(right)
        if error: 
            return rtr.fail(error)
        return rtr.succes(result)
    # gives me the parse tree
    def treee(self, tree):
        child = ""
        er = None
        res = -math.inf
        if type(tree).__name__ == "BinopNode":
            if type(tree.left_child).__name__ == "NumberNode":
                child = f"({tree.left_child.token.value} <- [{tree.op.value}] ->"
                left = Calculate(tree.left_child.token.value, self.pos)
            elif type(tree.left_child).__name__ == "BinopNode":
                l_child ,left = self.treee(tree.left_child)
                child = child + f'({l_child} <- [{tree.op.value}] ->'
            if type(tree.right_child).__name__ == "NumberNode":
                child = child + f'{tree.right_child.token.value})'
                right = Calculate(tree.right_child.token.value, self.pos)
            elif type(tree.right_child).__name__ == "BinopNode":
                r_child ,right = self.treee(tree.right_child)
                child = child + f'{r_child})'
            if tree.op.value == '-':
                res , er = left.sub_by(right)
            elif tree.op.value == '/':
                res , er = left.div_by(right)
            print(child)
            if er:
                print(er.as_string())
                return er
            if res == -math.inf:
                return f"nothing", res
            return f"<{child} = {res.value}>" , res

    
        
