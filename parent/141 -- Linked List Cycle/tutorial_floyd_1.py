class Solution:
    def isHappy(self, n: int) -> bool:
        # Floyd's cycle detection algo. Most straightforward
        def get_next(x: int) -> int:
            total = 0
            while x:
                digit = x%10
                total += (digit * digit)
                x //= 10
            return total
        
        slow = fast = n
        while fast != 1 and get_next(fast) != 1:
            slow, fast = get_next(slow), get_next(get_next(fast))
            if slow == fast:
                return False
        return True