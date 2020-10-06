from collections import deque

from cities import cities


def full(start: str):
    visited, search_queue = set(), deque()
    visited.add(start)
    search_queue.append(start)

    graph = set()

    while len(search_queue) > 0:
        current_node = search_queue.popleft()
        visited.add(current_node)
        for node in cities[current_node]:
            if node["name"] not in visited:
                name = current_node + " --> " + node["name"]
                graph.add(name)
                search_queue.append(node["name"])
    return graph
