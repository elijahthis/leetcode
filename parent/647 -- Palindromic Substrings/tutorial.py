class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_count = 0;

        for i in range (len(s)):
            # odd length palindrome
            palindrome_count += self.countPali(s, i, i);
            
            # even length palindrome
            palindrome_count += self.countPali(s, i, i+1);

        return palindrome_count;


    def countPali(self, s: str, l: int, r: int) -> int:
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count

