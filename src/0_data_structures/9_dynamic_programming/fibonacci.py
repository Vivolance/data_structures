"""
Dynamic Programming (DFS with cache):
1. Using a smaller solution to solve a larger solution
2. Top-Down Approach (Memoization): Break down the larger problems into smaller problems,
each time a smaller solution is derived, we store it to be used later.
3. Bottom Up Approach: Find solution for the small sub problem first, then using these solutions
to build a larger solution to the main problem
"""


# Fibonacci example
# Top-down approach with memoization
# Memo contains answers to smaller problems, think of it as your answer key
def fibo_top_down(n: int, memo: dict[int, int] = None) -> int:
    # Case if memo is none, create empty dict
    if memo is None:
        memo: dict[int, int] = {}
    # Case if n in memo
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo_top_down(n - 1, memo) + fibo_top_down(n - 2, memo)
    return memo[n]


# Bottom-up approach, derive solution from the base case
# Use when you do not have any answers to begin with
def fibo_bottom_up(n: int) -> int:
    # Base Case:
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibo_bottom_up(n - 1) + fibo_bottom_up(n - 2)


if __name__ == "__main__":
    print(fibo_top_down(10))
    print(fibo_bottom_up(10))
