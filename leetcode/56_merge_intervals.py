from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()
        stack = []

        for start,end in intervals:

            if stack and start <= stack[-1][1]:
                stack[-1][1] = max(end, stack[-1][1])
            else:
                stack.append([start,end])

        return stack
