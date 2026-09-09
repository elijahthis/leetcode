class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ANALYSIS:
        # - We can use a hash table to keep track of the characters we have seen so far
        # - We can use two pointers to keep track of the current substring
        # - We can use a variable to keep track of the max length of the substring
        # - We can iterate through the string and update the hash table and the pointers accordingly
        
        hash = {}   # char -> bool
        left_ptr = 0
        right_ptr = 0
        max_len = 0

        while right_ptr < len(s):
            if s[right_ptr] not in hash:
                hash[s[right_ptr]] = True
                right_ptr += 1
            else:
                max_len = max(max_len, right_ptr - left_ptr)

                del hash[s[left_ptr]]
                left_ptr += 1
        
        return max(max_len, right_ptr - left_ptr)