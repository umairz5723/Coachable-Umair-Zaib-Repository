""" 735. Asteroid Collision """

from typing import List

class Solution:
   """Class containing methods for asteroid collision simulation."""

   def asteroidCollision(self, asteroids: List[int]) -> List[int]:
       """
       Simulates collisions between asteroids and returns surviving asteroids.
       
       Positive integers represent asteroids moving right.
       Negative integers represent asteroids moving left.
       When asteroids collide, the smaller one explodes.
       If both are same size, both explode.

       Args:
           asteroids (List[int]): List of asteroid sizes with directions
                                 (positive = right, negative = left)

       Returns:
           List[int]: List of surviving asteroids after all collisions
       """

       stack = []
     
       for asteroid in asteroids:
           # Handle collisions using stack
           while stack and stack[-1] > 0 and asteroid < 0:
               # Current asteroid is moving left, top of stack moving right
               if stack[-1] < abs(asteroid):
                   # Stack asteroid is smaller, it explodes
                   stack.pop()
                   continue
               elif stack[-1] == abs(asteroid):
                   # Equal size, both explode
                   stack.pop()
                   break
               else:
                   # Current asteroid is smaller, it explodes
                   break
           else:
               # No collision occurred or asteroid survived collisions
               stack.append(asteroid)

       return stack
