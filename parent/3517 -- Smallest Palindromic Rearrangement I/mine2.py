class Solution:
    def smallestPalindrome(self, s: str) -> str:
        # Shorter. Same half-sort idea
        # Time: O(nlogn)
        # Space:  O(n)
        n = len(s)

        left = sorted(s[:n // 2])
        return ''.join(left + ([s[n // 2]] if n%2 else []) + left[::-1])