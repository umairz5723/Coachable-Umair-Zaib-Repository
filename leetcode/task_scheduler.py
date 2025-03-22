""" 621. Task Scheduler """

from collections import defaultdict
from typing import List
from heapq import heappush, heappop


class Solution:
    """  Solution Class """
    def least_interval(self, tasks: List[str], n: int) -> int:
        '''
        This function returns the minimum number
        of CPU intervals required to complete 
        all tasks in the tasks input list.

        Steps:
        - Collect the frequency of each task
        - Initialize a MAX heap (invert the frequency)
        so that we can always take the most frequency
        task during the next step
        - Let the pq simulate a CPU interval where
        we create a cur_interval list of size (n+1)
        to potentionally do n tasks that are UNIQUE.
        - After we decrement the frequency by one 
        we place tasks that dont have a freq == 0 
        back into the PQ for another interval.
        - Lastly we update the time based on if 
        we require another CPU interval (still elements
        in PQ) or if this interval was the final one.

        Time Complexity: O(N Log N) - If heap grows to size N
        Space Complexity: O(N)

        '''

        # Initialize the frequency of each task in tasks
        freq_dict = defaultdict(int)

        for task in tasks:
            freq_dict[task] += 1

        # Initialize a MAX heap (invert the freq to be negative)
        pq = []

        for task, freq in freq_dict.items():
            heappush(pq, (-freq, task))

        time = 0

        while pq:
            cur_interval = []

            for _ in range(n+1):
                if pq:
                    # Select these tasks to be used during this interval
                    cur_interval.append(heappop(pq))

            # Update the frequencies of these tasks
            for freq, task in cur_interval:
                if freq + 1 < 0:
                    # If we have not completed all occurences of this task
                    # We need to push the updated freq back into the max heap
                    heappush(pq, (freq + 1, task))

            # Update the time
            if pq:
                # We have more tasks to schedule this will require n+1 time
                time += n + 1
            else:
                # This was the final iteration of scheduling
                time += len(cur_interval)

        return time
    
