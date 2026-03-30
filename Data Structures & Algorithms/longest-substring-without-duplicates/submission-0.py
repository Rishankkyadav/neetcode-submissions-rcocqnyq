class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        inter = set()
        count = 0
        max_len = 0

        l = 0
        r = 1

        for r in range(len(s)):
            if s[r] not in inter:
                inter.add(s[r])
            else:
                while s[r] in inter:
                    inter.remove(s[l])
                    l += 1

                inter.add(s[r])

                
            count = r - l + 1
            max_len = max(max_len , count)
        return max_len
                    
                    


                
        

                    



            