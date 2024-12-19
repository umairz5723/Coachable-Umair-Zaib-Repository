""" 659. Design Hit Counter """

from typing import List

class HitCounter:
    def __init__(self):
        self.times = []

    def hit(self, timestamp: int):
        """Record a hit at the given timestamp."""
        self.times.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 300 seconds.
        Args:
            timestamp (int): The current timestamp.
        Returns:
            int: The number of hits within the last 300 seconds.
        """
        lo = 0
        hi = len(self.times) - 1
        target = timestamp - 300

        # Binary search to find the first timestamp within the window
        while lo <= hi:
            mid = (lo + hi) // 2

            # Corrected condition here
            if target >= self.times[mid]:
                lo = mid + 1
            else:
                hi = mid - 1

        return len(self.times) - lo


# Test Cases
hitCounter = HitCounter()
hitCounter.hit(1)
hitCounter.hit(2)
hitCounter.hit(3)
assert hitCounter.getHits(4) == 3  
hitCounter.hit(300)
assert hitCounter.getHits(300) == 4
assert hitCounter.getHits(301) == 3  

hitCounter2 = HitCounter()
hitCounter2.hit(1)
hitCounter2.hit(2)
hitCounter2.hit(301)
assert hitCounter2.getHits(301) == 2 
assert hitCounter2.getHits(302) == 1  

hitCounter3 = HitCounter()
hitCounter3.hit(1)
assert hitCounter3.getHits(1) == 1  
assert hitCounter3.getHits(301) == 0  
