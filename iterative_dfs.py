from cities import cities
from dfs_limited import dfs_limited


def iterative_dfs(start, finish):
    for i in range(len(cities)):
        graph, result = dfs_limited(start, finish, i)
        if result:
            return graph
