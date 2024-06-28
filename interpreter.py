import math
from tokens import TokenType
from errors import RunTimeError, Position
from symbol_table import SymbolTable
# from main import treee
################################################################################################################
# Interpreter
################################################################################################################

class RunTimeResult():
    def __init__(self) -> None:
        self.error = None
        self.value = None
        self.list_of_results = []
    
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
    def pow_by(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value ** operand.value, self.pos), None
    def div_by(self, operand):
        if isinstance(operand, Calculate):
            if operand.value == 0:
                return None, RunTimeError(self.pos,"Division by zero")
            return Calculate(self.value / operand.value, self.pos), None
    def less_than(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value < operand.value, self.pos), None
    def less_equal(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value <= operand.value, self.pos), None
    def great_than(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value > operand.value, self.pos), None
    def great_equal(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value >= operand.value, self.pos), None
    def equal(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value == operand.value, self.pos), None
    def not_equal(self, operand):
        if isinstance(operand, Calculate):
            return Calculate(self.value != operand.value, self.pos), None
    def not_(self):
        return Calculate(not self.value, self.pos), None
    def __repr__(self):
        return str(self.value)

class Interpreter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.pos = Position(self.file_name, 0, '')
        self.symbol_table = SymbolTable()

    def visit(self, node):
        rtr = RunTimeResult()
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit)
        m = method(node)
        if isinstance(m, Calculate):
            rtr.list_of_results.append(m)
        return m
    
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
                try:
                    result, error =  left.add_to(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '-':
                try:
                    result, error = left.sub_by(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '*':
                try:
                    result, error = left.mult_by(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '/':
                try:
                    result, error = left.div_by(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '^':
                try:
                    result, error = left.pow_by(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '<':
                try:
                    result, error = left.less_than(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '<=':
                try:
                    result, error = left.less_equal(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '>':
                try:
                    result, error = left.great_than(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '>=':
                try:
                    result, error = left.great_equal(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '==':
                try:
                    result, error = left.equal(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
            case '!=':
                try:
                    result, error = left.not_equal(right)
                except Exception:
                    return rtr.fail(RunTimeError(self.pos, f"atleast one of the entries is not a number!"))
        if error: 
            return rtr.fail(error)
        return rtr.succes(result)
    
    def visit_UnaryopNode(self, node):
        rtr = RunTimeResult()
        left = rtr.register(self.visit(node.operand))
        if rtr.error : return rtr
        if node.op.type == TokenType.NOT:
            result, error = left.not_()
        if error: 
            return rtr.fail(error)
        return rtr.succes(result)
    
    def visit_IdNode(self, node):
        rtr = RunTimeResult()
        value = self.symbol_table.get(node.token.value)
        if value is None:
            return rtr.fail(RunTimeError(self.pos, f"'{node.token.value}' is not defined"))
        return rtr.succes(value)
    
    def visit_AssignNode(self, node):
        rtr = RunTimeResult()
        value = rtr.register(self.visit(node.right_child))
        if rtr.error: return rtr
        self.symbol_table.set(node.left_child.token.value, value)
        return rtr.succes(value)
    
    def visit_IfNode(self, node):
        rtr = RunTimeResult()
        condition = rtr.register(self.visit(node.condition))
        if rtr.error: return rtr
        if condition.value:
            result =  rtr.register(self.visit(node.true_body))
        elif node.false_body:
            result =  rtr.register(self.visit(node.false_body))
        elif not (condition.value and node.false_body):
            return False
        else :
            return rtr.fail(RunTimeError(self.pos, f" if statement is not correct"))
        return rtr.succes(result)

    # def visit_WhileNode(self, node):
    #     rtr = RunTimeResult()
    #     while rtr.register(self.visit(node.condition)):
    #         result = rtr.register(self.visit(node.body))
    #         if rtr.error : return rtr
    #         if result: return rtr.succes(result)
    #     return rtr.fail(RunTimeError(self.pos, f" while statement is not correct"))

    # def visit_WhileNode(self, node):
    #     rtr = RunTimeResult()
    #     result = None
        
    #     while True:
    #         condition = rtr.register(self.visit(node.condition))
    #         if rtr.error: return rtr
    #         if not condition.value:
    #             break
            
    #         result = rtr.register(self.visit(node.body))
    #         if rtr.error: return rtr
        
    #     return rtr.succes(result)

    def visit_ForNode(self, node):
        rtr = RunTimeResult()
        result = None  # Initialize the result variable
        start_value = rtr.register(self.visit(node.start_value))
        if rtr.error: return rtr
        end_value = rtr.register(self.visit(node.end_value))
        if rtr.error: return rtr
        if start_value.value <= end_value.value:
            range_values = range(start_value.value, end_value.value + 1)
        else:
            range_values = range(start_value.value, end_value.value - 1, -1)
        for i in range_values:
            self.symbol_table.set(node.var_name.token.value, Calculate(i, self.pos))
            result = rtr.register(self.visit(node.body))
            if rtr.error: return rtr
        return rtr.succes(result)


    # def visit_LoopNode(self, node):
    #     rtr = RunTimeResult()
    #     loop_count =rtr.register(self.visit(node.count))
    #     if rtr.error : return rtr
    #     for i in range(1, loop_count.value + 1):
    #         self.symbol_table[node.var_name.token] = Calculate(i, self.pos)
    #         result = rtr.register(self.visit(node.body))
    #         if rtr.error : return rtr
    #         if result: return rtr.succes(result)
    #     return rtr.fail(RunTimeError(self.pos, f" loop statement is not correct"))

    def visit_PrintNode(self, node):
        rtr = RunTimeResult()
        if node.value and node.identifier:
            identifier_value = self.symbol_table.get(node.identifier.token.value)
            if identifier_value:
                print(f"{node.value} {identifier_value.value}")
                return None
            else:
                print(f"{node.value} undefined")
                return None
        elif node.identifier:
            identifier_value = self.symbol_table.get(node.identifier.token.value)
            if identifier_value:
                print(identifier_value.value)
                return None
            else:
                # print("undefined")
                return None
        return None
    
    def visit_StringNode(self, node):
        rtr = RunTimeResult()
        return rtr.succes(Calculate(node.value, self.pos).value.value)
    
    def visit_StatementsNode(self, node):
        rtr = RunTimeResult()
        for statement in node.statements:
            result = rtr.register(self.visit(statement))
            if rtr.error: return rtr
        return rtr.succes(result)
    
    def visit_ProgramNode(self, node):
        rtr = RunTimeResult()
        result = rtr.register(self.visit(node.value))
        if rtr.error: return rtr
        return result
    
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

    
        
