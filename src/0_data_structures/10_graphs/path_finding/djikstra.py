"""
Dijkstra is an algorithm that allows you to find the SHORTEST PATH from a source node to all other paths. (There might
be multiple path to the same node, and the most direct path may not be the shortest path)

TIME COMPLEXITY: O((V+E)logV)

Key Concepts:

1. Create a Priority Queue (min-heap) to append the curr_nodes' neighbour and their current shortest distance. Use this
to repeatedly check all nodes and its neighbour for the optimal shortest path, comparing with final_distance in 3.
(Technically we could do without using priority queue, but we are wasting an opportunity to optimize, since we are not
prioritising checking the minimum distances first, which is the crux of dijkstra, resulting in wasteful computations)

2. As the adjacency list is bidirectional, we have to create a bidirectional adjacency dict to map each node to each
other with their distance.

3. Create a final distance dict to display all shortest distances from the given source node to all other nodes. We
update this list iteratively to ensure all distances are the shortest.
"""

import heapq
import sys
from collections import defaultdict

# input set
adjacency_list: list[tuple[str, str, int]] = [
    ("Hougang", "Punggol", 5),
    ("Hougang", "Kovan", 1),
    ("Hougang", "Serangoon", 3),
    ("Punggol", "Pasir Ris", 1),
    ("Punggol", "Kovan", 2),
    ("Kovan", "Bishan", 2),
    ("Bishan", "Farrer", 1),
    ("Serangoon", "Farrer", 1),
    ("Kovan", "Serangoon", 1),
]

# output set
answer: dict[str, int] = {
    "Hougang": 0,
    "Punggol": 3,
    "Kovan": 1,
    "Serangoon": 2,
    "Pasir Ris": 4,
    "Bishan": 3,
    "Farrer": 3,
}


def dijkstra(source: str, adjacency_list: list[tuple[str, str, int]]) -> dict[str, int]:
    # 1. Create bidirectional mapping
    adjacency_dict: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for curr_source, curr_target, distance in adjacency_list:
        adjacency_dict[curr_source].append((curr_target, distance))
        adjacency_dict[curr_target].append((curr_source, distance))

    # 2. Initialise final result set distance default dict to return
    final_distance: defaultdict[str, int] = defaultdict(lambda: sys.maxsize)
    final_distance[source] = 0

    # Initialise priority queue to start travelling entire adjacency list
    priority_queue: list[tuple[int, str]] = [(0, source)]
    while priority_queue:
        curr_distance, curr_node = heapq.heappop(priority_queue)
        if curr_distance > final_distance[curr_node]:
            continue
        for neighbour, neighbour_distance in adjacency_dict[curr_node]:
            # checks the current shortest distance to this neighbour
            distance_through_neighbour: int = curr_distance + neighbour_distance
            # update the current shortest distance for the neighbour if it is shorter
            if distance_through_neighbour < final_distance[neighbour]:
                final_distance[neighbour] = distance_through_neighbour
                # push the latest shortest distance into the priority queue
                heapq.heappush(priority_queue, (distance_through_neighbour, neighbour))
    return final_distance


if __name__ == "__main__":
    actual_answer: dict[str, int] = dijkstra("Hougang", adjacency_list)
    print(actual_answer)
    assert actual_answer == answer
