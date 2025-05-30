"""
You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all
unique combinations of nums where the chosen numbers sum to target.

The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of
each of the chosen numbers is the same, otherwise they are different.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.

Input:
nums = [2,5,6,9]
target = 9

Output: [[2,2,5],[9]]


Key Concepts:
1. Notice that we can put the ways we choose the num into a tree structure:
    2 -> first pick
2  5  6  9 -> second picks
    .
    .
    .
We can use a DFS approach at each level to traverse downwards first, caching where we left off
This tells us that we need a stack.

2.
"""




