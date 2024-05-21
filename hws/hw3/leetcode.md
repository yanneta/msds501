
## Leetcode problems

In this homework, you are going to solve a few easy LeetCode-style problems. Hints are provided at the end of the document. Look at the test cases for examples of inputs and outputs.

## Deliverables

You should fill the functions in  leetcode_problems.py. Your solutions should pass the pytest.


## Here is the list of problems
1. Given two strings, word1 and word2, merge them by adding letters in alternating order, starting with word1. If one string is longer than the other, append the remaining letters onto the end of the merged string. 


2. For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

> Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

3. Imagine there are n students in a class, each with a different number of books they own represented by an integer array. You're also given an integer, extraBooks, which represents the additional books you have.

> Your task is to determine for each student, represented by an index in the array, if they will have the highest number of books in the class after receiving your extra books. Return a boolean array of length n, where each element is true if the corresponding student, after receiving the extra books, will have the highest number of books in the class, or false otherwise.

> Note that it's possible for multiple students to have the highest number of books in the class, and every student can have a different number of books.

4. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

> You may assume that each input would have exactly one solution, and you may not use the same element twice.

> You should return the answer in order.

5. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

> Note that you must do this in-place without making a copy of the array.

## Hints:

For problem 2, consider all substrings of the smallest given string. Check if the substring divides both strings. Take the larger substring that satisfies the condition.

Problem 3 could take 4 lines of code if you use list comprehensions. Two of these lines are to take care of the case in which books are the empty list.

For problem 4, Consider a double loop on the indices of the array. Can we avoid the double loop (use a dictionary in some way)?

For problem 5, consider looping through all the elements of the array. If you find a zero, move all the remaining elements to the left.

