class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for ch in s:
            if ch.isalnum():
                res.append(ch.lower())
        if res[::-1] == res:
            return True
        else: return False
                
                   
        

            