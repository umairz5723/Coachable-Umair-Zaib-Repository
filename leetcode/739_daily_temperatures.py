"""739. Daily Temperatures"""
import List

class Solution:
  """Solution Class"""
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        The solution makes use of a stack. We fill the stack by keeping track of the temp and index
        when its empty or when the current temperature is less than our equal to the top of our stack.
        We pop from the stack when we run into a temperature that is larger in value compared to the top of our stack
        by getting the difference between the current value of i and the popped element's index. We log this difference into the 
        popped elements index.
        """
        ans_array = [0] * len(temperatures)
        stack = [(temperatures[0], 0)]

        for i in range(1,len(temperatures)):

            while stack and stack[-1][0] < temperatures[i]:
                temp, idx = stack.pop()
                ans_array[idx] = i - idx
            
            stack.append((temperatures[i], i))
        
        return ans_array
