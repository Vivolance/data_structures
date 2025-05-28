"""
TikTok 2025 Big Data Engineer OA Question 2.

Given
1. processingPower: list[int] -> Represents a list of analyzers and their processing power

You are to find out power attainable by choosing the analyzers in the list. However you cannot choose analyzers which
are a difference of +/- 1. You can choose adjacent analyzers.

Eg. processingPower = [3,3,5,6,7,7,9,5,5,2]

Total output = 3+3+5+5+5+7+7+9 = 44

answer = 44
"""

from collections import defaultdict


class Solution:
    """
    Key concepts:
    1. Dynamic Programming problem
    2. Create a defaultdict that stores the power and frequency in the list of nums
    3. Sort the power in ascending order, now we have a problem similar to house robber
    4. Base case will be to choose or not to choose the smallest number
    5. Subsequently check +1, take the max (curr, prev + next)
    """

    def max_power(self, processing_power: list[int]) -> int:
        my_dict: defaultdict[int, int] = defaultdict(int)
        for num in processing_power:
            my_dict[num] += 1
        power_list: list[int] = sorted(my_dict.keys())
        n: int = len(power_list)

        # Initialise dp array
        dp: list[int] = [0] * n

        # Initialise base case 1
        dp[0] = my_dict[power_list[0]] * power_list[0]

        # Case when next power is 1 higher than previous
        if power_list[1] == power_list[0] + 1:
            # populate the max answer up to this point in the dp array
            dp[1] = max(dp[0], my_dict[power_list[1]] * power_list[1])
        # Case when next power can be chosen (i.e > 1 than previous)
        else:
            # populate the max answer up to this point in the dp array
            dp[1] = dp[0] + my_dict[power_list[1]] * power_list[1]

        for i in range(2, n):
            # Skip curr
            if power_list[i] == power_list[i - 1] + 1:
                # add dp answer 2 steps behind because we skip current
                dp[i] = max(
                    dp[i - 1], my_dict[power_list[i]] * power_list[i] + dp[i - 2]
                )
            # Choose curr
            else:
                dp[i] = my_dict[power_list[i]] * power_list[i] + dp[i - 1]

        return dp[n - 1]


if __name__ == "__main__":
    processingPower: list[int] = [3, 3, 5, 6, 7, 7, 9, 5, 5, 2]
    actual_answer: int = 44
    solution: Solution = Solution()
    answer: int = solution.max_power(processingPower)
    print(answer)
    assert answer == actual_answer
