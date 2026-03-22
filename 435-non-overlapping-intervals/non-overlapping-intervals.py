from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: sort by ending time
        intervals.sort(key=lambda x: x[1])
        
        count = 0  # number of intervals we can keep
        last_end = float('-inf')
        
        # Step 2: iterate
        for start, end in intervals:
            if start >= last_end:
                # no overlap → take it
                count += 1
                last_end = end
            else:
                # overlap → remove it
                continue
        
        # Step 3: removals = total - kept
        return len(intervals) - count