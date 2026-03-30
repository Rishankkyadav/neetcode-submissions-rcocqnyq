from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anamap = defaultdict(list)
        result = []
        
        for s in strs:
            sorted_s = tuple(sorted(s))
            anamap[sorted_s].append(s)

        for values in anamap.values():
            result.append(values)

        return result


