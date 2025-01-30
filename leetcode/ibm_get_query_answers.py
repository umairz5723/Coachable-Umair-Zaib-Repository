""" Get Query Answers"""

from typing import List
class Solution:

    """ Solution Class """

    def get_query_ans(self, cache_entries: List[List[str]], queries: List[List[str]]) -> List[int]:
        """
        This function uses a 2D dictionary 
        to store all input in cache_entries.

        We then get the result values from 
        the queries list using the 2D dict
        entries which guarentee O(1) lookup
        because the timestamp, value are 
        within the nested dictionary.

        Time complexity: O(N + Q) 
        where N is cache initalization
        and Q is query processing
        Space complexity: O(N)
        """
        cache = {}

        for timestamp, key, value in cache_entries:
            if key not in cache:
                cache[key]= {}
            cache[key][timestamp] = int(value)

        res = []

        for key, timestamp in queries:
            res.append(cache[key][timestamp])

        return res
