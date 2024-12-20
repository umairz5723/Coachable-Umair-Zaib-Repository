""" 54. Spiral Matrix """

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        l = 0 
        r = len(matrix[0])
        t = 0
        b = len(matrix)
        res = []

        while l < r and t < b:
            for j in range(l,r):
                res.append(matrix[l][j])
            t+=1
            
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1

            if not(l < r and t < b): break
            
            for j in range(r-1,l-1,-1):
                res.append(matrix[b-1][j])
            b-=1

            for i in range(b-1,t-1,-1):
                res.append(matrix[i][l])
            l+=1
        
        return res
