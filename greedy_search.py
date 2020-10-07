from cities import cities


class Node(object):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.f = 0

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.f < other.f

    def __str__(self):
        if self.parent:
            return "Name: " + str(self.name) + " " + "Parent: " + self.parent.name + " Cost: " + str(self.f)
        return "Name: " + str(self.name) + " " + "Parent: " + " None" + " Cost: " + str(self.f)


def check_opened(opened, new_node):
    for node in opened:
        if new_node == node and new_node.f >= node.f:
            return False
    return True


def greedy_search(start, finish):
    opened = list()
    closed = list()
    graph = list()

    start_node = Node(start, None)
    finish_node = Node(finish, None)

    opened.append(start_node)

    while opened:
        opened.sort()

        current_node = opened.pop(0)

        closed.append(current_node)

        if current_node == finish_node:
            path = list()
            sum = 0
            while current_node != start_node:
                path.append(current_node)
                if current_node:
                    sum += current_node.f
                current_node = current_node.parent
            return graph, path, sum

        neighbors = list()

        for neighbor in cities[current_node.name]:
            neighbors.append(Node(neighbor["name"], current_node))

        for next in neighbors:
            for node in cities[current_node.name]:
                if node["name"] == next.name:
                    next.f = node["dist"]

            if next in closed:
                continue

            if check_opened(opened, next):
                opened.append(next)
                graph.append(current_node.name + " --> " + next.name)
