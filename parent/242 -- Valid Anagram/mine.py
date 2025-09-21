class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ANALYSIS:
        # - We can sort the strings and compare them
        # - If the strings are anagrams, then the sorted strings should be equal
        # - The time complexity is O(nlogn) where n is the length of the string
        # - The space complexity is O(n) where n is the length of the string

        return sorted(s) == sorted(t)