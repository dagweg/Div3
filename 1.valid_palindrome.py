# Time: 8 minutes
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        word = ''
        for c in s:
            if 'a' <= c <= 'z' or '0' <= c <= '9':
                word = word + c

        n = len(word)
        for i in range(n//2):
            if word[i] != word[n-i-1]: 
                return False

        return True
