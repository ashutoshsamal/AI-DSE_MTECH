import numpy as np


def manhattanDistance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def Astar(start, end, grid):
    open_set = set([start])
    closed_set = set()
    # g stores current shortest distance from start to the current node
    g = {}
    g[start] = 0
    # parents stores an adjacency map of all nodes
    parents = {}
    parents[start] = start

    while len(open_set) > 0:
        n = None

        # find a node with the lowest value of f() - evaluation function
        for v in open_set:
            if n == None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v

        if n == end or grid[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n, grid):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        # update g(m)
                        g[m] = g[n] + weight
                        # change parent of m to n
                        parents[m] = n

                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the end node
        if n == end:
            path = []

            while parents[n] != n:
                path.append(n)
                n = parents[n]

            path.append(start)

            path.reverse()

            print('Path found: {}'.format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


def get_neighbors(v, grid):
    if v in grid:
        return grid[v]
    return None


# Define the grid as a dictionary of {node: [(neighbor, cost)]}
nodes = ["S", "1", "2", "3", "4", "5", "T"]
locations = {'S': (0, 0), '1': (1, 0), '2': (2, 0), '3': (1, 1), '4': (2, 1), '5': (2, 2), 'T': (2, 3)}

heuristic = {node: manhattanDistance(locations[node], locations['T']) for node in locations}

# Define the adjacency cost matrix as a dictionary
grid = {
    'S': [('1', 1)],
    '1': [('2', 1)],
    '2': [('3', 1), ('5', 1)],
    '3': [('4', 1)],
    '4': [('T', 1)],
    '5': [('T', 1)],
    'T': []
}

# Start and end nodes
start = 'S'
end = 'T'

# Run the A* algorithm
Astar(start, end, grid)
