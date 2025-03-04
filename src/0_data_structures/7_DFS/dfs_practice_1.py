"""
Implement a DEPTH FIRST SEARCH (DFS) suing a stack. For simplicity, we always use a deque to implement this.
DFS uses a stack in its implementation (LIFO)
"""

from collections import deque


def dfs(graph: dict[int, list[int]], start: int) -> list[int]:
    # tracks the visited path
    visited: set[int] = set()
    # stores the order of traversal
    order: list[int] = []
    # Use a stack as dfs
    stack: deque[int] = deque([start])

    while stack:
        curr_node: int = stack.pop()
        if curr_node not in visited:
            visited.add(curr_node)
            order.append(curr_node)

            # Add neighbours to the stack to be visited later
            for neighbour in graph[curr_node]:
                if neighbour not in visited:
                    stack.append(neighbour)
    return order


if __name__ == "__main__":
    # Example graph represented as an adjacency list.
    # Note that 1 could be added twice into the stack, but it is fine
    graph: dict[int, list[int]] = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4]
    }
    print(dfs(graph, 0))

