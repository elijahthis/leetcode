class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n open, n closed
        # ((()))
        # starts with "open"
        # "open" must always be >= "closed"
        # can add "open" anytime, as long as "open" < n
        # can only add "closed" if "open" > "closed"

        # Time: O(Cₙ · n)
        # Space: O(Cₙ · n)
        # The recursion ensures only valid states are explored (pruned search)

        stack = []
        result = []

        def backtrack(openN: int, closedN: int):
            if openN == closedN and closedN == n:
               result.append("".join(stack))
               return
            
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            
            if openN > closedN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        
        backtrack(0,0)
        return result
            
