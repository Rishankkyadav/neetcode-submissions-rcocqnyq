class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        count = {}
        l = 0
        r = 1

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r] , 0)

            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            counter = r - l + 1

            max_count = max(counter , max_count)
        return max_count




                

                    
                
            

        
        