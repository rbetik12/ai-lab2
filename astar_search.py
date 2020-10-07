from cities import cities
from distances import distances
from greedy_search import Node


class ANode(Node):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.h = 0
        self.g = 0
        self.f = 0

    def __str__(self):
        if self.parent:
            return "Name: " + str(self.name) + " " + "Parent: " + self.parent.name + " Cost: " + str(self.g)
        return "Name: " + str(self.name) + " " + "Parent: " + " None" + " Cost: " + str(self.g)


def checked_opened(opened, node):
    for el in opened:
        if node == el and node.g >= el.g:
            return False
    return True


def a_star(start, finish):
    start_node = ANode(start, None)
    start_node.g = start_node.f = start_node.h = 0

    finish_node = ANode(finish, None)
    finish_node.g = finish_node.f = finish_node.h = 0

    opened = list()
    closed = list()
    graph = list()

    opened.append(start_node)

    while opened:
        opened.sort()

        current_node = opened.pop(0)

        closed.append(current_node)

        if current_node == finish_node:
            path = list()
            sum = current_node.g
            while current_node != start_node:
                path.append(current_node)
                current_node = current_node.parent
            return graph, path, sum

        children = list()

        for child in cities[current_node.name]:
            children.append(ANode(child["name"], current_node))

        for child in children:
            if child in closed:
                continue

            child_parent_dist = 0
            for city in cities[current_node.name]:
                if child.name == city["name"]:
                    child_parent_dist = city["dist"]

            child.g = child.parent.g + child_parent_dist
            child.h = distances[child.name]
            child.f = child.g + child.h

            if checked_opened(opened, child):
                opened.append(child)
                graph.append(current_node.name + " --> " + child.name)
