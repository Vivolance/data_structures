"""
SUBSETS 1

Given an array nums of unique integers, return all possible subsets of nums.
The solution set must not contain duplicate subsets. You may return the solution in any order.

Example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


SUBSETS 2
Similar to subset 1, but now we have duplicates in nums. Solution must now contain duplicate subsets

KEY CONCEPTS:
1. Identify how we are going to choose each num in nums
    [], [1], [2], [3], pop [3], pop [2], [2,3], pop [1], [1,2], [1,3], pop [1,3], pop [1,2], [1,2,3], pop [1,2,3]

2. Backtracking problem, use DFS, call_stack contains:
    - curr_path
    - last_left_off_index

3. Pop from stack, append to result then append to call_stack

4. (For Subset 2) Sort raw nums, so that in the process of appending, we are adding subsets in the same sequence even if
there are repeated candidates. This allows us to check for exact duplicate sets from our results and filter them
"""


def subset(nums: list[int]) -> list[list[int]]:
    call_stack: list[tuple[list[int], int]] = [([], 0)]
    results: list[list[int]] = []
    n: int = len(nums)
    while call_stack:
        curr_path, last_index = call_stack.pop()
        results.append(curr_path)
        for i in range(last_index, n):
            new_path: list[int] = curr_path + [nums[i]]
            call_stack.append((new_path, i + 1))
    return results


def subset_two(nums: list[int]) -> list[list[int]]:
    nums.sort()
    call_stack: list[tuple[list[int], int]] = [([], 0)]
    results: list[list[int]] = []
    n: int = len(nums)
    while call_stack:
        curr_path, last_index = call_stack.pop()
        # Additional check here to remove duplicate sets
        if curr_path not in results:
            results.append(curr_path)
        for i in range(last_index, n):
            new_path: list[int] = curr_path + [nums[i]]
            call_stack.append((new_path, i + 1))
    return results


if __name__ == "__main__":
    subset_answer: list[list[int]] = subset([1, 2, 3])
    print(subset_answer)
    subset_two_answer: list[list[int]] = subset_two([1, 2, 1])
    print(subset_two_answer)
