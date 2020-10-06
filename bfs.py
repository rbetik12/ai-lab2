from collections import deque

from cities import cities


# graph = list()


def bfs(start: str, finish: str):
    visited, search_queue = set(), deque()
    visited.add(start)
    search_queue.append(start)

    marked_vertexs = list()

    graph = set()

    while len(search_queue) > 0:
        current_node = search_queue.popleft()
        visited.add(current_node)
        if current_node == finish:
            return graph
        for node in cities[current_node]:
            if node["name"] not in visited:
                if node["name"] not in marked_vertexs:
                    marked_vertexs.append(node["name"])
                    graph.add(current_node + " --> " + node["name"])
                if node["name"] == finish:
                    return graph
                search_queue.append(node["name"])
    return graph
