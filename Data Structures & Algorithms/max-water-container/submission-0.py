class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        for i in range(len(heights)):
            for j in range(i + 1 , len(heights)):
                x = min(heights[i] , heights[j]) * (j-i)
                res.append(x)
        return max(res)


            
            
            


        