""" 322. Coin Change """

from typing import List

class Solution:

    """ Solution Class """

    def coin_change(self, coins: List[int], amount: int) -> int:

        """
        This function uses bottom-up DP
        to calculate the fewest coins that
        we need to make == amount.

        1) Sort the coins list to avoid unncessary 
        checks unrealistic combinations
        2) Implement a dp array to hold the amount
        from [0, amount + 1] (i.e: 0 coins until 11 coins).
        3) Get the minimum combination amount
        for each coin up to amount + 1
        4) Collect the difference of the current coin 
        amount "i" - the coin we are currently processing:
             - Iterate through each coin to potentially
            find a new minimum combination, break when
            we have a negative difference. 
             - Update the minimum after the processing of 
             each coin
        5) Return the final index in dp if it holds an actual
        integer value, otherwise return -1.  

        Time Complexity: O(C * A), C is the coins and A is the amount
        Space Complexity: O(A), holding A elements in our DP array
        """

        # Sort the coins and initalize a dp array
        coins.sort()
        dp = [0] * (amount + 1)


        for i in range(1, (amount+1)):
            # Initalize a min value to alter dp
            min_val = float('inf')

            for coin in coins:
                diff = i - coin

                # Break from the loop when we get a negative diff (coins are only getting larger)
                if diff < 0:
                    break

                # Update the min
                min_val = min(min_val, dp[diff] + 1)

            dp[i] = min_val


        # Return the min val at the last index if its not inf
        if dp[-1] == float('inf'):
            return -1

        return dp[-1]
