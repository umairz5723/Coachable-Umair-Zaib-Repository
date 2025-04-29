""" IBM Count Teams"""

from math import comb
from typing import List

class Solution:
    """ Solution Class """
    def count_teams(self, skills: List[int], min_players: int, min_lvl: int, max_lvl: int) -> int:
        """
        This function determines the number of
        combinations that can be formed when 
        creating a team of valid players.

        Critia: In order for a player to be eligible
        they must have a level of at least min_level
        and at most max_level. We handle this in the initial
        loop. 

        After determing the number of eligible players
        we can then calculate the number of teams
        that can formed using the combinations. We start
        at the min_players position and move towards 
        eligible + 1:
            (Exp: min_players = 3, eligible = 4, min_level = 4, max_level = 10)
            total_teams += comb(4,3) = 4
            total_teams += comb(4,4) = 1
            = 4 + 1 = 5

        """
        # Step 1: Count the number of eligible players
        eligible = 0
        for skill in skills:
            if min_lvl <= skill <= max_lvl:
                eligible += 1

        # Step 2: Calculate the total number of valid teams
        total_teams = 0
        for team_size in range(min_players, eligible + 1):
            total_teams += comb(eligible, team_size)

        return total_teams
