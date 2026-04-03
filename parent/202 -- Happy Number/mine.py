class Solution:
    def isHappy(self, n: int) -> bool:
        # works, but not the right approach. see why below
        # confusing use of total, makes it hard to reason about correctness
        dividend = n
        total = 0

        while True:
            # do stuff
            while dividend:
                total += ((dividend%10)*(dividend%10))
                dividend = dividend//10

            # This is a hack, not a correct condition
            if total < 7:
                break
            
            dividend = total
            total = 0
            
        return total == 1