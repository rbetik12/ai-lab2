from graphviz import Digraph

from bfs import bfs
from bidirectional import bidirectional_bfs
from dfs import dfs
from dfs_limited import dfs_limited
from iterative_dfs import iterative_dfs


def draw_tree(tree_algorithm, filename, comment, start, finish, s_node=None):
    dot = Digraph(comment)
    dot.format = 'svg'

    for node in tree_algorithm:
        left, right = node.split("-->")
        left = left.strip()
        right = right.strip()
        if left == start:
            dot.node(left, left, color='red', style='filled', fillcolor='red')
        else:
            dot.node(left, left)
        if right == finish:
            dot.node(right, right, color='red', style='filled', fillcolor='red')
        else:
            dot.node(right, right)

        if left == s_node:
            dot.node(left, left, color='green', style='filled', fillcolor='green')
        if right == s_node:
            dot.node(right, right, color='green', style='filled', fillcolor='green')

        dot.edge(left, right)

    dot.render("trees/" + filename)


if __name__ == "__main__":
    start = "Брест"
    finish = "Казань"
    graph_bfs = bfs(start, finish)
    graph_dfs = dfs(start, finish)
    graph_dfs_limited, res = dfs_limited(start, finish, 7)
    graph_iterative_dfs = iterative_dfs(start, finish)

    graph_front_bfs, graph_back_bfs, node = bidirectional_bfs(start, finish)

    draw_tree(graph_bfs, "BFS-Tree", "bfs", start, finish)
    draw_tree(graph_dfs, "DFS-Tree", "dfs", start, finish)
    draw_tree(graph_dfs_limited, "DFS-Limited-Tree", "dfs-limited", start, finish)
    draw_tree(graph_iterative_dfs, "DFS-Iterative", "dfs-iterative", start, finish)

    draw_tree(graph_front_bfs, "BFS-Front", "bfs-front", start, finish, node)
    draw_tree(graph_back_bfs, "BFS-Back", "bfs-back", finish, start, node)
