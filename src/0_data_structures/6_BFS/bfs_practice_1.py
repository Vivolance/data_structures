"""
Implement a BREADTH FIRST SEARCH (BFS) suing a queue. For simplicity, we always use a deque to implement this.
DFS uses a stack in its implementation (FIFO)
"""

from collections import deque


def bfs(graph: dict[int, list[int]], start: int) -> list[int]:
    # track visited path
    visited: set[int] = set()
    # stores and return the order of the bfs
    order: list[int] = []
    # use queue for bfs
    queue: deque[int] = deque([start])

    while queue:
        curr_node: int = queue.popleft()
        if curr_node not in visited:
            visited.add(curr_node)
            order.append(curr_node)

            # Add neighbours to be visited later
            for neighbour in graph[curr_node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return order


if __name__ == "__main__":
    # Example graph represented as an adjacency list.
    # Note that 1 could be added twice into the queue, but it is fine
    graph: dict[int, list[int]] = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1, 5],
        5: [2, 4],
    }
    print(bfs(graph, 0))
    # expected output [0, 1, 2, 3, 4, 5]
