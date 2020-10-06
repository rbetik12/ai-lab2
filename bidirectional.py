from collections import deque

from cities import cities


def __vertexs_intersect(visited_vertexs_1, visited_vertexs_2):
    for i in visited_vertexs_1:
        for j in visited_vertexs_2:
            if i == j:
                return True, i
    return False, None


def __bfs_iteration(search_queue, visited_vertexs, graph, marked_vertexs):
    if search_queue:
        current_node = search_queue.popleft()
        visited_vertexs.append(current_node)

        for node in cities[current_node]:
            if node["name"] not in visited_vertexs:
                if node["name"] not in marked_vertexs:
                    marked_vertexs.append(node["name"])
                    graph.add(current_node + " --> " + node["name"])
                search_queue.append(node["name"])
    return search_queue, visited_vertexs, graph, marked_vertexs


def bidirectional_bfs(start, finish):
    visited_vertexs_1 = list()
    visited_vertexs_2 = list()
    search_queue_1 = deque()
    search_queue_2 = deque()
    graph_1 = set()
    graph_2 = set()
    marked_vertexs_1 = list()
    marked_vertexs_2 = list()

    visited_vertexs_1.append(start)
    search_queue_1.append(start)

    visited_vertexs_2.append(finish)
    search_queue_2.append(finish)

    while search_queue_1 or search_queue_2:
        search_queue_1, visited_vertexs_1, graph_1, marked_vertexs_1 = __bfs_iteration(search_queue_1,
                                                                                       visited_vertexs_1, graph_1,
                                                                                       marked_vertexs_1)
        search_queue_2, visited_vertexs_2, graph_2, marked_vertexs_2 = __bfs_iteration(search_queue_2,
                                                                                       visited_vertexs_2, graph_2,
                                                                                       marked_vertexs_2)

        is_intersects, node = __vertexs_intersect(visited_vertexs_1, visited_vertexs_2)
        if is_intersects:
            return graph_1, graph_2, node

    return None, None, node
