"""
Backtracking (Combination Sum)

Main Rules to solve any Backtracking problems:
1. *** Identify what states to store in the call_stack (eg stack = [(path, index, remaining)]
2. ** Identify constraints at each level (eg remaining < target)
3. * Backtracking primarily use DFS (stack) to implement

Qn: Given a list[nums] and the target, find out how many unique combination of the list[nums] we can derive to match
the target. Individual numbers can be repeated unlimited times. [2,2,5] is the same as [2,5,2]
"""


def combination_sum(nums: list[int], target: int) -> list[list[int]]:
    # Sort the nums in place, so that when iterating through nums we can ignore numbers that exceed target
    nums.sort()
    # Define an answer var to store the final answer
    answer: list[list[int]] = []
    # Define current path at every stage
    path: list[int] = []
    # Define index where we left off in our DFS
    index: int = 0
    # Define a call_stack to do backtracking
    call_stack: list[tuple[list[int], int, int]] = [(path, index, target)]
    while call_stack:
        path, index, remaining = call_stack.pop()
        if remaining == 0:
            answer.append(path)
            continue
        else:
            for i in range(index, len(nums)):
                num: int = nums[i]
                # Any further num in nums is ignored since sorted nums will get larger. Avoid redundant checks since
                # remaining is already exceeded at curr num
                if num > remaining:
                    break
                else:
                    curr_path: list[int] = path + [num]
                    new_remaining: int = remaining - num
                    # Track where we left off to avoid repeated num added
                    call_stack.append((curr_path, i, new_remaining))
    print(answer)
    return answer


if __name__ == "__main__":
    combination_sum([2,5,6,9],9)

