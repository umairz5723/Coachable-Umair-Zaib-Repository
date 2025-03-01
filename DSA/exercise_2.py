from typing import List


def multiplication_table(rows: int, cols:int) -> List[List[int]]:
    """ Function for creating a multiplication table"""
    table = [[(i + 1) * (j + 1) for j in range(cols)] for i in range(rows)]
    return table


def merge_sorted_list(l1: List[int], l2: List[int]) -> List[int]:
    """ Function for merging two sorted lists"""
    if not l1:
        return l2
    if not l2:
        return l1
    res = []
    p1 = 0
    p2 = 0

    # While both pointers are valid
    while p1 and p2:
        if l1[p1] < l2[p2]:
            res.append(l1[p1])
            p1 += 1
        else:
            res.append(l2[p2])
            p2 += 1

    # Collect any possible remaining elements from either list
    while p1 < len(l1):
        res.append(l1[p1])

    while p2 < len(l2):
        res.append(l2[p2])

    return res

def sum_diagonals(matrix):
    """ Function for returning the sum of diagonals """

    '''
    1 2 3
    4 5 6
    7 8 9        diag = (0,0) + (1,1) + (2,2)
                 anti = (2,0) + (1,1) + (0,2)
    '''
    n = len(matrix)
    diagonal_sum = 0
    anti_diagonal_sum = 0

    for i in range(n):
        # diagonal is when we have equal index values
        # such as (1,1), (2,2), etc..
        diagonal_sum += matrix[i][i]

        # the row will drop down normally
        # but to access the correct column we will
        # start at the end, i.e (0,2) then work our
        # way to the front of each column
        # (0,3-1 - 0) = (0,3)
        # (1,3-1 - 1) = (1, 1)
        # (2, 2-1 - 1) = (2,0)
        anti_diagonal_sum += matrix[i][n - 1 - i]

    return diagonal_sum + anti_diagonal_sum

def first_occurence(nums: List[int], target:int):
    """ Function to find first occurence of a target number"""
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1

    # If nums is sorted we can use binary search
    # to find the target and continue searching
    # towards the left-hand side to find the first
    # occurence


def missing_number(nums: List[int]):
    """ Function to find the missing number in nums"""
    res = len(nums)
    # Use bit manipulation to XOR
    # Each element with the current idx value
    # This servers as canceling out two numbers that are the same
    # Such as 3^3 = 0, so we will be left with the missing value
    for i in range(len(nums)):
        res ^= nums[i] ^ i

    return res

def running_sum(nums: List[int]) -> List[int]:
    """ Function to create a prefix array """
    for i in range(1,len(nums)):
        nums[i] += nums[i-1]

    return nums


def find_duplicates(nums: List[int]):
    """ Function to return a set of duplicates in nums """
    seen = set()
    dups = set()

    for num in nums:
        if num in seen:
            dups.add(num)
        else:
            seen.add(num)

    return dups


def fibonacci(n: int) -> int:
    """ Function for iterative fibonacci """
    if n < 2:
        return n

    prev_1 = 0
    prev_2 = 1

    for i in range(n-1):
        temp = prev_2
        prev_2 = prev_1 + prev_2
        prev_1 = temp

    return prev_2


def merge_intervals(intervals_list: List[List[int]]) -> List[List[int]]:
    """ Function to merge overlapping intervals """
    intervals_list.sort( key = lambda x:x[0])
    stack = []


    for interval in intervals_list:

        if stack and interval[0] <= stack[-1][1]:
            stack[-1][1] = max(interval[1], stack[-1][1])
        else:
            stack.append(interval)

    return stack
