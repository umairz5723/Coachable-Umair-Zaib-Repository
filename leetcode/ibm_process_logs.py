""" Process Logs"""
from typing import List

class Solution:
    """ Solution Class """
    def process_logs(self, logs: List[str], threshold: int) -> List[str]:
        """
        This function uses a dictionary to 
        keep a log of transactions made.

        For each log in the logs list we
        split the string and update the amount
        of transactions made:
        - We handle the edgecase of the sender 
        being the reciever = 1 transaction.
        - And normal transactions where the
        unique sender/receiver each update 
        their transaction amount by 1.

        Our final steps is to go through the 
        dictionary values and append any 
        entries (user_ids) that meet or exceed
        the threshold. Lastly, we return this
        as as sorted list.
        """
        log_dict = {}

        # Process each log entry
        for log in logs:
            sender, receiver, _ = log.split()

            # Handle self-transaction
            if sender == receiver:
                log_dict[sender] = log_dict.get(sender, 0) + 1
            else:
                # Update sender count
                log_dict[sender] = log_dict.get(sender, 0) + 1
                # Update receiver count
                log_dict[receiver] = log_dict.get(receiver, 0) + 1

        # Find users with transactions >= threshold
        sus = []
        for user_id, count in log_dict.items():
            if count >= threshold:
                sus.append(user_id)

        sus.sort()
        return sus 
