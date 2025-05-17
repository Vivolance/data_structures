"""
Dijkstra only works when we are finding the shortest path in a graph that has only positive weights, it would not work
well in graphs that have negative weights between the nodes. Hence, bellman-ford algorithm is used here instead. Bellman-ford
is a brute force solution to search all possible paths, caching the shortest path after traversing all possibilities of
the graph.

Time Complexity: O(V x E)
- V number of vertices
- E number of edges

Key Concepts:
1. Used when your graphs has negative weights or negative cycles
2. Bellman Ford can detect negative cycles, but cannot resolve shortest paths for them if they exist
3. Bellman for loops through V-1 times, assuming V number of nodes, the longest path without repeating nodes is V - 1,
after V - 1 times, the shortest path is guaranteed for that node.
4. We do not take into account of repeated nodes because that would result in a cycle, which boils down to 2 cases:
    - Negative cycles where the path gets shorter and shorter (bellman ford uses this to flag out negative cycles)
    - If positive cycle it only gets longer and longer which is not what we want
5. Hence, Bellman Ford algorithm requires you to input the number of vertices
6. Each iteration of V-1 times lets you find the shortest paths that are 1 edges long, 2 edges long...
"""

import sys
from collections import defaultdict


def bellman_ford(
    source: str, vertices: list[str], adjacency_list: list[tuple[str, str, int]]
) -> dict[str, int]:
    # Initialise your answer to return
    distance: dict[str, int] = defaultdict(lambda: sys.maxsize)
    distance[source] = 0

    # loop through vertices V - 1 times, max path without repeating vertices.
    for _ in range(len(vertices) - 1):
        # Flag to display if a full pass over all edges is done and nothing is updated
        # signalling it is ready and break out early
        check = True
        for source, target, curr_distance in adjacency_list:
            # check if curr update (distance) is shorter or new explored path is shorter
            if distance[target] > distance[source] + curr_distance:
                # update distance if shorter path found
                distance[target] = distance[source] + curr_distance
                check = False
        if check:
            break

    # Logic to detect negative weight cycles by going through the entire adjacency_list once more
    # By right, there should not be any more updates
    # If found out that there is still a shorter path update, it means somewhere a negative weight cycle is present
    for source, target, curr_distance in adjacency_list:
        candidate_distance: int = distance[source] + curr_distance
        if candidate_distance < distance[target]:
            raise RuntimeError("Negative weight cycle present")

    return distance


if __name__ == "__main__":
    adjacency_list: list[tuple[str, str, int]] = [
        ("Hougang", "Kranji", 8),
        ("Hougang", "Bishan", 3),
        ("Hougang", "Tampines", 5),
        ("Kranji", "Bishan", 2),
        ("Bishan", "Tampines", 1),
        ("Kranji", "CCK", 2),
        ("Bishan", "Raffles", 10),
        ("Tampines", "Eunos", 1),
        ("CCK", "Raffles", -7),
        ("Raffles", "Eunos", 1),
    ]

    answer: dict[str, int] = {
        "Hougang": 0,
        "Bishan": 3,
        "Tampines": 4,
        "Kranji": 8,
        "CCK": 10,
        "Eunos": 4,
        "Raffles": 3,
    }
    vertices: list[str] = list(answer.keys())
    print(vertices)

    actual_answer = bellman_ford(
        source="Hougang", vertices=vertices, adjacency_list=adjacency_list
    )
    assert actual_answer == answer
