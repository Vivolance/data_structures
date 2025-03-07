"""
Using bisect to binary search the first occurence of a target
given a list[int]

bisect_left: gives the position of the first occurrence of the target
bisect_right: gives the position + 1 of the last occurrence of the target
"""

import bisect


def binary_search_left(n: list[int], x: int) -> int:
    """
    Performs a binary search over n to find x, if present return the position else -1
    Note that n must already be a sorted list
    """
    i: int = bisect.bisect_left(n, x)
    if i < len(n) and n[i] == x:
        return i
    return -1


def binary_search_right(n: list[int], x: int) -> int:
    """
    Performs a binary search over n to find x, if present return the position else -1
    Note that n must already be a sorted list
    """
    i: int = bisect.bisect_right(n, x)
    # i - 1 because bisect_right gives you the next position where x is found
    if i < len(n) and n[i - 1] == x:
        return i - 1
    return -1


if __name__ == "__main__":
    n: list[int] = [1, 2, 3, 4, 4, 5, 6, 7, 8]
    target: int = 4
    index_bisect_left: int = binary_search_left(n, target)
    index_bisect_right: int = binary_search_left(n, target)
    print(index_bisect_left)
    print(index_bisect_right)
