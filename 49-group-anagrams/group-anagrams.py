from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sorted_str = ''.join(sorted(s))

            if sorted_str in groups:
                groups[sorted_str].append(s)
            else:
                groups[sorted_str] = [s]

        result = []
        for value in groups.values():
            result.append(value)

        return result
