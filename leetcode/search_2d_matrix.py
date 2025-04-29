""" 74. Search a 2D Matrix """

from typing import List

class Solution:
    """ Solution Class """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        This function utilizes binary search
        on the input matrix to find the existence
        of a target in O(log(m*n)) time. We can 
        treat the matrix as a flattened list and 
        search it, translating the "mid" pointer back into
        a row and column to extract the middle value.

        1) Initialize two pointers l,r where l 
        represents the first element in the matrix
        and r is the final element.

        2) Conduct binary search:
            - Extract a mid 
            - Translate the mid point
            into a row position using (mid // cols)
            - Translate the mid point
            into a column position using (mid % cols)
            - Return if/when the mid_val is the target
            - Cut down on the search by comparing the 
            target value versus the mid_val.

        Time complexity: O(log(m * n))
        Space complexity: O(1)

        """

        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows * cols) - 1

        while l <= r:

            mid = (l+r) // 2

            # Translate our mid into a row and col
            m_r = mid // cols
            m_c = mid % cols

            mid_val = matrix[m_r][m_c]

            if target == mid_val:
                return True
            if target < mid_val:
                r = mid - 1
            else:
                l = mid + 1

        return False
