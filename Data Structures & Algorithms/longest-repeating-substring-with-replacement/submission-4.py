class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        freq = {}
        res = 0

   
        #ws - mfc <=k

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r] , 0) + 1
            max_freq = max(freq.values())

            if (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res , r - l + 1 , 0)
        return res

            





       

                

                    
                
 

        
        