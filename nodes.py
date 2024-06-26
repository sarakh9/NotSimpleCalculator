#################################################################################################################
# DIAGRAM NODE
#################################################################################################################

# NUMBERS
class StatementsNode:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return f"{self.statements}"
class NumberNode:
    def __init__(self, token):
        self.token = token
    
    def __repr__(self):
        return f"{self.token}"

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

class IfNode:
    def __init__(self, condition, true_body, false_body=None):
        self.condition = condition
        self.true_body = true_body
        self.false_body = false_body
    
    def __repr__(self):
        if self.false_body != None:
            return f"(if {self.condition}, then, {self.true_body} else {self.false_body})"
        else:
            return f"(if {self.condition}, then, {self.true_body})"

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
    
    def __repr__(self):
        return f"(while {self.condition} do {self.body})"

class ForNode:
    def __init__(self, var_name, start_value, end_value, body):
        self.var_name = var_name
        self.start_value = start_value
        self.end_value = end_value
        self.body = body
    
    def __repr__(self):
        return f"(for {self.var_name} of {self.start_value} to {self.end_value} do {self.body})"

class LoopNode:
    def __init__(self, var_name, count, body):
        self.var_name = var_name
        self.count = count
        self.body = body
    
    def __repr__(self):
        return f"(loop {self.var_name}:{self.count} do {self.body})"

class PrintNode:
    def __init__(self, value, identifier):
        self.value = value
        self.identifier = identifier
    
    def __repr__(self):
        return f"{self.value}"

class StringNode:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value}"
class ProgramNode:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"{self.value}"
