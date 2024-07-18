
def reverse_string(s):
    """
    Reverses the input list of characters in place.
    
    :param s: List[str] - A list of characters to be reversed.
    :return: None - This function modifies the list in place and does not return anything.
    
    Example:
    >>> s = ['h', 'e', 'l', 'l', 'o']
    >>> reverseString(s)
    >>> print(s)
    ['o', 'l', 'l', 'e', 'h']
    """
    # Your code here


def find_max_average(nums, k):
    """
    Finds the maximum average value of a contiguous subarray of length k.

    This function takes an integer array `nums` and an integer `k`, and finds a 
    contiguous subarray of length `k` that has the maximum average value. It 
    returns this maximum average value as a float.

    :param nums: List[int] - The input list of integers.
    :param k: int - The length of the contiguous subarray.
    :return: float - The maximum average value of a contiguous subarray of length `k`.

    Example:
    >>> find_max_average([1, 12, -5, -6, 50, 3], 4)
    12.75

    The contiguous subarray with the maximum average is [12, -5, -6, 50] 
    and the average value is (12 + -5 + -6 + 50) / 4 = 51 / 4 = 12.75.
    """
    # Your code here


def find_numbers(nums):
    """
    Given an integer array nums, find all the unique numbers x in nums that satisfy
    the following: x + 1 is not in nums, and x - 1 is not in nums.

    :param nums: List[int] - The input list of integers.
    :return: List[int] - A list of integers
    Example:
    >>> find_numbers([1, 2, 3, 6, 7, 8, 10])
    [10]
    
    In this example, the numbers 1, 2, 3, 6, 7, and 8 are adjacent to other numbers, 
    so only 10 is returned in the result.
    """
    # Your code here


def contains_duplicate(nums):
    """
    Given an integer array nums, return True if any value appears at least twice in the array, 
    and return False if every element is distinct.

    Parameters:
    nums (List[int]): A list of integers.

    Returns:
    bool: True if any integer appears at least twice, False if all integers are unique.

    Example:
    >>> contains_duplicate([1, 2, 3, 1])
    True
    >>> contains_duplicate([1, 2, 3, 4])
    False
    >>> contains_duplicate([])
    False
    """
    # Your code here


def find_winners_and_losers(matches):
    """
    Given an integer array matches where matches[i] = [winneri, loseri] indicates
    that the player winneri defeated player loseri in a match, return a list answer
    of size 2 where:

    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match.

    Both lists in the answer should be sorted in increasing order.

    Parameters:
    matches (List[List[int]]): A list of matches where each match is represented
                               as a list of two integers [winner, loser].

    Returns:
    List[List[int]]: A list containing two lists:
                     - The first list contains all players who have not lost any matches.
                     - The second list contains all players who have lost exactly one match.
                     Both lists are sorted in increasing order.

    Example:
    >>> matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4]]
    >>> find_winners_and_losers(matches)
    [1, 2, 10], [4, 5, 7, 8, 9]
    """
    from collections import defaultdict

    # Your code here
