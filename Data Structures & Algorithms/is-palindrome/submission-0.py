#T:O(n), S:O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ''

        for c in s:
            if c.isalnum(): #check if char is alphanumeric
                st += c.lower()
        
        st_rev = st[::-1] #reverse a string

        return st == st_rev

            
        