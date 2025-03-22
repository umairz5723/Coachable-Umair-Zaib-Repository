""" 295. Median of Data Stream """

from heapq import heappop, heappush

class MedianFinder:
    """ Solution Class """

    def __init__(self):
        """
        function to initalize
        the MedianFinder data structure
        """
        self.small_heap = []
        self.large_heap = []


    def add_num(self, num: int) -> None:
        """
        This function inserts a number
        into the data structure depending 
        on sizes of both heaps.

        If the heaps are of equal length, we will
        insert it into the small heap first, inverted.
        The top of the small heap will always hold the
        largest AMONGST the smallet numbers. 

        If the large heap is exactly one element larger,
        we push the given "num" into the large heap first, 
        this pop the smallest element in the large heap and
        move it over to the small heap (inverted).

        This means the median will either reside in both 
        heaps at the 0th index (even data stream is of even
        length.) Or, the median will reside at the 0th index
        of the large_heap.

        Time complexity: O(log n)
        """

        if len(self.small_heap) == len(self.large_heap):
            heappush(self.small_heap, -num)
            move_over = heappop(self.small_heap)
            heappush(self.large_heap, -move_over)
        else:
            heappush(self.large_heap, num)
            move_over = heappop(self.large_heap)
            heappush(self.small_heap, -move_over)


    def find_median(self) -> float:
        """
        This function returns the median
        in the data stream thus far. If the
        lenght of both heaps are even we must take
        the median between two number. Otherwise we have
        an odd total heap length, which means the median
        is one number which resides at the top of our large
        heap.

        Time complexity: O(1)
        """
        if len(self.small_heap) == len(self.large_heap):
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        return self.large_heap[0]
