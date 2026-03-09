from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Step 1: Count frequency
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Step 2: Create buckets (index = frequency)
        freq = [[] for i in range(len(nums) + 1)]
        
        for num, c in count.items():
            freq[c].append(num)
        
        # Step 3: Collect top k frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res