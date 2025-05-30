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
This tell us that we need a stack.

2. Call stack should contain information regarding where we left off and the answer up to that point
    - Remaining value up to that point we have chosen
    - Index that we left off [2,5,6,9] so that we can choose the next number
    - Answer set up till now []
"""


def combination_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    result: list[list[int]] = []
    n: int = len(nums)
    # Base case if target is less than smallest nums
    if target < nums[0]:
        return [[]]
    call_stack: list[tuple[list[int], int, int]] = [([], target, 0)]
    while call_stack:
        answer_set, remaining, index = call_stack.pop()
        if remaining == 0:
            result.append(answer_set)
        else:
            for i in range(index, n):
                if nums[i] <= remaining:
                    updated_answer_set: list[int] = answer_set + [nums[i]]
                    new_remaining: int = remaining - nums[i]
                    call_stack.append((updated_answer_set, new_remaining, i))
                else:
                    break

    return result


if __name__ == "__main__":
    combination_sum_one_result: list[list[int]] = combination_sum([2, 5, 6, 9], 9)
    print(combination_sum_one_result)
