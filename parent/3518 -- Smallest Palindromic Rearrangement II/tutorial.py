from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Convo: 
        # https://share.gemini.google/qpHhcp4YMJRY
        # https://chatgpt.com/share/6a6eb495-2f40-83ea-84c0-5ff0104e0f2c
        # Combinatorial Counting with Multiset Permutations
        # Time: O(n). Actually O(26 * N / 2)
        # Space: O(n)


        # Step 1: Count character frequencies
        counts = Counter(s)
        
        half_counts = {}
        mid_char = ""
        m = 0  # Length of the half-string
        
        # Step 2: Extract half-frequencies and identify the middle character
        for char in counts.keys():
            if counts[char] % 2 != 0:
                mid_char = char
            
            if counts[char] // 2 > 0:
                half_counts[char] = counts[char] // 2
                m += counts[char] // 2
                
        # Step 3: Calculate the total distinct palindromic permutations initially
        total_perms = math.factorial(m)
        for count in half_counts.values():
            total_perms //= math.factorial(count)
            
        # If k exceeds the total possible distinct permutations, return empty
        if k > total_perms:
            return ""
            
        half_str = []
        
        # Step 4: Construct the first half character by character
        for i in range(m):      # runs n/2 times
            remaining_length = m - i
            
            # Check each available character in alphabetical order
            for char in sorted(half_counts.keys()):            # runs 26 times max
                if half_counts[char] > 0:
                    # Number of permutations if we lock 'char' into the current position
                    perms_with_char = (total_perms * half_counts[char]) // remaining_length
                    
                    if k <= perms_with_char:
                        # The k-th permutation falls within this character's block
                        half_str.append(char)
                        half_counts[char] -= 1
                        total_perms = perms_with_char  # Update total for the next iteration
                        break
                    else:
                        # Skip this character's block and reduce k
                        k -= perms_with_char
                        
        # Step 5: Assemble the final palindrome
        first_half = "".join(half_str)
        return first_half + mid_char + first_half[::-1]