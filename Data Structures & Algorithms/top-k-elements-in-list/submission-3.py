
from collections import Counter
class Solution:
    res = []
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        keys = list(freq.keys())
        ex = sorted(keys , key = lambda x: freq[x] , reverse = True)

        return ex[0:k]






        


        