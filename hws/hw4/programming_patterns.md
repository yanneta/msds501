
## Problem solving  problems

In this homework, you are going to solve a few easy LeetCode-style problems that use the programming patterns studied in class. Hints are provided at the end of the document. Look at the test cases for examples of inputs and outputs.

## Deliverables

You should fill the functions in  problems.py. Your solutions should pass the pytest.


## Here is the list of problems
1. Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place.  

2. Write a function that, given an integer array and an integer k finds a contiguous subarray of length  k that has the maximum average value and returns this value.

3. Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.

4. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

5. You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

> Return a list answer of size 2 where:

> answer[0] is a list of all players that have not lost any matches.
> answer[1] is a list of all players that have lost exactly one match. 

The values in the two lists should be returned in increasing order.

## Hints:
1. This problem can be solve with two pointers in one pass throught the list.

2. This is a sliding window problem. Consider all windows of length k. Keep track of max sum and update current sum. When dividing interger do float(maxsum)/k.

3. Create a set to keep track of elements.
