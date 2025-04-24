'''153. Find Minimum in Rotated Sorted Array'''

class Solution:
  '''Solution Class'''
  
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        min_val = inf

        while lo <= hi:
            mid = (lo + hi) // 2
            min_val = min(min_val, nums[mid])

            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        
        return min_val
