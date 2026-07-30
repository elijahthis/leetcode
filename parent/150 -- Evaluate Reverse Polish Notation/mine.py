class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Time: O(n)
        # Space: O(n)
        def apply(op, op1, op2):
            match op:
                case "*":
                    return op1 * op2
                case "/":
                    return int(op1 / op2)
                case "+":
                    return op1 + op2
                case "-":
                    return op1 - op2
                case _:
                    return 0
        
        operators = {"*", "+", "/", "-"}
        stack = []
        for item in tokens:
            if item in operators:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(apply(item, op1, op2))
            else:
                stack.append(int(item))
        
        return stack.pop()