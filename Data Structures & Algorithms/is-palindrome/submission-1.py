class Solution:
    def isPalindrome(self, s: str) -> bool:
        # how to put to lowercase
        s = ''.join(c for c in s.lower() if c.isalnum()) 
        # need to remove spaces and question marks
        return s == s[::-1]