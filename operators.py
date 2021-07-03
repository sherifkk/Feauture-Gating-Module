
class OrOperator:
    def __init__(self):
        self.precedence = 1
        self.operandsCount = 2
    
    def execute(self, operands):
        if(not isinstance(operands[0], bool) or not isinstance(operands[1], bool)):
            raise ValueError("Invalid Operand type for ||")
        else:
            return(operands[0] or operands[1])

class AndOperator:
    def __init__(self):
        self.precedence = 2
        self.operandsCount = 2
    
    def execute(self, operands):
        if(not isinstance(operands[0], bool) or not isinstance(operands[1], bool)):
            raise ValueError("Invalid Operand type for &&")
        else:
            return(operands[0] and operands[1])

class NotOperator:
    def __init__(self):
        self.precedence = 3
        self.operandsCount = 1
    
    def execute(self, operands):
        if(not isinstance(operands[0], bool)):
            raise ValueError("Invalid Operand type for !")
        else:
            return(operands[0] and operands[1])

class EqualOperator:
    def __init__(self):
        self.precedence = 4
        self.operandsCount = 2
    
    def execute(self, operands):
        return(operands[0] == operands[1])

class NotEqualOperator:
    def __init__(self):
        self.precedence = 4
        self.operandsCount = 2
    
    def execute(self, operands):
        return(operands[0] != operands[1])

class GreaterThanOperator:
    def __init__(self):
        self.precedence = 4
        self.operandsCount = 2
    
    def execute(self, operands):
        return(operands[0] > operands[1])

class GreaterThanEqualOperator:
    def __init__(self):
        self.precedence = 4
        self.operandsCount = 2
    
    def execute(self, operands):
        return(operands[0] >= operands[1])

class LessThanOperator:
    def __init__(self):
        self.precedence = 4
        self.operandsCount = 2
    
    def execute(self, operands):
        return(operands[0] < operands[1])

class LessThanEqualOperator:
    def __init__(self):
        self.precedence = 4
        self.operandsCount = 2
    
    def execute(self, operands):
        return(operands[0] <= operands[1])

class BetweenOperator:
    def __init__(self):
        self.precedence = 4
        self.operandsCount = 3
    
    def execute(self, operands):
        return(operands[0] <= operands[1] and operands[0] >= operands[3])

class AllOfOperator:
    def __init__(self):
        self.precedence = 5
        self.operandsCount = 3
    
    def execute(self, operands):
        if(not isinstance(operands[0], bool) or not isinstance(operands[1], bool) or not isinstance(operands[3], bool)):
            raise ValueError("Invalid Operand type for allof")
        else:
            return(operands[0] and operands[1] and operands[3])

class NoneOfOperator:
    def __init__(self):
        self.precedence = 5
        self.operandsCount = 3
    
    def execute(self, operands):
        if(not isinstance(operands[0], bool) or not isinstance(operands[1], bool) or not isinstance(operands[3], bool)):
            raise ValueError("Invalid Operand type for noneof")
        else:
            return(not operands[0] and not operands[1] and not operands[3])

class Operators:
    def getOperator(token):
        operators = {
            "||" : OrOperator(),
            "&&" : AndOperator(),
            "!" : NotOperator(),
            "==" : EqualOperator(),
            "!=" : NotEqualOperator(),
            ">" : GreaterThanOperator(),
            ">=" : GreaterThanEqualOperator(),
            "<" : LessThanOperator(),
            "<=" : LessThanEqualOperator(),
            "between" : BetweenOperator(),
            "allof" : AllOfOperator(),
            "noneOf" : NoneOfOperator(),
        }
        return(operators.get(token))