""" 435. Non-overlapping Intervals """

from typing import List

class Solution:

    """ Solution Class """

    def erase_overlap_intervals(self, intervals: List[List[int]]) -> int:
        """
        This function uses a greedy approach to 
        return the minimum number of intervals needed
        to be removed to make the rest of the intervals
        non-overlapping:

        We sort the list based on the end times where each
        interval is [start,end]. By doing so we minimize future
        interval conflicts as we deal with the intervals that end
        the earliest first. 

        We then keep track of prev_end which represents the last 
        completed interval to verify whether it conflicts with the 
        start time of the current interval we are looping over, if so,
        we "remove" it by adding one to "removals".

        Otherwise we adjust prev_end to reflect the latest interval that
        has ended. 

        Time complexity: O(N LOG N)
        Space complexity: O(1)

        """

        intervals.sort(key = lambda x:x[1])
        prev_end = intervals[0][1]
        removals = 0

        for i in range(1, len(intervals)):
            if prev_end > intervals[i][0]:
                removals += 1
            else:
                prev_end = intervals[i][1]

        return removals
