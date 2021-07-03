from collections import deque
from operators import Operators

class FeatureGating:
    def isAllowed(self, featureName, conditionalExpression, userAttributes):
        self.executePostfix(self.infixToPostfix(conditionalExpression), userAttributes)

    def infixToPostfix(self, conditionalExpression):
        postfix = ""
        stack = deque()
        tokenArray = conditionalExpression.split()
        for token in tokenArray:
            if(token == '('):
                stack.append(token)
            
            elif (token == ')'):
                while(stack and stack[-1] != "("):
                    postfix += stack.pop() + " "
                if(stack and stack[-1] != "("):
                    raise ValueError("Invalid Conditional Expression!")
                else:
                    stack.pop()

            elif(not Operators.getOperator(token)):
                postfix += token + " "
            
            else:
                while(stack and 
                    (Operators.getOperator(token).precedence if Operators.getOperator(token) else -1) <=
                    (Operators.getOperator(stack[-1]).precedence if Operators.getOperator(stack[-1]) else -1)):
                    if(stack[-1] == "("):
                        raise ValueError("Invalid Conditional Expression!")
                    postfix += stack.pop() + " "
                stack.append(token)
        
        while(stack):
            if(stack[-1] == "("):
                raise ValueError("Invalid Conditional Expression!")
            else:
                postfix += stack.pop() + " "

        return(postfix)

    def executePostfix(self, postfix, userAttributes):
        tokenArray = postfix.split()
        stack = deque()
        for token in tokenArray:
            operator = Operators.getOperator(token)
            if(operator):
                operands = []
                operandsCount = operator.operandsCount
                for i in range(operandsCount):
                    operands.append(stack.pop());
                operands.reverse()
                stack.append(operator.execute(operands))
            elif(userAttributes.get(token)):
                stack.append(userAttributes.get(token))
            elif(token == "true"):
                stack.append(True)
            elif(token == "false"):
                stack.append(False)
            else: 
                try:
                    stack.append(int(token))
                except ValueError:
                    try:
                        stack.append(float(token))
                    except ValueError:
                        stack.append(token)

        print(stack.pop())