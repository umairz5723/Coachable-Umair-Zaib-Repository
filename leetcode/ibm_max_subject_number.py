""" IBM Max Subject Number"""

from typing import List

class Solution:
    """ Solution Class """
    def max_subjects_number(self, answered: List[int], needed: List[int], q: int) -> int:
        """
        This function returns the number of
        subjects we can pass based on
        the number of questions already 
        answered (answered_list) and the 
        questions needed to pass a given 
        subject (index). We are given an
        integer "q" that represents the number
        of questions we can answer. 

        The goal is the answer as many questions
        as possible such that we can pass as 
        many subjects as possible. This means we 
        must distribute q across answered[i] such that
        we can bring up the value at a given index to 
        meet the value at needed[i].

        The process:
            1. Calculate the remaining questions need for each
            index. In the event that we answered more questions
            than needed, we set the remaining for that given 
            index to 0.
            
            2. Sort the remaining questions so we can increment 
            the indexes with the least "needed" questions.
            
            3. Loop over the sorted remaining questions list and 
            verify that we have enough "q" remaining, if so we can 
            get the difference of q and the current required value. We 
            add one to the passed_subjects when this occurs to represent
            that we have answered the needed questions.
            Should our value of "q" be less than the "req", we can break
            the look because we know the value of "req" will remain the same 
            or increment in value.
        """
        # Step 1: Calculate remaining questions needed for each subject
        remaining = []
        for i in range(len(answered)):
            remaining.append(max(0,needed[i] - answered[i]))

        # Step 2: Sort the remaining question in asc order
        # So we can answer as many remaning questions as possible
        remaining.sort()

        # Step 3: Allocate questions and count passed subjects
        passed_subjects = 0
        for req in remaining:
            if q >= req:
                q -= req
                passed_subjects += 1
            else:
                break

        return passed_subjects
