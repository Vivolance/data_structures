"""
BACKTRACKING

Main Rules to solve any Backtracking problems:
1. *** Identify what states to store in the call_stack (eg stack = [(path, index, remaining)]
2. ** Identify constraints at each level (eg remaining < target)
3. * Backtracking primarily use DFS (stack) to implement

Qn (Combination Sum): Given a list[nums] and the target, find out how many unique combination of the list[nums]
we can derive to match the target. Individual numbers can be repeated unlimited times. [2,2,5] is the same as [2,5,2]


QN (Permutations): Given a list of int, return all unique permutations in any order that can be generated from the list

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


def permutation(nums: list[int]) -> list[list[int]]:
    picks: list[int] = []
    choices: list[int] = nums
    call_stack: list[tuple[list[int], list[int]]] = [(picks, choices)]
    result: list[list[int]] = []
    while call_stack:
        curr_pick, curr_choice = call_stack.pop()
        if not curr_choice:
            result.append(curr_pick)
        else:
            for i in range(0, len(curr_choice)):
                new_pick: list[int] = curr_pick + [curr_choice[i]]
                new_choice: list[int] = curr_choice[:i] + curr_choice[i + 1 :]
                call_stack.append((new_pick, new_choice))
    print(result)
    return result


if __name__ == "__main__":
    combination_sum([2, 5, 6, 9], 9)
    permutation([1, 2, 3])
