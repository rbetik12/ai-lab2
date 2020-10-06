from cities import cities


def dfs(start: str, finish: str):
    visited, search_stack = set(), list()
    visited.add(start)
    search_stack.append(start)

    graph = set()
    marked_vertexs = list()

    while len(search_stack) > 0:
        current_node = search_stack.pop()
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
                search_stack.append(node["name"])
